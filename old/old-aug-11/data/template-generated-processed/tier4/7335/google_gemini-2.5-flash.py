def solve():
    """Index: 7335.
    Returns: the amount of money Sophie saves in a year.
    """
    # L1
    loads_per_week = 4 # 4 loads of laundry a week
    sheets_per_load = 1 # 1 dryer sheet per load
    sheets_per_week = loads_per_week * sheets_per_load

    # L2
    weeks_per_year = 52 # WK
    total_sheets_per_year = sheets_per_week * weeks_per_year

    # L3
    sheets_per_box = 104 # 104 dryer sheets in a box
    boxes_needed = total_sheets_per_year / sheets_per_box

    # L4
    cost_per_box = 5.50 # A box of dryer sheets costs $5.50
    money_saved = cost_per_box * boxes_needed

    # FA
    answer = money_saved
    return answer