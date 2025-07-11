def solve():
    """Index: 2645.
    Returns: the total amount of money Rebecca will have at the end of the day in dollars.
    """
    # L1
    haircut_price = 30 # charges $30 for haircuts
    num_haircuts = 4 # four haircuts scheduled
    haircut_income = haircut_price * num_haircuts

    # L2
    dye_job_price = 60 # charges $60 for dye jobs
    num_dye_jobs = 2 # two dye jobs scheduled
    dye_job_income = dye_job_price * num_dye_jobs

    # L3
    hair_dye_cost_per_box = 10 # buy a box of hair dye for $10
    hair_dye_boxes_needed = num_dye_jobs # one box per dye job
    hair_dye_total_cost = hair_dye_cost_per_box * hair_dye_boxes_needed

    # L4
    perm_price = 40 # charges $40 for perms
    num_perms = 1 # one perm scheduled
    perm_income = perm_price * num_perms
    tips = 50 # makes $50 in tips
    total_money = haircut_income + dye_job_income + perm_income - hair_dye_total_cost + tips

    # FA
    answer = total_money
    return answer