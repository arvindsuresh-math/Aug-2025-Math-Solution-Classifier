def solve(
    wall1_length: int = 12, # 12 foot by 16 foot kitchen (first wall length)
    wall2_length: int = 16, # 12 foot by 16 foot kitchen (second wall length)
    wall_height: int = 10, # 10 foot high ceilings
    coats_primer: int = 1, # Each wall needs one coat of primer
    coats_paint: int = 2, # and two coats of paint
    painting_rate: int = 40 # Martha can paint 40 square feet per hour
):
    """Index: 3518.
    Returns: the number of hours needed to paint all coats on all four walls.
    """
    #: L1
    wall1_area = wall1_length * wall_height

    #: L2
    total_wall1_area = wall1_area * 2

    #: L3
    wall2_area = wall2_length * wall_height

    #: L4
    total_wall2_area = wall2_area * 2

    #: L5
    total_wall_area = total_wall1_area + total_wall2_area

    #: L6
    total_coats = coats_primer + coats_paint
    total_area_to_paint = total_wall_area * total_coats

    #: L7
    hours_needed = total_area_to_paint / painting_rate

    answer = hours_needed # FINAL ANSWER
    return answer