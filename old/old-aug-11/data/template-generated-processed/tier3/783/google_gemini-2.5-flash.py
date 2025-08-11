def solve():
    """Index: 783.
    Returns: the difference in number between the zebras and the monkeys.
    """
    # L1
    parrots = 8 # 8 parrots
    snakes_multiplier = 3 # 3 times the number of snakes than parrots
    snakes = parrots * snakes_multiplier

    # L2
    monkeys_multiplier = 2 # 2 times the number of monkeys than snakes
    monkeys = snakes * monkeys_multiplier

    # L3
    parrots_and_snakes_sum = parrots + snakes

    # L4
    elephants_divisor = 2 # half the number of parrots and snakes added up
    elephants = parrots_and_snakes_sum / elephants_divisor

    # L5
    zebras_fewer = 3 # 3 fewer zebras than elephants
    zebras = elephants - zebras_fewer

    # L6
    difference_zebras_monkeys = monkeys - zebras

    # FA
    answer = difference_zebras_monkeys
    return answer