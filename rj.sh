# !/bin/bash

RJ_PATH="/home/clz/local/rjsupplicant/rjsupplicant.sh"

echo $RJ_PATH

if [ -e $RJ_PATH ]
then
    while true
    do
        bash $RJ_PATH
        echo 锐捷断网 at `date`
        sleep 3
    done
fi
