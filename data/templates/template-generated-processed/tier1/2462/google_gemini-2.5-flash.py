def solve():
    """Index: 2462.
    Returns: the number of additional demerits Andy can get before being fired.
    """
    # L1
    demerits_per_late_instance = 2 # 2 demerits per instance
    late_instances = 6 # 6 times
    demerits_from_late = demerits_per_late_instance * late_instances

    # L2
    max_demerits = 50 # 50 demerits in a month before getting fired
    demerits_from_joke = 15 # 15 demerits for making an inappropriate joke
    remaining_demerits = max_demerits - demerits_from_late - demerits_from_joke

    # FA
    answer = remaining_demerits
    return answer