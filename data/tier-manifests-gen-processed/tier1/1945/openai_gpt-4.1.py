def solve():
    """Index: 1945.
    Returns: the number of pounds of apples Diego can buy.
    """
    # L1
    watermelon_pounds = 1 # a pound of watermelon
    grapes_pounds = 1 # a pound of grapes
    oranges_pounds = 1 # a pound of oranges
    non_apple_pounds = watermelon_pounds + grapes_pounds + oranges_pounds

    # L2
    total_capacity = 20 # can carry 20 pounds of fruit
    apple_pounds = total_capacity - non_apple_pounds

    # FA
    answer = apple_pounds
    return answer