def solve():
    """Index: 5524.
    Returns: the total amount Gondor earns.
    """
    # L1
    phones_monday = 3 # 3 phones last Monday
    phones_tuesday = 5 # 5 phones last Tuesday
    total_phones_repaired = phones_monday + phones_tuesday

    # L2
    earnings_per_phone = 10 # $10 from repairing a phone
    earnings_from_phones = earnings_per_phone * total_phones_repaired

    # L3
    laptops_wednesday = 2 # 2 laptops on Wednesday
    laptops_thursday = 4 # 4 laptops last Thursday
    total_laptops_repaired = laptops_wednesday + laptops_thursday

    # L4
    earnings_per_laptop = 20 # $20 from repairing a laptop
    earnings_from_laptops = earnings_per_laptop * total_laptops_repaired

    # L5
    total_earnings = earnings_from_laptops + earnings_from_phones

    # FA
    answer = total_earnings
    return answer