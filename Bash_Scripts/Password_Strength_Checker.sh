#!/bin/bash

# Prompt the user for a password
read -sp "Enter your password: " password
echo

# Get the length of the password
length=${#password}

# Check for letters and numbers
if [[ $password =~ [A-Za-z] && $password =~ [0-9] && $length -ge 8 ]]; then
    echo "Strong password"
elif [[ $length -ge 6 && $length -lt 8 && $password =~ [A-Za-z] ]]; then
    echo "Moderate password"
else
    echo "Weak password"
fi
