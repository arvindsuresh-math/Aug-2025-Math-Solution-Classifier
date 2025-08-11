def solve():
    """Index: 4266.
    Returns: the number of chocolate bars Matilda's father had left.
    """
    # L1
    initial_chocolate_bars = 20 # 20 chocolate bars
    number_of_people = 5 # herself and her 4 sisters
    chocolate_bars_per_person = initial_chocolate_bars / number_of_people

    # L2
    half_divisor = 2 # half of their chocolate bars
    given_to_father_per_person = chocolate_bars_per_person / half_divisor

    # L3
    father_received_total = given_to_father_per_person * number_of_people

    # L4
    given_to_mother = 3 # gave 3 chocolate bars to their mother
    father_ate = 2 # ate 2
    father_chocolate_bars_left = father_received_total - given_to_mother - father_ate

    # FA
    answer = father_chocolate_bars_left
    return answer