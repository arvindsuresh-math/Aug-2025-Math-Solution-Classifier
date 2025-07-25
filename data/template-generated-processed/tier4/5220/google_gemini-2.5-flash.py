def solve():
    """Index: 5220.
    Returns: the total number of towels to wash.
    """
    # L1
    first_hour_guests = 50 # In the first hour, 50 guests enter the gym.
    second_hour_increase_factor = 1.20 # 20% more guests enter than during the first hour.
    second_hour_towels = first_hour_guests * second_hour_increase_factor

    # L2
    third_hour_increase_factor = 1.25 # 25% more guests enter than in the second hour.
    third_hour_towels = second_hour_towels * third_hour_increase_factor

    # L3
    fourth_hour_increase_divisor = 3 # one third more guests enter than in the third hour.
    fourth_hour_increase_amount = third_hour_towels / fourth_hour_increase_divisor

    # L4
    fourth_hour_towels = third_hour_towels + fourth_hour_increase_amount

    # L5
    total_towels_to_wash = first_hour_guests + second_hour_towels + third_hour_towels + fourth_hour_towels

    # FA
    answer = total_towels_to_wash
    return answer