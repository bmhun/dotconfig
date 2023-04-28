#!/bin/sh

# Disable beep
xset b off

# Keymap (sets keyboard map to the desired layout, in case of default "us" layout just comment it out)
setxkbmap -layout hu

# Mouse sensitivity
#   - Run xinput list
#   - Find your device and check its ID
#   - Run xinput list-props [DEVICE_ID]
#   - Find the property which controls the mouse sensitivity
#   - Finetune its value using: xinput set-prop [DEVICE_ID] [PROP_ID] [PROP_VALUE]
#   - Put your setting here (DEVICE_ID PROP_ID PROP_VALUE)
xinput set-prop 9 296 -0.6

# Volume (set the default output to a respectable 70% on boot)
pactl set-sink-volume @DEFAULT_SINK@ 70%

# Wallpaper (it restores the wallpaper settings you did in the nitrogen GUI)
nitrogen --restore &

# Compositor for effects and vsync (shows fancy blurring, rounded corners, fading and removes screen tearing)
picom &
