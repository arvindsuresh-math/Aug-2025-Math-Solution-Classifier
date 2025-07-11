def solve():
    """Index: 1900.
    Returns: the total number of yards Peyton Manning threw the ball in two days.
    """
    # L1
    saturday_throws = 20 # he threw the ball 20 times
    saturday_yards_per_throw = 20 # he could throw only 20 yards
    saturday_total = saturday_throws * saturday_yards_per_throw

    # L2
    sunday_multiplier = 2 # twice the distance he could throw on Saturday
    sunday_yards_per_throw = sunday_multiplier * saturday_yards_per_throw

    # L3
    sunday_throws = 30 # he threw the ball 30 times
    sunday_total = sunday_throws * sunday_yards_per_throw

    # L4
    total_yards = sunday_total + saturday_total

    # FA
    answer = total_yards
    return answer