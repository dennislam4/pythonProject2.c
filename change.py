# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 6/21/2022
# Description: Asks the user number of cents, from 0 to 99, and outputs how many of each type of coin would represent
#              that amount with the fewest total number of coins.

print("Please enter an amount in cents less than a dollar.")
coins = int(input())
quarters = coins // 25
coins %= 25
dimes = coins // 10
coins %= 10
nickels = coins // 5
coins %= 5
pennies = coins // 1
coins %= 1
print(f"Your change will be:\nQ: {quarters}\nD: {dimes}\nN: {nickels}\nP: {pennies}")
