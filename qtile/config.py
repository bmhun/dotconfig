# Import from config files (ide warns cause not used, but it is used)
from mouse import mouse
from keys import keys
from groups import groups
from layouts import layouts, floating_layout
from screens import screens, extension_defaults, widget_defaults
from hooks import *


#################################
#        Basic settings         #
#################################
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wmname = "Qtile"
