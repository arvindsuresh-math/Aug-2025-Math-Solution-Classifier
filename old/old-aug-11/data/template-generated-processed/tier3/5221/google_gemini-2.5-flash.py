def solve():
    """Index: 5221.
    Returns: the total number of cakes the chef made.
    """
    # L1
    total_eggs = 60 # The chef has 60 eggs
    eggs_in_fridge = 10 # He puts 10 eggs in the fridge
    eggs_for_cakes = total_eggs - eggs_in_fridge

    # L2
    eggs_per_cake = 5 # used 5 eggs to make one cake
    num_cakes = eggs_for_cakes / eggs_per_cake

    # FA
    answer = num_cakes
    return answer