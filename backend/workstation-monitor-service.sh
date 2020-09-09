#!/bin/bash

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
log_dir=${HOME}"/workstation-monitor/"$timestamp
[ -d $log_dir ] || mkdir $log_dir -p
echo "Logging to $log_dir"

workspace_root=${BASH_SOURCE%/*}/..
export PYTHONPATH=$workspace_root
cd "$workspace_root" || exit
# shellcheck disable=SC1090
source "$workspace_root"/backend/venv/bin/activate

cd $workspace_root || exit
python backend/monitor.py --output_dir=$log_dir
