def solve():
    """Index: 4799.
    Returns: the total amount the school spent.
    """
    # L1
    regular_fee = 150 # regular seminar fee is $150
    discount_percentage_num = 5 # 5% discount
    percent_divisor = 100 # WK
    discount_per_teacher = regular_fee * discount_percentage_num / percent_divisor

    # L2
    fee_per_teacher_after_discount = regular_fee - discount_per_teacher

    # L3
    num_teachers = 10 # registered 10 teachers
    total_seminar_fees = fee_per_teacher_after_discount * num_teachers

    # L4
    food_allowance_per_teacher = 10 # $10 food allowance for each of the teachers
    total_food_allowance = food_allowance_per_teacher * num_teachers

    # L5
    total_spent = total_seminar_fees + total_food_allowance

    # FA
    answer = total_spent
    return answer