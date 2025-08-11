def solve():
    """Index: 6799.
    Returns: the total number of cell phones that were sold today.
    """
    # L1
    initial_samsung_inventory = 14 # started the day with 14 Samsung cell phones
    damaged_samsung = 2 # 2 Samsung cell phones were damaged
    working_samsung_initial = initial_samsung_inventory - damaged_samsung

    # L2
    initial_iphone_inventory = 8 # started with 8
    defective_iphone = 1 # 1 iPhone had a manufacturing defect
    working_iphone_initial = initial_iphone_inventory - defective_iphone

    # L3
    remaining_samsung = 10 # he has 10 Samsung cell phones
    samsung_sold = working_samsung_initial - remaining_samsung

    # L4
    remaining_iphone = 5 # he has 5 iPhones
    iphone_sold = working_iphone_initial - remaining_iphone

    # L5
    total_sold = samsung_sold + iphone_sold

    # FA
    answer = total_sold
    return answer