#!/bin/bash

sleep 30

echo 'Hiding the mouse cursor...'
unclutter -idle 0.1 -root &

#chromium-browser --kiosk http://localhost:8000/web \
#  --noerrdialogs --disable-infobars --no-first-run \
#  --start-maximized --use-gl=egl

echo 'Starting Chromium...'
/usr/bin/chromium-browser https://developbyter.com \
  --window-position=0,0 \
  --start-fullscreen \
  --kiosk \
  --incognito \
  --noerrdialogs \
  --disable-translate \
  --no-first-run \
  --fast \
  --fast-start \
  --disable-infobars \
  --disable-features=TranslateUI \
  --disk-cache-dir=/dev/null \
  --overscroll-history-navigation=0 \
  --disable-pinch \
  --hide-scrollbars \
  --disable-gpu \
  --disable-software-rasterizer \
  --app=http://localhost:8000/web/