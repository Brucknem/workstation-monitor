#!/bin/bash
eol=$'\n'
cpu_values_raw="$(mpstat -P ALL)"
filename="cpu-query.csv"
source "${BASH_SOURCE%/*}/helpers.sh"
filename=$(join $1 $filename)

tail_length=3
if [ -f "$filename" ]; then
    tail_length=4
fi

cpu_values_raw=$(echo "$cpu_values_raw" | tail -n +$tail_length)
while IFS= read -r line
do
    # echo "$line"
    fixed_line=$(echo $line | tr -s '[:blank:]' ';')
    # echo "$fixed_line"
    cpu_values="$fixed_line$eol"
    echo $cpu_values >> $filename
done < <(printf '%s\n' "$cpu_values_raw")