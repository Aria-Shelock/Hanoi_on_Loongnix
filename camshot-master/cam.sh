#!/bin/sh
camshot -W 640 -H 480 -p nenew_shot &
sleep 5
cat nenew_shot>/home/loongson/2021/pic/camshot.bmp
kill $(ps aux |grep camshot |grep -v grep|awk '{print$2}')
