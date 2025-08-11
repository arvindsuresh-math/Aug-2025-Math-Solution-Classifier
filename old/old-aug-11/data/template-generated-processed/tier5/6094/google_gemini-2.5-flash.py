def solve():
    """Index: 6094.
    Returns: the number of minutes Walter spent looking at the seals.
    """
    # L1
    hours_at_zoo = 2 # 2 hours
    minutes_per_hour = 60 # WK
    minutes_from_hours = hours_at_zoo * minutes_per_hour

    # L2
    extra_minutes_at_zoo = 10 # 10 minutes
    total_minutes_at_zoo = minutes_from_hours + extra_minutes_at_zoo

    # L3-L7 (Implicit calculations for algebraic steps)
    penguin_time_multiplier = 8 # eight times as long looking at the penguins
    elephant_time = 13 # 13 minutes looking at the elephants
    seal_time_coefficient = 1 # implicit coefficient for 's'

    # From s + 8s + 13 = 130
    # Combine like terms: 9s + 13 = 130
    combined_s_coefficient = seal_time_coefficient + penguin_time_multiplier

    # Subtract 13 from both sides: 9s = 130 - 13
    remaining_time_for_s = total_minutes_at_zoo - elephant_time

    # Divide by 9: s = (130 - 13) / 9
    seals_minutes = remaining_time_for_s / combined_s_coefficient

    # FA
    answer = seals_minutes
    return answer