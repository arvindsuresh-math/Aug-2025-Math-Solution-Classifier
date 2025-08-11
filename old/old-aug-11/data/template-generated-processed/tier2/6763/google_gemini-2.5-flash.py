def solve():
    """Index: 6763.
    Returns: the number of boxes John has.
    """
    # L1
    stan_boxes = 100 # Stan has 100 boxes
    joseph_fewer_percent = 0.80 # 80% fewer boxes
    joseph_less_boxes = stan_boxes * joseph_fewer_percent

    # L2
    joseph_boxes = stan_boxes - joseph_less_boxes

    # L3
    jules_more_than_joseph = 5 # 5 more boxes than Joseph
    jules_boxes = joseph_boxes + jules_more_than_joseph

    # L4
    john_more_percent = 0.20 # 20% more boxes
    john_more_boxes = jules_boxes * john_more_percent

    # L5
    john_boxes = jules_boxes + john_more_boxes

    # FA
    answer = john_boxes
    return answer