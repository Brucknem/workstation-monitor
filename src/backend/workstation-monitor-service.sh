#!/bin/bash

modprobe asus-wmi-sensors
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
log_dir="/var/log/workstation-monitor/"$timestamp
[ -d $log_dir ] || mkdir $log_dir -p
echo "Logging to $log_dir"

while true; do
    /bin/bash ${BASH_SOURCE%/*}/query-all.sh $log_dir
    sleep 1
done
