def solve():
    """Index: 6541.
    Returns: the total number of people in the park over the two days.
    """
    # L1
    visitors_saturday = 200 # 200 visitors last Saturday
    more_visitors_sunday = 40 # 40 more visitors on Sunday
    visitors_sunday = visitors_saturday + more_visitors_sunday

    # L2
    total_visitors = visitors_sunday + visitors_saturday

    # FA
    answer = total_visitors
    return answer