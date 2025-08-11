def solve():
    """Index: 1787.
    Returns: the total time, in minutes, Kira took to make her breakfast.
    """
    # L1
    time_per_sausage = 5 # 5 minutes to fry each sausage
    num_sausages = 3 # fries 3 sausages
    sausage_cooking_time = time_per_sausage * num_sausages

    # L2
    time_per_egg = 4 # 4 minutes to scramble each egg
    num_eggs = 6 # scrambles 6 eggs
    egg_cooking_time = time_per_egg * num_eggs

    # L3
    total_cooking_time = sausage_cooking_time + egg_cooking_time

    # FA
    answer = total_cooking_time
    return answer