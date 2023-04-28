import os
import subprocess

from libqtile import hook


#################################
#      Starting components      #
#################################
@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


#################################
#         Picom shadows         #
#################################
@hook.subscribe.client_focus
def set_hint(window):
    window.window.set_property("QTILE_FLOATING", str(window.floating), type="STRING", format=8)
