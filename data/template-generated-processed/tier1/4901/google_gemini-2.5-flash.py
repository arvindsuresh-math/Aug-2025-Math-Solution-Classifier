def solve():
    """Index: 4901.
    Returns: my current age.
    """
    # L1
    dog_age_in_future = 4 # my dog will turn 4 years old
    years_from_now = 2 # Two years from now
    dog_current_age = dog_age_in_future - years_from_now

    # L2
    my_age_when_dog_born = 15 # I was 15 years old
    my_current_age = my_age_when_dog_born + dog_current_age

    # FA
    answer = my_current_age
    return answer