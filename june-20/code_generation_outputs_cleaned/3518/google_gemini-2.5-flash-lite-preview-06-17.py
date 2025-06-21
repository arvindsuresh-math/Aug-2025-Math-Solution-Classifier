def solve(
    wall_width1: int = 12, # kitchen, which has 12 foot by 16 foot
    wall_width2: int = 16, # kitchen, which has 12 foot by 16 foot
    ceiling_height: int = 10, # 10 foot high ceilings
    coats_of_primer: int = 1, # one coat of primer
    coats_of_paint: int = 2, # two coats of paint
    paint_rate: int = 40 # Martha can paint 40 square feet per hour
):
    """Index: 3518.
    Returns: the total number of hours it will take Martha to paint the kitchen.
    """
    #: L1
    area_wall1 = wall_width1 * ceiling_height

    #: L2
    total_area_wall1 = area_wall1 * 2

    #: L3
    area_wall2 = wall_width2 * ceiling_height

    #: L4
    total_area_wall2 = area_wall2 * 2

    #: L5
    total_area_walls = total_area_wall1 + total_area_wall2

    #: L6
    total_coats = coats_of_primer + coats_of_paint
    total_square_footage_to_paint = total_area_walls * total_coats

    #: L7
    total_hours = total_square_footage_to_paint / paint_rate

    answer = total_hours # FINAL ANSWER
    return answer