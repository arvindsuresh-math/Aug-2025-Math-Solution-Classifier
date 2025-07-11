def solve():
    """Index: 1190.
    Returns: Harry's age.
    """
    # L1
    kiarra_age = 30 # If Kiarra is 30
    kiarra_bea_multiplier = 2 # Kiarra is twice as old as Bea
    bea_age = kiarra_age / kiarra_bea_multiplier

    # L2
    job_bea_multiplier = 3 # Job is 3 times older than Bea
    job_age = bea_age * job_bea_multiplier

    # L3
    figaro_job_difference = 7 # Figaro is 7 years older than Job
    figaro_age = job_age + figaro_job_difference

    # L4
    harry_figaro_divisor = 2 # Harry is half as old as Figaro
    harry_age = figaro_age / harry_figaro_divisor

    # FA
    answer = harry_age
    return answer