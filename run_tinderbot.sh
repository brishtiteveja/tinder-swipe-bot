#! /bin/bash

password="aaanandaaa0595"

COUNTER=1
RERUN=1800
while true; 
do
	cmd="python tinder_bot.py"
    tcmd="tinder_bot.py"
	res=$(ps aux | grep -v grep | grep $tcmd)
    echo $res

	if [ -z "$res" ] 
	then
		echo "Running the tinderbot again"
		echo $password | sudo -S -k sh kill_tinderbot.sh 
		$cmd > log_tinderbot.txt &
	else
		echo "-"
	fi

	sleep 10 
	TIME=$(($COUNTER * 10))
	echo "Time="$TIME"sec"
	COUNTER=$[$COUNTER +1]

	if [ $TIME -ge $RERUN ]
	then
		echo "tinder bot will be killed and rerun now"
		echo $password | sudo -S -k sh kill_tinderbot.sh 
		COUNTER=1
	fi
done
