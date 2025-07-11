def solve():
    """Index: 1781.
    Returns: the salesman's profit from selling all the backpacks.
    """
    # L1
    num_sold_swap_meet = 17 # sold 17 of them for $18 at the swap meet
    price_swap_meet = 18 # $18 at the swap meet
    revenue_swap_meet = num_sold_swap_meet * price_swap_meet

    # L2
    num_sold_department = 10 # 10 were sold to a department store
    price_department = 25 # $25 each
    revenue_department = num_sold_department * price_department

    # L3
    total_sold_so_far = num_sold_swap_meet + num_sold_department

    # L4
    total_bags = 48 # a case of 48 backpacks
    num_remaining = total_bags - total_sold_so_far
    price_remaining = 22 # remainder were sold for $22 each

    # L5
    revenue_remaining = num_remaining * price_remaining

    # L6
    total_revenue = revenue_swap_meet + revenue_department + revenue_remaining

    # L7
    cost = 576 # bought a case of 48 backpacks for $576
    profit = total_revenue - cost

    # FA
    answer = profit
    return answer