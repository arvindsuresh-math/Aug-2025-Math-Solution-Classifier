def solve(
    length1: int = 12, # 12 foot
    length2: int = 16, # 16 foot
    height: int = 10, # 10 foot high ceilings
    coats_primer: int = 1, # one coat of primer
    coats_paint: int = 2, # two coats of paint
    paint_rate: int = 40 # paint 40 square feet per hour
):
    """Index: 3518.
    Returns: the number of hours it will take Martha to paint the kitchen.
    """
    #: L1
    area_wall1 = length1 * height

    #: L2
    total_area_wall1 = area_wall1 * 2

    #: L3
    area_wall2 = length2 * height

    #: L4
    total_area_wall2 = area_wall2 * 2

    #: L5
    total_wall_area = total_area_wall1 + total_area_wall2

    #: L6
    total_coats = coats_primer + coats_paint
    total_area_to_paint = total_wall_area * total_coats

    #: L7
    hours_needed = total_area_to_paint / paint_rate

    answer = hours_needed # FINAL ANSWER
    return answer