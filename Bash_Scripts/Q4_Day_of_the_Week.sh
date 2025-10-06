#!/bin/bash

# Prompt the user for a number
read -p "Enter a number between 1 and 7: " num

# Validate input (must be integer 1–7)
if ! [[ "$num" =~ ^[1-7]$ ]]; then
    echo "Invalid input"
    exit 1
fi

# Match number to day
case $num in
    1) echo "Monday" ;;
    2) echo "Tuesday" ;;
    3) echo "Wednesday" ;;
    4) echo "Thursday" ;;
    5) echo "Friday" ;;
    6) echo "Saturday" ;;
    7) echo "Sunday" ;;
esac
