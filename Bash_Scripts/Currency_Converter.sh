#!/bin/bash

# Simple Currency Converter

echo "Welcome to the Currency Converter!"
echo "Available currencies: USD, EUR, GBP, JPY, GHC"

# Prompt user for input
read -p "Enter the amount: " amount
read -p "Enter the base currency (USD/EUR/GBP/JPY/GHC): " base
read -p "Enter the target currency (USD/EUR/GBP/JPY/GHC): " target

# Exchange rates (relative to USD for simplicity)
# 1 USD = X in target currency
USD_TO_GHC=11
USD_TO_EUR=0.93
USD_TO_GBP=0.80
USD_TO_JPY=149.50
USD_TO_USD=1

# Convert base currency to USD first
case $base in
    USD) amount_in_usd=$amount ;;
    GHC) amount_in_usd=$(echo "$amount / $USD_TO_GHC" | bc -l) ;;
    EUR) amount_in_usd=$(echo "$amount / $USD_TO_EUR" | bc -l) ;;
    GBP) amount_in_usd=$(echo "$amount / $USD_TO_GBP" | bc -l) ;;
    JPY) amount_in_usd=$(echo "$amount / $USD_TO_JPY" | bc -l) ;;
    *) echo "Invalid base currency"; exit 1 ;;
esac

# Convert USD to target currency
case $target in
    USD) result=$(echo "$amount_in_usd * $USD_TO_USD" | bc -l) ;;
    GHC) result=$(echo "$amount_in_usd * $USD_TO_GHC" | bc -l) ;;
    EUR) result=$(echo "$amount_in_usd * $USD_TO_EUR" | bc -l) ;;
    GBP) result=$(echo "$amount_in_usd * $USD_TO_GBP" | bc -l) ;;
    JPY) result=$(echo "$amount_in_usd * $USD_TO_JPY" | bc -l) ;;
    *) echo "Invalid target currency"; exit 1 ;;
esac

# Print result
printf "\n%.2f %s = %.2f %s\n" "$amount" "$base" "$result" "$target"


