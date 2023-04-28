# This file has everything separated, so it's easy to modify one variable and change it everywhere
# Basically it has the dicts with the arguments, that are only used once (but it looks nice)
from libqtile import widget, qtile, bar
from libqtile.config import Screen

#################################
#    Importing theme settings   #
#################################
import themes
from settings import accent_main, accent_alternate, background_main, background_alternate, \
    active_text_color, inactive_text_color, arch_icon_name, bar_separator_image_based, bar_margin_before_menu, \
    run_launcher, power_menu, calendar, left_separator_icon_name, right_separator_icon_name, bar_window_display_mode, \
    bar_scale, bar_opacity, bar_shown, number_of_screens, main_screen, bar_separator, bar_margin, \
    bar_show_menu, bar_show_current_layout, bar_position, clock_style, groups_fontsize_multiplier

#################################
#    Calculating from scaling   #
#################################
scaled_bar_size = round(28 * bar_scale)
scaled_widget_fontsize = round(14 * bar_scale)
scaled_widget_padding = round(2 * bar_scale)
scaled_spacer = round(5 * bar_scale)
scaled_arch_margin_x = round(5 * bar_scale)
scaled_arch_margin_y = round(4.25 * bar_scale)
scaled_groupbox_fontsize = round(groups_fontsize_multiplier * scaled_widget_fontsize)
scaled_groupbox_margin_x = round(2 * bar_scale)
scaled_groupbox_margin_y = 4  # Does not need to be scaled, just fits better with this name
scaled_groupbox_border_width = round(3 * bar_scale)
scaled_separated_clock_fontsize = round(scaled_widget_fontsize * 1.15)
scaled_clock_fontsize = round(scaled_widget_fontsize * 1.1)
scaled_layout_fontsize = round(scaled_widget_fontsize * 1.1)

#################################
#      Widget/ext. defaults     #
#################################
widget_defaults = dict(
    font="Ubuntu",
    fontsize=scaled_widget_fontsize,
    padding=scaled_widget_padding,
    background=background_main,
    foreground=active_text_color,
)
extension_defaults = widget_defaults.copy()


#################################
#        Defining spacers       #
#################################
# Method to get spacers with scaling
def get_spacer_main(scale: float = 1):
    return widget.Spacer(length=scaled_spacer * scale, background=background_main)


def get_spacer_alt(scale: float = 1):
    return widget.Spacer(length=scaled_spacer * scale, background=background_alternate)


#################################
#           Separators          #
#################################
# Methods
def get_separator_alt_main():
    return widget.TextBox(
        bar_separator[0][0],
        foreground=background_alternate if not bar_separator[0][3] else background_main,
        background=background_main if not bar_separator[0][3] else background_alternate,
        fontsize=round(bar_separator[0][1] * bar_scale),
        padding=round(bar_separator[0][2] * bar_scale)
    ) if not bar_separator_image_based else widget.Image(
        filename="~/.config/qtile/icons/" + right_separator_icon_name,
        margin=0,
        margin_x=0,
        margin_y=0
    )


def get_separator_main_alt():
    return widget.TextBox(
        bar_separator[1][0],
        foreground=background_main if not bar_separator[1][3] else background_alternate,
        background=background_alternate if not bar_separator[1][3] else background_main,
        fontsize=round(bar_separator[1][1] * bar_scale),
        padding=round(bar_separator[1][2] * bar_scale)
    ) if not bar_separator_image_based else widget.Image(
        filename="~/.config/qtile/icons/" + left_separator_icon_name,
        margin=0,
        margin_x=0,
        margin_y=0
    )


#################################
#         Main menu icon        #
#################################
arch_args = {
    "background": background_alternate,
    "filename": "~/.config/qtile/icons/" + arch_icon_name,
    "scale": True,
    "mouse_callbacks": {
        'Button1': lambda: qtile.cmd_spawn(run_launcher),
        'Button3': lambda: qtile.cmd_spawn(power_menu)
    },
    "margin_x": scaled_arch_margin_x,
    "margin_y": scaled_arch_margin_y,
}

#################################
#     GroupBox customization    #
#################################
groupbox_args = {
    "highlight_method": "line",
    "highlight_color": background_alternate,
    "background": background_alternate,
    "active": active_text_color,
    "inactive": inactive_text_color,
    "fontsize": scaled_groupbox_fontsize,
    "disable_drag": True,
    "rounded": False,
    "borderwidth": scaled_groupbox_border_width,
    "margin_x": scaled_groupbox_margin_x,  # Bring them closer
    "margin_y": scaled_groupbox_margin_y,  # Centered vertically
    "other_screen_border": accent_alternate,  # Disable showing the group selected on the other screen
    "other_current_screen_border": accent_alternate,
    "this_screen_border": accent_main,
    "this_current_screen_border": accent_main,
}

#################################
#     Clocks (diff. layouts)    #
#################################
# Simple clock layout (same font size all along)
simple_clock_args = {
    "format": "%Y-%m-%d %A  %H:%M:%S",
    "background": background_alternate,
    "fontsize": scaled_clock_fontsize,
    "mouse_callbacks": {
        'Button1': lambda: qtile.cmd_spawn(calendar),
    },
}

# A better-looking clock with separate date (smaller font) and time (bigger font)
advanced_clock_date_args = {
    "format": "%Y-%m-%d %A",
    "background": background_alternate,
    "padding": 5,
    "mouse_callbacks": {
        'Button1': lambda: qtile.cmd_spawn(calendar),
    }
}

advanced_clock_time_args = {
    "format": "%H:%M:%S",
    "background": background_alternate,
    "fontsize": scaled_separated_clock_fontsize,
    "mouse_callbacks": {
        'Button1': lambda: qtile.cmd_spawn(calendar),
    }
}

#################################
#    Window name (remove tags)  #
#################################
window_name_args = {
    "format": "{name}",
}

#################################
#            Tasklist           #
#################################
tasklist_args = {
    "border": background_alternate,
    "icon_size": 0,
    "fontsize": 14,
    "padding": 5.5,
    "margin": 1,
    "borderwidth": 3,
    "highlight_method": "block",
    "txt_floating": "",
    "txt_maximized": "↕ ",
    "txt_minimized": "↓ "
}

#################################
#            Systray            #
#################################
systray_args = {
    "background": background_alternate
}

#################################
#          Layout text          #
#################################
layout_args = {
    "fontsize": scaled_layout_fontsize,
    "padding": 0,
}


#################################
#      Methods for widgets      #
#################################
# The spacer which makes it so that there is a distance between the beginning of the bar and the first widget
def get_start_spacer():
    return [
        get_spacer_alt(1),
    ]


# Main menu icon
def get_arch_icon():
    return [
        widget.Image(**arch_args),
        get_spacer_alt(),  # Spacer to make the group box look better after this
    ]


# Get groups
def get_groups():
    return [
        # The group box itself
        widget.GroupBox(**groupbox_args),

        # The separator after group box and potentially before the window title (if needed)
        get_separator_alt_main(),
        get_spacer_main(2)
    ]


# Literally just get the window name widget
def get_window_name():
    if bar_window_display_mode == "windowname":
        return [
            widget.WindowName(**window_name_args),
        ]
    elif bar_window_display_mode == "tasklist":
        return [
            widget.TaskList(**tasklist_args),
        ]
    else:
        return [
            widget.WindowName(**window_name_args, fmt="{}"),
        ]


# Standalone function to get the separator because the main screen might need the systray after this so its separate
def get_clock_separator():
    return [
        get_separator_main_alt(),
    ]


# Only called once, for the main screen
def get_systray():
    return [
        widget.Systray(**systray_args),
    ]


# Get the clock with its spacers
def get_clock():
    return [
        get_spacer_alt(),
        widget.Clock(**simple_clock_args),
        get_spacer_alt(),
    ] if clock_style == themes.clock_style_simple else [
        widget.Clock(**advanced_clock_date_args),
        widget.Clock(**advanced_clock_time_args),
        get_spacer_alt(2),
    ]


# Get layout text if required (with its separators and spacers)
def get_layout():
    return [
        # The separator after the clock
        get_separator_alt_main(),

        widget.CurrentLayout(**layout_args),
        get_spacer_main(3),
    ]


#################################
#     Assembling widget list    #
#################################
def get_widgets(main: bool):
    out = []

    # Start with a spacer to look good with rounded corners
    if bar_margin_before_menu:
        out.extend(get_start_spacer())

    # Arch icon menu if requested
    if bar_show_menu:
        out.extend(get_arch_icon())

    # Groups
    out.extend(get_groups())

    # Window name if requested
    out.extend(get_window_name())

    # Separator before the clock
    out.extend(get_clock_separator())

    # Systray if main screen
    if main:
        out.extend(get_systray())

    # Clock
    out.extend(get_clock())

    # Current layout text if requested
    if bar_show_current_layout:
        out.extend(get_layout())

    return out


def get_margins(margin: int, top: bool):
    return [margin if top else 0, margin, margin if not top else 0, margin]


def get_bar(main: bool, top: bool):
    return bar.Bar(get_widgets(main), scaled_bar_size, opacity=bar_opacity, margin=get_margins(bar_margin, top))


screens = []

for i in range(number_of_screens):
    if not bar_shown[i]:
        continue

    if main_screen == i:
        screens.append(Screen(
            top=get_bar(True, True) if bar_position == themes.bar_position_top else None,
            bottom=get_bar(True, False) if bar_position == themes.bar_position_bottom else None
        ))
    else:
        screens.append(Screen(
            top=get_bar(False, True) if bar_position == themes.bar_position_top else None,
            bottom=get_bar(False, False) if bar_position == themes.bar_position_bottom else None
        ))
