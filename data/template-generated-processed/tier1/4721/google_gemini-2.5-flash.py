def solve():
    """Index: 4721.
    Returns: Louis's current age.
    """
    # L1
    carla_age_future = 30 # Carla will be 30 years old
    years_from_now = 6 # In 6 years
    carla_current_age = carla_age_future - years_from_now

    # L2
    sum_ages = 55 # The sum of the current ages of Carla and Louis is 55
    louis_current_age = sum_ages - carla_current_age

    # FA
    answer = louis_current_age
    return answer