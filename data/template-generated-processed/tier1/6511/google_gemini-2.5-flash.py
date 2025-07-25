def solve():
    """Index: 6511.
    Returns: the total number of toes on the Popton school bus.
    """
    # L1
    hoopit_hands = 4 # 4 hands
    hoopit_toes_per_hand = 3 # 3 toes on each of their 4 hands
    hoopit_toes_per_hoopit = hoopit_hands * hoopit_toes_per_hand

    # L2
    neglart_hands = 5 # 5 hands
    neglart_toes_per_hand = 2 # 2 toes on each of their 5 hands
    neglart_toes_per_neglart = neglart_hands * neglart_toes_per_hand

    # L3
    num_hoopit_students = 7 # 7 Hoopit students
    total_hoopit_toes_on_bus = num_hoopit_students * hoopit_toes_per_hoopit

    # L4
    num_neglart_students = 8 # 8 Neglart students
    total_neglart_toes_on_bus = num_neglart_students * neglart_toes_per_neglart

    # L5
    total_toes_on_bus = total_hoopit_toes_on_bus + total_neglart_toes_on_bus

    # FA
    answer = total_toes_on_bus
    return answer