def solve():
    """Index: 760.
    Returns: the total amount of money Susan will spend on food.
    """
    # L1
    num_guests = 30 # 30 guests
    servings_per_batch = 2 # recipe makes 2 servings each
    num_batches = num_guests / servings_per_batch

    # L2
    potatoes_per_batch = 4 # each batch calls for 4 potatoes
    total_potatoes = num_batches * potatoes_per_batch

    # L3
    salt_teaspoons_per_batch = 1 # each batch calls for 1 teaspoon of salt
    total_teaspoons_salt = salt_teaspoons_per_batch * num_batches

    # L4
    teaspoons_per_container = 5 # each container of salt has 5 teaspoons
    num_salt_containers = total_teaspoons_salt / teaspoons_per_container

    # L5
    potato_cost = 0.10 # a potato costs $.10
    salt_container_cost = 2 # a container of salt costs $2
    total_potato_cost = total_potatoes * potato_cost
    total_salt_cost = num_salt_containers * salt_container_cost

    # L6
    total_food_cost = total_potato_cost + total_salt_cost

    # FA
    answer = total_food_cost
    return answer