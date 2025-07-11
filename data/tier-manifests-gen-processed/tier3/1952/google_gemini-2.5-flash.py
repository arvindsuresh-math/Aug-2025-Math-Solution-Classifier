def solve():
    """Index: 1952.
    Returns: the total earnings in dollars for the week.
    """
    # L1
    first_day_sales = 10 # On the first day, she sells ten candy bars
    daily_increase = 4 # sells four more candy bars than she sold the previous day each day afterward
    second_day_sales = first_day_sales + daily_increase

    # L2
    third_day_sales = second_day_sales + daily_increase

    # L3
    fourth_day_sales = third_day_sales + daily_increase

    # L4
    fifth_day_sales = fourth_day_sales + daily_increase

    # L5
    sixth_day_sales = fifth_day_sales + daily_increase

    # L6
    total_candies_week = first_day_sales + second_day_sales + third_day_sales + fourth_day_sales + fifth_day_sales + sixth_day_sales

    # L7
    cost_per_candy_cents = 10 # each candy bar costs 10 cents
    total_earnings_cents = total_candies_week * cost_per_candy_cents

    # L8
    cents_per_dollar = 100 # 1 dollar is equal to 100 cents
    total_earnings_dollars = total_earnings_cents / cents_per_dollar

    # FA
    answer = total_earnings_dollars
    return answer