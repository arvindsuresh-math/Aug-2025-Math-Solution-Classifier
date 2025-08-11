def solve():
    """Index: 2754.
    Returns: the number of oranges Emily has.
    """
    # L1
    sandra_times_betty = 3 # Sandra has 3 times as many oranges as Betty
    betty_oranges = 12 # Betty has 12 oranges
    sandra_oranges = sandra_times_betty * betty_oranges

    # L2
    emily_times_sandra = 7 # Emily has 7 times as many oranges as Sandra
    emily_oranges = emily_times_sandra * sandra_oranges

    # FA
    answer = emily_oranges
    return answer