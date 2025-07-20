def solve():
    """Index: 6772.
    Returns: the total number of people in the group.
    """
    # L1
    total_spent = 94 # spent a total of $94
    spent_on_pineapple = 54 # $54 was spent on pineapple juice
    spent_on_mango = total_spent - spent_on_pineapple

    # L2
    cost_mango_juice = 5 # mango juice, which sells for $5 a glass
    num_people_mango = spent_on_mango / cost_mango_juice

    # L3
    cost_pineapple_juice = 6 # pineapple juice, at $6 a glass
    num_people_pineapple = spent_on_pineapple / cost_pineapple_juice

    # L4
    total_people = num_people_mango + num_people_pineapple

    # FA
    answer = total_people
    return answer