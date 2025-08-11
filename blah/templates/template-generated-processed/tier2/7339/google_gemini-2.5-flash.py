def solve():
    """Index: 7339.
    Returns: the total money earned from selling milk and butter.
    """
    # L1
    sticks_per_gallon = 2 # One gallon of milk equals 2 sticks of butter
    butter_price_per_stick = 1.5 # sells the butter for $1.5 a stick
    butter_value_per_gallon = sticks_per_gallon * butter_price_per_stick

    # L3
    milk_per_cow = 4 # Each cow produces 4 gallons of milk
    num_cows = 12 # She has 12 cows
    total_milk_produced = milk_per_cow * num_cows

    # L4
    milk_price_per_gallon = 3 # selling the milk at the market for $3 a gallon
    total_earnings = total_milk_produced * milk_price_per_gallon

    # FA
    answer = total_earnings
    return answer