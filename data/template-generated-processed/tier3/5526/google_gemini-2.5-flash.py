def solve():
    """Index: 5526.
    Returns: the total amount Jenny spent on the cat in the first year.
    """
    # L1
    monthly_food_cost = 25 # monthly cost of food was $25
    months_per_year = 12 # WK
    total_food_cost = monthly_food_cost * months_per_year

    # L2
    adoption_fee = 50 # The adoption fee was $50
    vet_cost = 500 # the vet visits cost $500 for the first year
    shared_expenses = total_food_cost + adoption_fee + vet_cost

    # L3
    split_divisor = 2 # split all the costs down the middle
    jenny_shared_expenses = shared_expenses / split_divisor

    # L4
    toys_cost = 200 # She bought $200 in toys
    total_cost_jenny_paid = jenny_shared_expenses + toys_cost

    # FA
    answer = total_cost_jenny_paid
    return answer