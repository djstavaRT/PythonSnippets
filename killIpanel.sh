#!/bin/sh

ps -ef|grep -v grep|grep lj_rescue.py|while read u p o
do
    kill -9 $p
done
