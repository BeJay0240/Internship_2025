#!/bin/bash

# Prompt the user for age
read -p "Enter your age: " age

# Check if input is a number
if ! [[ $age =~ ^[0-9]+$ ]]; then
    echo "Invalid input. Please enter a valid number."
    exit 1
fi

# Classify age groups
if (( age >= 0 && age <= 12 )); then
    echo "You are a child"
elif (( age >= 13 && age <= 19 )); then
    echo "You are a teenager"
elif (( age >= 20 && age <= 64 )); then
    echo "You are an adult"
else
    echo "You are a senior"
fi
