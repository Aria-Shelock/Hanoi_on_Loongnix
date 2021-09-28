#!/bin/sh
camshot -W 640 -H 480 -p nenew_shot &
sleep 5
cat nenew_shot>camshot.bmp
