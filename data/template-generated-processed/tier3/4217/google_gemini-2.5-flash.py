def solve():
    """Index: 4217.
    Returns: the total number of tourists left at the end of the tour.
    """
    # L1
    initial_tourists = 30 # A group of 30 tourists
    eaten_by_anacondas = 2 # Two tourists are eaten by anacondas
    remaining_after_anacondas = initial_tourists - eaten_by_anacondas

    # L2
    poisoned_divisor = 2 # half the remaining tourists
    poisoned_tourists = remaining_after_anacondas / poisoned_divisor
    unpoisoned_tourists = remaining_after_anacondas - poisoned_tourists

    # L3
    recovered_divisor = 7 # 1/7 of the poisoned tourists recovered
    recovered_tourists = poisoned_tourists / recovered_divisor

    # L4
    total_surviving_tourists = unpoisoned_tourists + recovered_tourists

    # FA
    answer = total_surviving_tourists
    return answer