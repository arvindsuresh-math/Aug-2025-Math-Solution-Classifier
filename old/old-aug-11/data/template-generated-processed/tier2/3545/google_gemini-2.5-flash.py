def solve():
    """Index: 3545.
    Returns: the total cost to feed Belle treats for a week.
    """
    # L1
    rawhide_bone_cost_per_unit = 1 # each rawhide bone is $1
    rawhide_bones_per_evening = 2 # 2 rawhide bones every evening
    days_per_week = 7 # WK
    weekly_rawhide_cost = rawhide_bone_cost_per_unit * rawhide_bones_per_evening * days_per_week

    # L2
    dog_biscuit_cost_per_unit = 0.25 # each dog biscuit is $0.25
    dog_biscuits_per_evening = 4 # 4 dog biscuits every evening
    weekly_biscuit_cost = dog_biscuit_cost_per_unit * dog_biscuits_per_evening * days_per_week

    # L3
    total_weekly_cost = weekly_rawhide_cost + weekly_biscuit_cost

    # FA
    answer = total_weekly_cost
    return answer