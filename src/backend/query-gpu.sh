#!/bin/bash

declare -a flags=(
# General
timestamp
driver_version
count
name
serial
fan.speed
pstate

# Memory
memory.total
memory.used
memory.free
compute_mode

# Utilization
utilization.gpu
utilization.memory

# Power
temperature.gpu
temperature.memory
power.management
power.draw

# Clock
clocks.current.graphics
clocks.current.sm
clocks.current.memory
clocks.current.video

# GOM
clocks_throttle_reasons.active
clocks_throttle_reasons.applications_clocks_setting
clocks_throttle_reasons.sw_power_cap
clocks_throttle_reasons.hw_slowdown
clocks_throttle_reasons.hw_thermal_slowdown
clocks_throttle_reasons.hw_power_brake_slowdown
clocks_throttle_reasons.sw_thermal_slowdown
clocks_throttle_reasons.sync_boost

# Errors
ecc.errors.corrected.volatile.device_memory
ecc.errors.corrected.volatile.dram
ecc.errors.corrected.volatile.register_file
ecc.errors.corrected.volatile.l1_cache
ecc.errors.corrected.volatile.l2_cache
ecc.errors.corrected.volatile.texture_memory
ecc.errors.corrected.volatile.cbu
ecc.errors.corrected.volatile.sram
ecc.errors.corrected.volatile.total
ecc.errors.corrected.aggregate.device_memory
ecc.errors.corrected.aggregate.dram
ecc.errors.corrected.aggregate.register_file
ecc.errors.corrected.aggregate.l1_cache
ecc.errors.corrected.aggregate.l2_cache
ecc.errors.corrected.aggregate.texture_memory
ecc.errors.corrected.aggregate.cbu
ecc.errors.corrected.aggregate.sram
ecc.errors.corrected.aggregate.total
ecc.errors.uncorrected.volatile.device_memory
ecc.errors.uncorrected.volatile.dram
ecc.errors.uncorrected.volatile.register_file
ecc.errors.uncorrected.volatile.l1_cache
ecc.errors.uncorrected.volatile.l2_cache
ecc.errors.uncorrected.volatile.texture_memory
ecc.errors.uncorrected.volatile.cbu
ecc.errors.uncorrected.volatile.sram
ecc.errors.uncorrected.volatile.total
ecc.errors.uncorrected.aggregate.device_memory
ecc.errors.uncorrected.aggregate.dram
ecc.errors.uncorrected.aggregate.register_file
ecc.errors.uncorrected.aggregate.l1_cache
ecc.errors.uncorrected.aggregate.l2_cache
ecc.errors.uncorrected.aggregate.texture_memory
ecc.errors.uncorrected.aggregate.cbu
ecc.errors.uncorrected.aggregate.sram
ecc.errors.uncorrected.aggregate.total
retired_pages.single_bit_ecc.count
)


printf -v var "%s," "${flags[@]}"
result=$(nvidia-smi --format=csv --query-gpu=$var)
filename="gpu-query.csv"
source "${BASH_SOURCE%/*}/helpers.sh"
filename=$(join $1 $filename)

tail_length=1
if [ -f "$filename" ]; then
    tail_length=2
fi

result=$(echo "$result" | tail -n +$tail_length)

while IFS= read -r line
do
    # echo "$line"
    fixed_line=$(echo "$line" | sed 's/,\s/;/g')

    # echo "$fixed_line"
    raw_values="$fixed_line$eol"
    echo $raw_values >> $filename
done < <(printf '%s\n' "$result")