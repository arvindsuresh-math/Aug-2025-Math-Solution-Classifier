def solve(
        length_kitchen_1: int = 12, # 12 foot
        width_kitchen: int = 16, # 16 foot
        ceiling_height: int = 10, # 10 foot high ceilings
        coats_primer: int = 1, # one coat of primer
        coats_paint: int = 2, # two coats of paint
        paint_rate: int = 40 # 40 square feet per hour
    ):
    """Index: 3518.
    Returns: the total number of hours Martha needs to paint the kitchen.
    """
    #: L1
    wall_1_area = length_kitchen_1 * ceiling_height

    #: L2
    total_wall_1_area = wall_1_area * 2

    #: L3
    wall_2_area = width_kitchen * ceiling_height

    #: L4
    total_wall_2_area = wall_2_area * 2

    #: L5
    total_surface_area = total_wall_1_area + total_wall_2_area

    #: L6
    total_coats = coats_primer + coats_paint
    total_paint_area = total_surface_area * total_coats

    #: L7
    hours_needed = total_paint_area / paint_rate

    answer = hours_needed # FINAL ANSWER
    return answer