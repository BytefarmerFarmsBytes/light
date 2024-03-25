#!/bin/sh
#
#GUI for TRIM4SSD-portable...
#

#
yad --center  --title="Action Light Changer" --form --width=400 --text="Select your color" \
--button="Red":light\ -s\ red --button="Green":light\ -s\ red --button="Blue":light\ -s\ red --button="Cyan":light\ -s\ red --button="Magenta":light\ -s\ red --button="Yellow":light\ -s\ red --button="White":light\ -s\ red --button="Black":light\ -s\ red
