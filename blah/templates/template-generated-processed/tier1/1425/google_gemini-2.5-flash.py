def solve():
    """Index: 1425.
    Returns: the difference between the number of cupcakes Betty and Dora made.
    """
    # L1
    dora_rate = 8 # Dora makes 8 every hour
    total_hours = 5 # after 5 hours
    dora_total_cupcakes = dora_rate * total_hours

    # L2
    betty_break_hours = 2 # Betty took a two-hour break
    betty_working_hours = total_hours - betty_break_hours

    # L3
    betty_rate = 10 # Betty makes 10 cupcakes every hour
    betty_total_cupcakes = betty_rate * betty_working_hours

    # L4
    difference_cupcakes = dora_total_cupcakes - betty_total_cupcakes

    # FA
    answer = difference_cupcakes
    return answer