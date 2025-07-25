def solve():
    """Index: 1810.
    Returns: the total number of amoxicillin capsules sold every 2 weeks.
    """
    # L1
    earned_100mg_weekly = 80 # earned a total of $80 from 100 mg amoxicillin
    cost_100mg_capsule = 5 # each capsule of 100 mg amoxicillin costs $5
    capsules_100mg_weekly = earned_100mg_weekly / cost_100mg_capsule

    # L2
    weeks_period = 2 # every 2 weeks
    capsules_100mg_biweekly = capsules_100mg_weekly * weeks_period

    # L3
    earned_500mg_weekly = 60 # $60 from 500 mg amoxicillin
    cost_500mg_capsule = 2 # each capsule of 500 mg amoxicillin costs $2
    capsules_500mg_weekly = earned_500mg_weekly / cost_500mg_capsule

    # L4
    capsules_500mg_biweekly = capsules_500mg_weekly * weeks_period

    # L5
    total_capsules_biweekly = capsules_500mg_biweekly + capsules_100mg_biweekly

    # FA
    answer = total_capsules_biweekly
    return answer