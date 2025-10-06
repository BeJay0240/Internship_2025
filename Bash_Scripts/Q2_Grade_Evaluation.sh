#!/bin/bash

# Prompt the user for a numeric grade
read -p "Enter a numeric grade (0-100): " grade

# Validate input (check if it's a number between 0 and 100)
if ! [[ "$grade" =~ ^[0-9]+$ ]] || [ "$grade" -lt 0 ] || [ "$grade" -gt 100 ]; then
    echo "Invalid input. Please enter a number between 0 and 100."
    exit 1
fi

# Determine the letter grade
if [ "$grade" -ge 90 ]; then
    echo "Letter Grade: A"
elif [ "$grade" -ge 80 ]; then
    echo "Letter Grade: B"
elif [ "$grade" -ge 70 ]; then
    echo "Letter Grade: C"
elif [ "$grade" -ge 60 ]; then
    echo "Letter Grade: D"
else
    echo "Letter Grade: F"
fi
