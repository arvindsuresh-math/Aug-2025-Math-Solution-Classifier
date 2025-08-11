def solve():
    """Index: 239.
    Returns: the average pounds of peanuts Frank eats per day.
    """
    # L1
    one_dollar_bills_count = 7 # 7 one-dollar bills
    one_dollar_value = 1 # one-dollar bills
    total_one_dollar_value = one_dollar_bills_count * one_dollar_value

    # L2
    five_dollar_bills_count = 4 # 4 five-dollar bills
    five_dollar_value = 5 # five-dollar bills
    total_five_dollar_value = five_dollar_bills_count * five_dollar_value

    # L3
    ten_dollar_bills_count = 2 # 2 ten-dollar bills
    ten_dollar_value = 10 # ten-dollar bills
    total_ten_dollar_value = ten_dollar_bills_count * ten_dollar_value

    # L4
    twenty_dollar_bill_value = 20 # 1 twenty-dollar bill
    total_money = total_one_dollar_value + total_five_dollar_value + total_ten_dollar_value + twenty_dollar_bill_value

    # L5
    change_received = 4 # $4 in change
    money_spent = total_money - change_received

    # L6
    cost_per_pound = 3 # $3 a pound
    pounds_of_peanuts = money_spent / cost_per_pound

    # L7
    days_in_week = 7 # all in one week
    average_pounds_per_day = pounds_of_peanuts / days_in_week

    # FA
    answer = average_pounds_per_day
    return answer