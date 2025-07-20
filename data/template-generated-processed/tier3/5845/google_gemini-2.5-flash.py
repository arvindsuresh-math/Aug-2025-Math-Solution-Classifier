from fractions import Fraction

def solve():
    """Index: 5845.
    Returns: the total money Didi raised.
    """
    # L1
    num_cakes = 10 # 10 same-size cakes
    slices_per_cake = 8 # 8 slices per cake
    total_slices = num_cakes * slices_per_cake

    # L2
    price_per_slice = 1 # selling a slice for $1
    didi_sales = total_slices * price_per_slice

    # L3
    first_owner_donation_fraction = Fraction(50, 100) # 50 cents for each slice
    first_owner_donation = first_owner_donation_fraction * total_slices

    # L4
    second_owner_donation_fraction = Fraction(25, 100) # a quarter for each slice sold
    second_owner_donation = second_owner_donation_fraction * total_slices

    # L5
    total_money_raised = didi_sales + first_owner_donation + second_owner_donation

    # FA
    answer = total_money_raised
    return answer