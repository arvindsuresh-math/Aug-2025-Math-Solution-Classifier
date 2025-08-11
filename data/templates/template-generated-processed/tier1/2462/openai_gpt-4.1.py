def solve():
    """Index: 2462.
    Returns: how many more demerits Andy can get this month before getting fired.
    """
    # L1
    demerits_per_late = 2 # 2 demerits per instance for showing up late
    late_times = 6 # showing up late 6 times
    demerits_late = demerits_per_late * late_times

    # L2
    max_demerits = 50 # can get 50 demerits in a month before getting fired
    demerits_joke = 15 # 15 demerits for making an inappropriate joke
    demerits_remaining = max_demerits - demerits_late - demerits_joke

    # FA
    answer = demerits_remaining
    return answer