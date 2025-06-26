#!/bin/bash

source env/bin/activate

cd /home/pi/ZutrittskontrolleMobil25
git pull
pip install -r requirements.txt

ln -s /home/pi/ZutrittskontrolleMobil25/ZuKoMob25.service /etc/systemd/system/ZuKoMob25.service

systemctl enable ZuKoMob25.service

cp /home/pi/ZutrittskontrolleMobil25/splash.png /usr/share/plymouth/themes/pix/splash.png

shutdown -h now
