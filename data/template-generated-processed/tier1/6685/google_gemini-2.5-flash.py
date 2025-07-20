def solve():
    """Index: 6685.
    Returns: the total number of pizzas made by Heather and Craig in two days.
    """
    # L1
    craig_pizzas_day1 = 40 # Craig made 40 pizzas on their first day
    heather_multiplier_day1 = 4 # four times as many pizzas as Craig
    heather_pizzas_day1 = heather_multiplier_day1 * craig_pizzas_day1

    # L2
    total_pizzas_day1 = heather_pizzas_day1 + craig_pizzas_day1

    # L3
    craig_more_pizzas_day2 = 60 # 60 more pizzas on their second day than their first day
    craig_pizzas_day2 = craig_more_pizzas_day2 + craig_pizzas_day1

    # L4
    heather_fewer_pizzas_day2 = 20 # 20 fewer pizzas than Craig's number
    heather_pizzas_day2 = craig_pizzas_day2 - heather_fewer_pizzas_day2

    # L5
    total_pizzas_day2 = heather_pizzas_day2 + craig_pizzas_day2

    # L6
    total_pizzas_two_days = total_pizzas_day2 + total_pizzas_day1

    # FA
    answer = total_pizzas_two_days
    return answer