def solve():
    """Index: 5970.
    Returns: the number of servings of popcorn Jared should order.
    """
    # L1
    pieces_per_friend = 60 # each eat 60 pieces of popcorn
    number_of_friends = 3 # his three other friends
    friends_total_popcorn = pieces_per_friend * number_of_friends

    # L2
    jared_popcorn = 90 # Jared can eat 90 pieces of popcorn
    total_popcorn_eaten = friends_total_popcorn + jared_popcorn

    # L3
    pieces_per_serving = 30 # 30 pieces of popcorn in a serving
    servings_needed = total_popcorn_eaten / pieces_per_serving

    # FA
    answer = servings_needed
    return answer