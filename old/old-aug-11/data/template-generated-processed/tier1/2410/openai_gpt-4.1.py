def solve():
    """Index: 2410.
    Returns: Freddy's age.
    """
    # L1
    job_age = 5 # Job is 5
    stephanie_multiplier = 4 # Stephanie is 4 times as old as Job
    stephanie_age = job_age * stephanie_multiplier

    # L2
    freddy_younger = 2 # Freddy is 2 years younger than Stephanie
    freddy_age = stephanie_age - freddy_younger

    # FA
    answer = freddy_age
    return answer