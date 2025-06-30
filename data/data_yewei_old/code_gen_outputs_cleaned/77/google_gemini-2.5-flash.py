def solve():
    initial_weight_kg = 97
    weight_loss_per_month_kg = 3
    months_until_fight = 4

    # Calculate the total weight lost over the months
    total_weight_loss_kg = weight_loss_per_month_kg * months_until_fight

    # Calculate the final weight on the day of the fight
    final_weight_kg = initial_weight_kg - total_weight_loss_kg

    return final_weight_kg

# Execute the function to get the answer
final_weight = solve()