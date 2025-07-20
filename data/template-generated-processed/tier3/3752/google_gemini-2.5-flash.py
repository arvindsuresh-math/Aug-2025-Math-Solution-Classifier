def solve():
    """Index: 3752.
    Returns: the total number of basketballs Lucca and Lucien have.
    """
    # L1
    lucca_total_balls = 100 # Lucca has 100 balls
    lucca_percentage_value = 10 # 10 percent of his balls
    percentage_divisor = 100 # (10 / 100)
    lucca_basketballs = lucca_total_balls * lucca_percentage_value / percentage_divisor

    # L2
    lucien_total_balls = 200 # Lucien has 200 balls
    lucien_percentage_value = 20 # 20 percent of them
    lucien_basketballs = lucien_total_balls * (lucien_percentage_value / percentage_divisor)

    # L3
    total_basketballs = lucca_basketballs + lucien_basketballs

    # FA
    answer = total_basketballs
    return answer