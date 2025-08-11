def solve():
    """Index: 4262.
    Returns: the total distance traveled during the horseback riding trip.
    """
    # L1
    first_day_speed = 5 # traveled at 5 miles per hour
    first_day_hours = 7 # for 7 hours
    first_day_distance = first_day_speed * first_day_hours

    # L2
    second_day_part1_speed = 6 # traveled at 6 miles per hour
    second_day_part1_hours = 6 # for 6 hours
    second_day_part1_distance = second_day_part1_speed * second_day_part1_hours

    # L3
    half_speed_divisor = 2 # half that speed
    second_day_part2_hours = 3 # for another three hours
    second_day_part2_distance = (second_day_part1_speed / half_speed_divisor) * second_day_part2_hours

    # L4
    third_day_hours = 5 # traveled for 5 hours
    third_day_speed = 7 # at 7 miles per hour
    third_day_distance = third_day_hours * third_day_speed

    # L5
    total_distance = first_day_distance + second_day_part1_distance + second_day_part2_distance + third_day_distance

    # FA
    answer = total_distance
    return answer