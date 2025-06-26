def solve_71():
    # Price per craft
    price_per_craft = 12
    # Number of crafts sold
    num_crafts_sold = 3
    # Extra money received from customer
    extra_money = 7
    # Amount deposited into bank account
    amount_deposited = 18

    # Calculate total earnings from selling crafts
    earnings_from_crafts = num_crafts_sold * price_per_craft

    # Calculate total earnings including the extra money
    total_earnings = earnings_from_crafts + extra_money

    # Calculate the amount Hillary is left with after making the deposit
    money_left = total_earnings - amount_deposited

    return money_left

# Execute the function to get the answer
# print(solve_71())