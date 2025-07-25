def solve():
    """Index: 7450.
    Returns: the total number of marshmallows needed.
    """
    # L1
    total_campers = 96 # 96 campers
    girls_fraction_denominator = 3 # one-third of the campers are girls
    num_girls = total_campers / girls_fraction_denominator

    # L2
    num_boys = num_girls + num_girls

    # L3
    girls_marshmallow_percent_num = 75 # 75% of the girls want to toast marshmallows
    percent_factor = 0.01 # WK
    girls_marshmallow_toasters = num_girls * girls_marshmallow_percent_num * percent_factor

    # L4
    boys_marshmallow_percent_num = 50 # 50% of the boys want to toast marshmallows
    boys_marshmallow_toasters = num_boys * boys_marshmallow_percent_num * percent_factor

    # L5
    total_marshmallows_needed = girls_marshmallow_toasters + boys_marshmallow_toasters

    # FA
    answer = total_marshmallows_needed
    return answer