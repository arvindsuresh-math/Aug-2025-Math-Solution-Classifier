def solve():
    """Index: 5820.
    Returns: the number of bonnets Mrs. Young sent to each orphanage.
    """
    # L1
    bonnets_monday = 10 # On Monday, she made 10 bonnets
    twice_factor = 2 # twice more than on Monday
    bonnets_tuesday_wednesday = bonnets_monday * twice_factor

    # L2
    additional_thursday = 5 # on Thursday she made 5 more than on Monday
    bonnets_thursday = bonnets_monday + additional_thursday

    # L3
    less_friday = 5 # on Friday she made 5 less than on Thursday
    bonnets_friday = bonnets_thursday - less_friday

    # L4
    total_bonnets = bonnets_monday + bonnets_tuesday_wednesday + bonnets_thursday + bonnets_friday

    # L5
    num_orphanages = 5 # sent them to 5 orphanages
    bonnets_per_orphanage = total_bonnets / num_orphanages

    # FA
    answer = bonnets_per_orphanage
    return answer