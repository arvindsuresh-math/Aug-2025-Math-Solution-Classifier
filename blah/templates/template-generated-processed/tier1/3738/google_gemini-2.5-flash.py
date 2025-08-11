def solve():
    """Index: 3738.
    Returns: the total amount of money Julieta spent at the store.
    """
    # L1
    initial_backpack_cost = 50 # backpack was $50
    backpack_increase = 5 # increased by $5
    new_backpack_cost = initial_backpack_cost + backpack_increase

    # L2
    initial_binder_cost = 20 # each ring-binder cost was $20
    binder_reduction = 2 # reduced by $2
    new_binder_cost = initial_binder_cost - binder_reduction

    # L3
    num_ring_binders = 3 # three ring-binders
    total_binder_cost = new_binder_cost * num_ring_binders

    # L4
    total_spent = new_backpack_cost + total_binder_cost

    # FA
    answer = total_spent
    return answer