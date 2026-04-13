#!/bin/bash

# check if input is given
if [ -z "$1" ]; then
    echo "usage: $0 <target_ip>"
    exit 1
fi

TARGET="$1"

# date for file name
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

OUTPUT="scan_${TARGET}_${DATE}.txt"

# basic ports
PORTS=(21 22 80 443 3306)

echo "scanning $TARGET"

# write header
echo "scan results for $TARGET" > "$OUTPUT"
echo "date: $DATE" >> "$OUTPUT"
echo "-------------------" >> "$OUTPUT"

open_count=0

# scan ports
for port in "${PORTS[@]}"; do
    if nc -z -w 1 "$TARGET" "$port" &>/dev/null; then
        echo "port $port open"
        echo "port $port open" >> "$OUTPUT"
        ((open_count++))
    else
        echo "port $port closed"
        echo "port $port closed" >> "$OUTPUT"
    fi
done

# summary
echo "-------------------" >> "$OUTPUT"
echo "open ports: $open_count" >> "$OUTPUT"

echo "done"
echo "open ports: $open_count"
echo "saved in $OUTPUT"

