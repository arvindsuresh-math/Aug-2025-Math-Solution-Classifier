def solve():
    """Index: 3776.
    Returns: the total money Julia spent on food for her animals.
    """
    # L1
    total_weekly_cost = 30 # food for both of the animals for $30 in total a week
    rabbit_food_weekly_cost = 12 # the weekly cost of the rabbit food is $12
    parrot_food_weekly_cost = total_weekly_cost - rabbit_food_weekly_cost

    # L2
    parrot_weeks = 3 # the parrot for 3 weeks
    spent_on_parrot = parrot_weeks * parrot_food_weekly_cost

    # L3
    rabbit_weeks = 5 # the rabbit for 5 weeks
    spent_on_rabbit = rabbit_weeks * rabbit_food_weekly_cost

    # L4
    total_spent = spent_on_parrot + spent_on_rabbit

    # FA
    answer = total_spent
    return answer