def solve():
    """Index: 5516.
    Returns: the number of lives a mouse has.
    """
    # L1
    cat_lives = 9 # A cat has nine lives
    dog_less_than_cat = 3 # 3 less lives than a cat
    dog_lives = cat_lives - dog_less_than_cat

    # L2
    mouse_more_than_dog = 7 # 7 more lives than a dog
    mouse_lives = dog_lives + mouse_more_than_dog

    # FA
    answer = mouse_lives
    return answer