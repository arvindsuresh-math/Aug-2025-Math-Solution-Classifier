def solve():
    """Index: 1856.
    Returns: the total number of watermelon slices at the picnic.
    """
    # L1
    danny_watermelons = 3 # Danny brings 3 watermelons
    danny_slices_per_watermelon = 10 # cuts each watermelon into 10 slices
    danny_total_slices = danny_watermelons * danny_slices_per_watermelon

    # L2
    sister_watermelons = 1 # His sister brings 1 watermelon
    sister_slices_per_watermelon = 15 # she cuts the watermelon into 15 slices
    sister_total_slices = sister_watermelons * sister_slices_per_watermelon

    # L3
    total_slices_at_picnic = danny_total_slices + sister_total_slices

    # FA
    answer = total_slices_at_picnic
    return answer