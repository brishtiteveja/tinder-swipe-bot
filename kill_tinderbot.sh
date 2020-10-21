#!/bin/sh

pid_chrome=$(ps aux | grep -v grep |grep "Google Chrome" | tr -s " " | cut -d " " -f 2 | xargs)
echo "aaanandaaa0595" | sudo -S -k kill -9 $pid_chrome > /dev/null 2>&1

pid_tinder=$(ps aux | grep -v grep |grep tinder_bot | tr -s " " | cut -d " " -f 2 | xargs)
echo "aaanandaaa0595" | sudo -S -k kill -9 $pid_tinder > /dev/null 2>&1

