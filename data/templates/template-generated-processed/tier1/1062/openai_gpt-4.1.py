def solve():
    """Index: 1062.
    Returns: the number of sandwiches Ruth prepared.
    """
    # L1
    num_other_cousins = 2 # her two other cousins arrived
    sandwiches_per_other_cousin = 1 # ate 1 sandwich each
    sandwiches_eaten_by_other_cousins = num_other_cousins * sandwiches_per_other_cousin

    # L2
    sandwiches_left_after_all = 3 # There were 3 sandwiches left.
    sandwiches_left_before_other_cousins = sandwiches_left_after_all + sandwiches_eaten_by_other_cousins

    # L3
    sandwiches_eaten_by_first_cousin = 2 # her first cousin arrived and ate 2 sandwiches
    sandwiches_left_before_first_cousin = sandwiches_left_before_other_cousins + sandwiches_eaten_by_first_cousin

    # L4
    sandwiches_eaten_by_ruth = 1 # She ate 1 sandwich
    sandwiches_given_to_brother = 2 # gave 2 sandwiches to her brother
    sandwiches_eaten_by_ruth_and_brother = sandwiches_eaten_by_ruth + sandwiches_given_to_brother

    # L5
    sandwiches_prepared = sandwiches_left_before_first_cousin + sandwiches_eaten_by_ruth_and_brother

    # FA
    answer = sandwiches_prepared
    return answer