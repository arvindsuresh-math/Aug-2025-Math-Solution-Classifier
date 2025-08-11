def solve():
    """Index: 2645.
    Returns: the total money Rebecca will have at the end of the day.
    """
    # L1
    haircut_charge = 30 # charges $30 for haircuts
    num_haircuts = 4 # four haircuts scheduled
    income_from_haircuts = haircut_charge * num_haircuts

    # L2
    dye_job_charge = 60 # charges $60 for dye jobs
    num_dye_jobs = 2 # two dye jobs scheduled
    income_from_dye_jobs = dye_job_charge * num_dye_jobs

    # L3
    hair_dye_cost = 10 # buy a box of hair dye for $10
    cost_of_hair_dye = hair_dye_cost * num_dye_jobs

    # L4
    perm_charge = 40 # $40 for perms
    tips = 50 # makes $50 in tips
    total_money = income_from_haircuts + income_from_dye_jobs + perm_charge - cost_of_hair_dye + tips

    # FA
    answer = total_money
    return answer