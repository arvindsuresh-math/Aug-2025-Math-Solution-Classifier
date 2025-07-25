def solve():
    """Index: 4297.
    Returns: the average price of each DVD bought.
    """
    # L1
    num_dvds_box1 = 10 # 10 movies
    price_per_dvd_box1 = 2.00 # $2.00 apiece
    cost_box1 = num_dvds_box1 * price_per_dvd_box1

    # L2
    num_dvds_box2 = 5 # 5 movies
    price_per_dvd_box2 = 5.00 # $5 each
    cost_box2 = num_dvds_box2 * price_per_dvd_box2

    # L3
    total_dvds = num_dvds_box1 + num_dvds_box2

    # L4
    total_spent = cost_box1 + cost_box2

    # L5
    average_price = total_spent / total_dvds

    # FA
    answer = average_price
    return answer