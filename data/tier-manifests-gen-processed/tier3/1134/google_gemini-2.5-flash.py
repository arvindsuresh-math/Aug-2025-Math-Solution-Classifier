def solve():
    """Index: 1134.
    Returns: the total number of days it will take for them to finish the lollipops.
    """
    # L1
    alison_lollipops = 60 # With 60 lollipops, Alisson has
    henry_more_than_alison = 30 # Henry has 30 more lollipops than Alison
    henry_lollipops = alison_lollipops + henry_more_than_alison

    # L2
    alison_henry_total = henry_lollipops + alison_lollipops

    # L3
    diane_multiplier = 2 # Alison has half the number of lollipops Diane has
    diane_lollipops = diane_multiplier * alison_lollipops

    # L4
    total_lollipops = diane_lollipops + alison_henry_total

    # L5
    lollipops_per_day = 45 # eat 45 lollipops each day
    days_to_finish = total_lollipops / lollipops_per_day

    # FA
    answer = days_to_finish
    return answer