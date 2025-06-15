#!/bin/bash

sleep 30

echo 'Hiding the mouse cursor...'
unclutter -idle 0.1 -root &

#chromium-browser --kiosk http://localhost:8000/web \
#  --noerrdialogs --disable-infobars --no-first-run \
#  --start-maximized --use-gl=egl

echo 'Starting Chromium...'
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --disable-gpu --disable-software-rasterizer --kiosk --hide-scrollbars --app=http://localhost:8000/web/
