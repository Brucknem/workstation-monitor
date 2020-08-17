#!/bin/bash
eol=$'\n'
raw_sensors="$(sensors)"
declare -A adapters

name=""
while IFS= read -r line
do
    if [ -z "$line" ]; then
        continue
    fi
    # echo "$line"

    if [[ $line == *":"* ]]; then
        adapters["$name"]+=$line$eol
    else
        name="$line"
    fi
done < <(printf '%s\n' "$raw_sensors")

output_folder="sensors/"
[ -d $output_folder ] || mkdir -p $output_folder

for i in "${!adapters[@]}"
do 
    filename="$output_folder$i.csv"
    sensors="${adapters[$i]}"
    # printf "%s\n%s\n" "$filename" "$sensors"

    sensors="${sensors//:/$eol}"    
    readarray -t sensors<<<"$sensors"

    keys=""
    values=""

    for i in "${!sensors[@]}"; do 
        if [[ $((i % 2)) == 0 ]]
        then
            key="$(echo -e "${sensors[$i]}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
            value="$(echo -e "${sensors[$i+1]}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
            keys+=$key";"
            values+=$value";"
        fi
    done

    if [ ! -f "$filename" ]; then
        echo $keys > $filename
    fi
    echo $values >> $filename
done