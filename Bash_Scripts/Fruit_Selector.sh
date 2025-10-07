#!/bin/bash

# Prompt the user to enter a fruit name
read -p "Enter a fruit name: " fruit

# Check the input
if [[ -z $fruit ]]; then
    echo "I don't recognize that fruit"
elif [[ $fruit == "apple" ]]; then
    echo "You chose an apple!"
elif [[ $fruit == "banana" ]]; then
    echo "Bananas are great!"
else
    echo "That's a nice choice!"
fi


