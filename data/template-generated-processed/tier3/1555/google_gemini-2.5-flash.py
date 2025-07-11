def solve():
    """Index: 1555.
    Returns: the number of stickers each student will receive.
    """
    # L1
    gold_stickers = 50 # 50 gold stickers
    silver_multiplier = 2 # twice as many silver stickers
    silver_stickers = gold_stickers * silver_multiplier

    # L2
    bronze_fewer = 20 # 20 fewer bronze stickers
    bronze_stickers = silver_stickers - bronze_fewer

    # L3
    total_stickers = gold_stickers + silver_stickers + bronze_stickers

    # L4
    num_students = 5 # each of her 5 students
    stickers_per_student = total_stickers / num_students

    # FA
    answer = stickers_per_student
    return answer