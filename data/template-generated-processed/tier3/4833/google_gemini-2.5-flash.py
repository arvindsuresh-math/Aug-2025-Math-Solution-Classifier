def solve():
    """Index: 4833.
    Returns: the total number of animals John has.
    """
    # L1
    snakes = 15 # He has 15 snakes
    monkey_multiplier = 2 # twice as many monkeys
    monkeys = snakes * monkey_multiplier

    # L2
    fewer_lions = 5 # 5 fewer lions
    lions = monkeys - fewer_lions

    # L3
    more_pandas = 8 # 8 more pandas
    pandas = lions + more_pandas

    # L4
    dog_divisor = 3 # 1/3 as many dogs
    dogs = pandas / dog_divisor

    # L5
    total_animals = snakes + monkeys + lions + pandas + dogs

    # FA
    answer = total_animals
    return answer