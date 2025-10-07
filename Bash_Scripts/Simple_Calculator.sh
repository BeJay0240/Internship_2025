#!/bin/bash

#!/bin/bash

# Prompt the user for input
read -p "Enter first number: " num1
read -p "Enter second number: " num2
read -p "Enter an operator (+, -, *, /): " op

# Perform the operation
case $op in
    +)
        result=$((num1 + num2))
        echo "Result: $result"
        ;;
    -)
        result=$((num1 - num2))
        echo "Result: $result"
        ;;
    \*)
        result=$((num1 * num2))
        echo "Result: $result"
        ;;
    /)
        if [[ $num2 -eq 0 ]]; then
            echo "Error: Division by zero"
        else
            result=$((num1 / num2))
            echo "Result: $result"
        fi
        ;;
    *)
        echo "Invalid operator"
        ;;
esac
