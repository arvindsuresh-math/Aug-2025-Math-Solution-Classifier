def solve():
    """Index: 6241.
    Returns: the number of calories each person gets.
    """
    # L1
    num_oranges = 5 # James takes 5 oranges
    pieces_per_orange = 8 # breaks each orange into 8 pieces
    total_pieces = num_oranges * pieces_per_orange

    # L2
    num_people = 4 # 4 people
    pieces_per_person = total_pieces / num_people

    # L3
    fraction_of_orange_per_person = pieces_per_person / pieces_per_orange

    # L4
    calories_per_orange = 80 # an orange has 80 calories
    calories_per_person = calories_per_orange * fraction_of_orange_per_person

    # FA
    answer = calories_per_person
    return answer