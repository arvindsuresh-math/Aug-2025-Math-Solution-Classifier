def solve():
    """Index: 4464.
    Returns: the profit made from the movie.
    """
    # L1
    cost_per_person_food = 3 # $3 worth of food
    num_people = 50 # 50 people there
    food_cost = cost_per_person_food * num_people

    # L2
    actor_cost = 1200 # cost $1200
    cost_without_equipment = actor_cost + food_cost

    # L3
    equipment_multiplier = 2 # twice as much as food and actors combined
    equipment_rental_cost = cost_without_equipment * equipment_multiplier

    # L4
    total_cost = equipment_rental_cost + cost_without_equipment

    # L5
    movie_sold_price = 10000 # sold the movie for $10,000
    profit = movie_sold_price - total_cost

    # FA
    answer = profit
    return answer