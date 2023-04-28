from libqtile.lazy import lazy
from libqtile.config import Drag, Click

from settings import mod


# Drag/control floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]
