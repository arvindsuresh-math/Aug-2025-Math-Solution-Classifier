def solve():
    # Cost charged per lawn
    charge_per_lawn = 33

    # Number of lawns mowed last week
    num_lawns_mowed = 16

    # Number of customers who gave a tip
    num_customers_tipped = 3

    # Amount of tip per customer
    tip_per_customer = 10

    # Calculate earnings from mowing lawns (without tips)
    earnings_from_mowing = charge_per_lawn * num_lawns_mowed

    # Calculate total earnings from tips
    total_tips = num_customers_tipped * tip_per_customer

    # Calculate total earnings
    total_earnings = earnings_from_mowing + total_tips

    return total_earnings

# Execute the function to get the answer
answer = solve()