#!/bin/bash

# Prompt the user for an integer
read -p "Enter an integer: " num

# Validate input (must be an integer, can be negative)
if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
    echo "Invalid input. Please enter an integer."
    exit 1
fi

# Check if number is even or odd using modulo
if (( num % 2 == 0 )); then
    echo "Even"
else
    echo "Odd"
fi

