def solve():
    """Index: 1787.
    Returns: the total time in minutes Kira took to make her breakfast.
    """
    # L1
    sausage_time_per = 5 # it takes 5 minutes to fry each sausage
    num_sausages = 3 # fries 3 sausages
    sausage_total_time = sausage_time_per * num_sausages

    # L2
    egg_time_per = 4 # 4 minutes to scramble each egg
    num_eggs = 6 # scrambles 6 eggs
    egg_total_time = egg_time_per * num_eggs

    # L3
    total_time = sausage_total_time + egg_total_time

    # FA
    answer = total_time
    return answer