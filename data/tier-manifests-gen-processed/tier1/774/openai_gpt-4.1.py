def solve():
    """Index: 774.
    Returns: the most money the plumber can earn from one of the three jobs.
    """
    # L1
    toilets_job1 = 3 # fixing three toilets (job 1)
    sinks_job1 = 3 # three sinks (job 1)
    toilet_price = 50 # charges $50 to fix a toilet
    sink_price = 30 # charges $30 to fix a sink
    job1_earnings = toilets_job1 * toilet_price + sinks_job1 * sink_price

    # L2
    toilets_job2 = 2 # two toilets (job 2)
    sinks_job2 = 5 # five sinks (job 2)
    job2_earnings = toilets_job2 * toilet_price + sinks_job2 * sink_price

    # L3
    toilets_job3 = 1 # one toilet (job 3)
    showers_job3 = 2 # two showers (job 3)
    sinks_job3 = 3 # three sinks (job 3)
    shower_price = 40 # charges $40 to fix a shower
    job3_earnings = toilets_job3 * toilet_price + showers_job3 * shower_price + sinks_job3 * sink_price

    # L4
    most_money = max(job1_earnings, job2_earnings, job3_earnings)

    # FA
    answer = most_money
    return answer