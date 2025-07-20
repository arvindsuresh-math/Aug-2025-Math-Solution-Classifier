def solve():
    """Index: 7215.
    Returns: the difference, in dollars, between the baker's daily average and total for today.
    """
    # L1
    avg_pastries_sold = 20 # sells 20 pastries
    pastry_price = 2 # pastries are sold for $2
    avg_pastry_sales = avg_pastries_sold * pastry_price

    # L2
    avg_bread_sold = 10 # sells 10 loaves of bread
    bread_price = 4 # loaves of bread are sold for $4
    avg_bread_sales = avg_bread_sold * bread_price

    # L3
    total_daily_average = avg_pastry_sales + avg_bread_sales

    # L4
    today_pastries_sold = 14 # Today, he sells 14 pastries
    today_pastry_sales = today_pastries_sold * pastry_price

    # L5
    today_bread_sold = 25 # Today, he sells 25 loaves of bread
    today_bread_sales = today_bread_sold * bread_price

    # L6
    total_today_sales = today_pastry_sales + today_bread_sales

    # L7
    difference = total_today_sales - total_daily_average

    # FA
    answer = difference
    return answer