def solve():
    """Index: 239.
    Returns: the average number of pounds of peanuts Frank eats per day.
    """
    # L1
    one_dollar_bills = 7 # 7 one-dollar bills
    one_dollar_value = 1 # WK
    one_dollar_total = one_dollar_bills * one_dollar_value

    # L2
    five_dollar_bills = 4 # 4 five-dollar bills
    five_dollar_value = 5 # WK
    five_dollar_total = five_dollar_bills * five_dollar_value

    # L3
    ten_dollar_bills = 2 # 2 ten-dollar bills
    ten_dollar_value = 10 # WK
    ten_dollar_total = ten_dollar_bills * ten_dollar_value

    # L4
    twenty_dollar_bills = 1 # 1 twenty-dollar bill
    twenty_dollar_value = 20 # WK
    twenty_dollar_total = twenty_dollar_bills * twenty_dollar_value
    total_money = one_dollar_total + five_dollar_total + ten_dollar_total + twenty_dollar_total

    # L5
    change = 4 # $4 in change
    money_spent = total_money - change

    # L6
    price_per_pound = 3 # $3 a pound
    pounds_bought = money_spent / price_per_pound

    # L7
    days_in_week = 7 # WK
    average_per_day = pounds_bought / days_in_week

    # FA
    answer = average_per_day
    return answer