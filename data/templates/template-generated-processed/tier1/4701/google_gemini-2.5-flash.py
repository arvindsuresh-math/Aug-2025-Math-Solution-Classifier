def solve():
    """Index: 4701.
    Returns: the total cost Kath will pay for admission.
    """
    # L1
    admission_cost_regular = 8 # admission costs $8
    discount_early_bird = 3 # price is $3 less
    early_bird_cost = admission_cost_regular - discount_early_bird

    # L2
    kath_count = 1 # herself
    siblings_count = 2 # 2 siblings
    friends_count = 3 # 3 of her friends
    total_people = kath_count + siblings_count + friends_count

    # L3
    total_admission_cost = early_bird_cost * total_people

    # FA
    answer = total_admission_cost
    return answer