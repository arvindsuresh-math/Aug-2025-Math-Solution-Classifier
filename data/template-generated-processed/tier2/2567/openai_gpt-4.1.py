def solve():
    """Index: 2567.
    Returns: the total amount of money Hank donates to the local homeless shelter.
    """
    # L1
    carwash_proceeds = 100 # Hank makes $100 in a carwash
    carwash_donation_percent = 0.90 # donates 90% of the proceeds
    carwash_donation = carwash_proceeds * carwash_donation_percent

    # L2
    bakesale_proceeds = 80 # Hank makes $80 in a bake sale
    bakesale_donation_percent = 0.75 # donates 75% of the proceeds
    bakesale_donation = bakesale_proceeds * bakesale_donation_percent

    # L3
    mowing_proceeds = 50 # he makes $50 mowing lawns
    mowing_donation_percent = 1.00 # donates 100% of the proceeds
    mowing_donation = mowing_proceeds * mowing_donation_percent

    # L4
    total_donation = carwash_donation + bakesale_donation + mowing_donation

    # FA
    answer = total_donation
    return answer