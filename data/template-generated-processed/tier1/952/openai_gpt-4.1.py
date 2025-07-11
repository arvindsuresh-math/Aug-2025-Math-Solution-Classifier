def solve():
    """Index: 952.
    Returns: the total amount of fish sold in two weeks.
    """
    # L1
    first_week_kg = 50 # sold 50 kg of salmon
    multiplier_next_week = 3 # three times more the following week
    second_week_kg = first_week_kg * multiplier_next_week

    # L2
    total_kg = first_week_kg + second_week_kg

    # FA
    answer = total_kg
    return answer