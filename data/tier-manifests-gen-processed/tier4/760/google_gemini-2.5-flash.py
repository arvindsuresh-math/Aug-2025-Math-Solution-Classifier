def solve():
    """Index: 760.
    Returns: the total money Susan will spend on food.
    """
    # L1
    num_guests = 30 # 30 guests
    servings_per_batch = 2 # makes 2 servings each
    num_batches = num_guests / servings_per_batch

    # L2
    potatoes_per_batch = 4 # calls for 4 potatoes
    total_potatoes_needed = num_batches * potatoes_per_batch

    # L3
    teaspoons_salt_per_batch = 1 # 1 teaspoon of salt
    total_teaspoons_salt_needed = teaspoons_salt_per_batch * num_batches

    # L4
    teaspoons_per_container = 5 # each container of salt has 5 teaspoons
    num_salt_containers = total_teaspoons_salt_needed / teaspoons_per_container

    # L5
    cost_per_potato_value = 0.1 # A potato costs $.10
    cost_per_potato_display = 1 # For template display of $.1
    cost_per_salt_container = 2 # a container of salt costs $2
    cost_potatoes = total_potatoes_needed * cost_per_potato_value
    cost_salt = num_salt_containers * cost_per_salt_container

    # L6
    total_food_cost = cost_potatoes + cost_salt

    # FA
    answer = total_food_cost
    return answer