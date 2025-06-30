def solve_59():
    # Coins collected in the first hour
    coins_hour_1 = 15
    # Coins collected in the second hour
    coins_hour_2 = 35
    # Coins collected in the third hour
    coins_hour_3 = 35
    # Coins collected in the fourth hour
    coins_hour_4 = 50
    # Coins given to coworker
    coins_given_away = 15

    # Calculate the total coins collected before giving any away
    total_coins_collected = coins_hour_1 + coins_hour_2 + coins_hour_3 + coins_hour_4

    # Calculate the final number of coins after giving some away
    final_coins = total_coins_collected - coins_given_away

    return final_coins

# Execute the function to get the answer
# print(solve_59())