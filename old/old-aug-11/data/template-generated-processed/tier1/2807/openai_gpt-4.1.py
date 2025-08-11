def solve():
    """Index: 2807.
    Returns: the number of minutes Osborn must take on Friday to tie his old average.
    """
    # L1
    days_in_week = 5 # school week (Monday to Friday)
    old_average = 3 # 3 minutes on average to get dressed
    total_needed = days_in_week * old_average

    # L2
    monday = 2 # Monday is takes him 2 minutes
    tuesday = 4 # Tuesday it takes him 4 minutes
    wednesday = 3 # Wednesday it takes him 3 minutes
    thursday = 4 # Thursday it takes him 4 minutes
    total_so_far = monday + tuesday + wednesday + thursday

    # L3
    friday_needed = total_needed - total_so_far

    # FA
    answer = friday_needed
    return answer