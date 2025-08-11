def solve():
    """Index: 4233.
    Returns: the total cost of potatoes.
    """
    # L1
    pounds_per_person = 1.5 # Each person eats 1.5 pounds of potatoes
    num_people = 40 # makes potatoes for 40 people
    total_pounds_needed = pounds_per_person * num_people

    # L2
    pounds_per_bag = 20 # A 20-pound bag of potatoes
    num_bags_needed = total_pounds_needed / pounds_per_bag

    # L3
    cost_per_bag = 5 # bag of potatoes costs $5
    total_cost = num_bags_needed * cost_per_bag

    # FA
    answer = total_cost
    return answer