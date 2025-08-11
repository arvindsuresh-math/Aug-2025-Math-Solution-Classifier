def solve():
    """Index: 6219.
    Returns: the total amount spent on the picnic basket contents.
    """
    # L1
    sandwich_price = 5 # Sandwiches are $5 each
    theo_and_tia = 2 # Theo and Tia
    friends_invited = 2 # two of their friends
    num_people = theo_and_tia + friends_invited
    cost_sandwiches = sandwich_price * num_people

    # L2
    fruit_salad_price = 3 # Fruit salad is $3 each
    cost_fruit_salads = fruit_salad_price * num_people

    # L3
    soda_price = 2 # Sodas are $2 each
    sodas_per_person = 2 # two sodas per person
    cost_sodas = soda_price * num_people * sodas_per_person

    # L4
    snack_bag_price = 4 # The snack bags are $4 each
    num_snack_bags = 3 # 3 bags of snacks
    cost_snacks = snack_bag_price * num_snack_bags

    # L5
    total_cost = cost_sandwiches + cost_fruit_salads + cost_sodas + cost_snacks

    # FA
    answer = total_cost
    return answer