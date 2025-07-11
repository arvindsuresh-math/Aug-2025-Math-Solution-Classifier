def solve():
    """Index: 2622.
    Returns: the number of jelly beans Mikey has.
    """
    # L1
    napoleon_jelly_beans = 17 # Napoleon has 17 jelly beans
    sedrich_more_jelly_beans = 4 # Sedrich has 4 more jelly beans than Napoleon
    sedrich_jelly_beans = napoleon_jelly_beans + sedrich_more_jelly_beans

    # L2
    sum_napoleon_sedrich = napoleon_jelly_beans + sedrich_jelly_beans

    # L3
    twice_multiplier = 2 # Twice the sum
    twice_sum = sum_napoleon_sedrich * twice_multiplier

    # L4
    mikey_divisor = 4 # 4 times the number of jelly beans that Mikey has
    mikey_jelly_beans = twice_sum / mikey_divisor

    # FA
    answer = mikey_jelly_beans
    return answer