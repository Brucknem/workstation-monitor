#!/bin/bash

# modprobe asus-wmi-sensors
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
log_dir=${HOME}"/workstation-monitor/"$timestamp
[ -d $log_dir ] || mkdir $log_dir -p
echo "Logging to $log_dir"

workspace_root=${BASH_SOURCE%/*}/../..
cd $workspace_root
source $workspace_root/venv/bin/activate

cd $workspace_root
bazel run //src/backend:monitor -- --output_dir=$log_dir
