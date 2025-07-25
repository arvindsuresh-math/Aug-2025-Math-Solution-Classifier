def solve():
    """Index: 2816.
    Returns: the number of frogs that hatch out of the 800 eggs.
    """
    # L1
    total_eggs = 800 # 800 eggs a year
    dry_percent = 0.10 # 10 percent dry up
    dried_eggs = total_eggs * dry_percent

    # L2
    eaten_percent = 0.70 # 70 percent are eaten
    eaten_eggs = total_eggs * eaten_percent

    # L3
    eggs_left = total_eggs - dried_eggs - eaten_eggs

    # L4
    hatch_divisor = 4 # 1/4 of the remaining eggs end up hatching
    hatched_eggs = eggs_left / hatch_divisor

    # FA
    answer = hatched_eggs
    return answer