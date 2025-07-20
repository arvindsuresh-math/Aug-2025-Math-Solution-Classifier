def solve():
    """Index: 6399.
    Returns: the total amount Emmalyn earned from painting the fences.
    """
    # L1
    num_fences = 50 # 50 fences
    length_per_fence = 500 # each fence was 500 meters long
    total_length = num_fences * length_per_fence

    # L2
    charge_per_meter = 0.20 # twenty cents per meter
    total_income = charge_per_meter * total_length

    # FA
    answer = total_income
    return answer