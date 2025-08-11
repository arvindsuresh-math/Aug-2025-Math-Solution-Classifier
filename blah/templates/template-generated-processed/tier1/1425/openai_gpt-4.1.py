def solve():
    """Index: 1425.
    Returns: the difference between the number of cupcakes Dora and Betty made after 5 hours.
    """
    # L1
    dora_rate = 8 # Dora makes 8 every hour
    total_hours = 5 # after 5 hours
    dora_total = dora_rate * total_hours

    # L2
    betty_break = 2 # Betty took a two-hour break
    betty_hours = total_hours - betty_break

    # L3
    betty_rate = 10 # Betty makes 10 cupcakes every hour
    betty_total = betty_rate * betty_hours

    # L4
    difference = dora_total - betty_total

    # FA
    answer = difference
    return answer