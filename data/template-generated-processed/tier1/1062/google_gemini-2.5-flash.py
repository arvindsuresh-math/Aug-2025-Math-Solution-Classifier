def solve():
    """Index: 1062.
    Returns: the total number of sandwiches Ruth prepared.
    """
    # L1
    num_other_cousins = 2 # two other cousins arrived
    sandwiches_per_other_cousin = 1 # ate 1 sandwich each
    sandwiches_eaten_by_two_cousins = num_other_cousins * sandwiches_per_other_cousin

    # L2
    sandwiches_left_at_end = 3 # 3 sandwiches left
    sandwiches_before_two_cousins = sandwiches_left_at_end + sandwiches_eaten_by_two_cousins

    # L3
    sandwiches_first_cousin_ate = 2 # first cousin arrived and ate 2 sandwiches
    sandwiches_before_first_cousin = sandwiches_before_two_cousins + sandwiches_first_cousin_ate

    # L4
    ruth_ate = 1 # She ate 1 sandwich
    brother_ate = 2 # gave 2 sandwiches to her brother
    sandwiches_ruth_and_brother_ate = ruth_ate + brother_ate

    # L5
    total_prepared_sandwiches = sandwiches_before_first_cousin + sandwiches_ruth_and_brother_ate

    # FA
    answer = total_prepared_sandwiches
    return answer