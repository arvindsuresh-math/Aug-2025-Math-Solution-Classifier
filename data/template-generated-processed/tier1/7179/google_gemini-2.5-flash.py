def solve():
    """Index: 7179.
    Returns: the greatest difference between the number of each color of marble in the baskets.
    """
    # L1
    red_marbles_A = 4 # Basket A contains 4 red marbles
    yellow_marbles_A = 2 # and 2 yellow marbles
    diff_A = red_marbles_A - yellow_marbles_A

    # L2
    green_marbles_B = 6 # Basket B contains 6 green marbles
    yellow_marbles_B = 1 # and 1 yellow marble
    diff_B = green_marbles_B - yellow_marbles_B

    # L3
    white_marbles_C = 3 # Basket C contains 3 white marbles
    yellow_marbles_C = 9 # and 9 yellow marbles
    diff_C = yellow_marbles_C - white_marbles_C

    # L4
    greatest_difference = max(diff_A, diff_B, diff_C)

    # FA
    answer = greatest_difference
    return answer