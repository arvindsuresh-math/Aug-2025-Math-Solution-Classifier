def solve():
    """Index: 3401.
    Returns: the number of notebooks Jack has left.
    """
    # L1
    jack_more_than_gerald = 13 # 13 more notebooks
    gerald_notebooks = 8 # Gerald has 8 notebooks
    jack_initial_notebooks = jack_more_than_gerald + gerald_notebooks

    # L2
    given_to_paula = 5 # gives 5 notebooks to Paula
    after_paula_given = jack_initial_notebooks - given_to_paula

    # L3
    given_to_mike = 6 # 6 notebooks to Mike
    jack_notebooks_left = after_paula_given - given_to_mike

    # FA
    answer = jack_notebooks_left
    return answer