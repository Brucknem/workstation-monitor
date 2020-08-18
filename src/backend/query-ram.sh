#!/bin/bash
eol=$'\n'
raw_values_raw="type ""$(free -wm)"
filename="ram-query.csv"
source "${BASH_SOURCE%/*}/helpers.sh"
filename=$(join $1 $filename)

tail_length=1
if [ -f "$filename" ]; then
    tail_length=2
fi

raw_values_raw=$(echo "$raw_values_raw" | tail -n +$tail_length)
while IFS= read -r line
do
    # echo "$line"
    fixed_line=$(echo $line | tr -s '[:blank:]' ';')
    fixed_line=$(echo "${fixed_line//:}")
    # echo "$fixed_line"
    raw_values="$fixed_line$eol"
    echo $raw_values >> $filename
done < <(printf '%s\n' "$raw_values_raw")