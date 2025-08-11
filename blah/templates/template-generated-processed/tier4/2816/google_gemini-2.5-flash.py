def solve():
    """Index: 2816.
    Returns: the number of frogs that hatch.
    """
    # L1
    total_eggs = 800 # 800 eggs a year
    dried_up_percent = 0.10 # 10 percent dry up
    dried_up_eggs = total_eggs * dried_up_percent

    # L2
    eaten_percent = 0.70 # 70 percent are eaten
    eaten_eggs = total_eggs * eaten_percent

    # L3
    remaining_eggs = total_eggs - dried_up_eggs - eaten_eggs

    # L4
    hatching_divisor = 4 # 1/4 of the remaining eggs end up hatching
    hatched_frogs = remaining_eggs / hatching_divisor

    # FA
    answer = hatched_frogs
    return answer