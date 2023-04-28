from libqtile.lazy import lazy
from libqtile.config import Key

from settings import terminal, browser, filemanager, texteditor, run_launcher, locker, dropdowns,\
    mod, alt, control, shift

# Setting up the keybindings
keys = [
    # Custom keys for essential things
    Key([mod], "e", lazy.spawn(filemanager), desc="Open filemanager"),
    Key([mod], "t", lazy.spawn(browser), desc="Open browser"),
    Key([mod], "k", lazy.spawn(texteditor), desc="Open text editor"),
    Key([alt], "space", lazy.spawn(run_launcher), desc="Open launcher"),

    # Switch between windows (focus)
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving windows in group
    Key([mod, shift], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, shift], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, shift], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, shift], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Resizing windows
    Key([mod, control], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Playerctl commands (comment if you don't have playerctl installed)
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to next song"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next song"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Skip to next song"),

    # Basic functionality
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Key([mod], "p", lazy.spawn(sound_control), desc="Spawn an alsamixer inside the terminal"),  # Now as scratchpad
    Key([mod], "l", lazy.spawn(locker), desc="Lock the screen"),
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),  # Replaced with rofi

    # Qtile commands
    Key([mod, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Escape", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
]


# Get dropdown keys
def get_dropdown_keys():
    out = []

    for dd in dropdowns:
        modifiers = dd[0]
        key = dd[1]
        name = dd[2]

        out.append(
            Key(
                modifiers,
                key,
                lazy.group["scratchpad"].dropdown_toggle(name),
                desc="Toggle {} dropdown".format(name)
            )
        )
    return out


# Add dropdown keys to the list
keys.extend(get_dropdown_keys())

