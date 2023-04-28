# The configuration file where this qtile config's easily modifiable settings live (bit chaotic)
# You can select themes, screen settings, basic software commands and many more options (to open with keybindings)
# You can customize layouts in the layouts.py and keybindings in the keys.py file
import os

import themes


#################################
#         Key modifiers         #
#################################
mod = "mod4"
alt = "mod1"
shift = "shift"
control = "control"


#################################
#         Look and feel         #
#################################
# Select color theme
color_theme = themes.colors_dark_monochrome

# Select design (set None to use custom settings)
design_theme = themes.design_minimal

# Window related settings (only works if design is set to None)
wm_margin = themes.margin_default           # Margin between open windows (and around)
wm_border_radius = themes.br_rounder        # Window border radius (affecting picom configuration)
bar_margin = themes.margin_full             # Space around the bar (except bottom or top when bar is bottom mounted)

# Other design settings (unrelated to the design set)
wm_border_width = themes.bw_borderless      # Border width around windows
bar_scale = 1                               # Scale of the bar (applies to everything except margins around it)
bar_opacity = themes.opacity_eyecandy       # Opacity level of the bar
bar_separator_image_based = False           # Whether to use the round, image based separators
bar_separator = themes.bar_separator_backslash
bar_margin_before_menu = True               # Whether to have margins before the main menu icon in the bar
bar_show_menu = True                        # Whether to show the menu (left click: run launcher, right click: htop)
bar_window_display_mode = themes.windows_tasklist
bar_show_current_layout = False             # Whether to show the current layout as text after the clock
bar_position = themes.bar_position_top      # Where to place the bar

# Widgets settings
clock_style = themes.clock_style_advanced

# Screen settings
number_of_screens = 2   # Number of screens used with the current display server
main_screen = 0         # The index of the main screen (first -> 0)
bar_shown = [           # Boolean for each screen whether to show a bar (in the order that the display server uses)
    True,
    False,
]


#################################
#           Software            #
#################################
# Basic software
terminal = "alacritty"
browser = "firefox"
filemanager = "thunar"
texteditor = "gedit"
calculator = "qalculate-gtk"
calendar = ""

# Other
locker = "slock"
run_launcher = "rofi -show drun"
power_menu = "/home/bm/.config/rofi/powermenu/powermenu"
terminal_run = terminal + " -e "
sound_control = terminal_run + "alsamixer"
system_monitor = terminal_run + "htop"


#################################
#            Groups             #
#################################
group_switch_on_move = False  # Whether to switch when moving a window to a different group

# More other settings related to groups
# KEY, LABEL, LAYOUT, MATCH_CLASS
group_config = [
    ["0", "", "max", ["firefox"]],
    ["1", "", "columns", ["alacritty"]],
    ["2", "", "max", ["jetbrains-pycharm-ce", "jetbrains-idea-ce"]],
    ["3", "", "columns", ["thunar"]],
    ["4", "", "max", ["gedit"]],
    ["5", "", "max", ["discord"]],
    ["6", "", "max", []],
    ["7", "", "columns", []],
    ["8", "", "columns", []],
]

groups_fontsize_multiplier = 1.2  # 1 if TEXT; 1.2 if ICONS


#################################
#     Scratchpads/DropDowns     #
#################################
# Define scratchpads (dropdowns) here easily (these are centered by default)
# MODIFIERS, KEY, NAME, COMMAND, WIDTH, HEIGHT, [OPACITY] (dimensions should be given in a float 0 to 1)
dropdowns = [
    [[mod], "c", "calculator", calculator, 0.355, 0.5],
    [[mod], "p", "sound_control", sound_control, 0.5, 0.5],
    [[mod], "h", "system_monitor", system_monitor, 0.5, 0.5],
    [[mod], "Backspace", "terminal", terminal, 0.5, 0.5],
    [[mod], "s", "spotify", "spotify-launcher", 0.7, 0.7],
]


#################################
#           Layouts             #
#################################
# Windows that will be floating by default
floating_window_classes = [
    "confirmreset",  # gitk
    "makebranch",  # gitk
    "maketag",  # gitk
    "ssh-askpass",  # ssh-askpass
    "qalculate-gtk",  # calculator
    "virt-manager",  # virt-manager
    "spotify",  # music
]

floating_window_titles = [
    "branchdialog",  # gitk
    "pinentry",  # GPG key password entry
]


# !!! WARNING: You might break something if you edit this !!! (getting variables from selected color theme)
background_main = color_theme[0]
background_alternate = color_theme[1]
active_text_color = color_theme[2]
inactive_text_color = color_theme[3]
accent_main = color_theme[4]
accent_alternate = color_theme[5]
wm_border_focus = color_theme[6]
wm_border_normal = color_theme[7]
arch_icon_name = color_theme[8]
left_separator_icon_name = color_theme[9]
right_separator_icon_name = color_theme[10]


# Extracting design if set
if design_theme is not None:
    wm_margin = design_theme[0]
    wm_border_radius = design_theme[1]
    bar_margin = design_theme[2]


# Change picom config depending on settings
# Exclude bar from rounded corners if docked (0 margin) (this assumes that the configuration has this line)
if bar_margin == 0:
    os.system("sed -i '/QTILE_INTERNAL:32c = 1/s/^#//g' ~/.config/picom/picom.conf")
else:
    os.system("sed -i '/QTILE_INTERNAL:32c = 1/s/^/#/g' ~/.config/picom/picom.conf")


# Set border radius (this also assumes that the config contains the option already)
os.system("sed -i 's/corner-radius =.*/corner-radius = " +
          str(wm_border_radius if wm_margin != 0 else 0) +
          ";/' ~/.config/picom/picom.conf")
