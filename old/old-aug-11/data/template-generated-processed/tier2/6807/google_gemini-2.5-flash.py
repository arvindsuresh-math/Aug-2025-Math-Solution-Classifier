def solve():
    """Index: 6807.
    Returns: the total cost for the firm to produce three batches of yogurt.
    """
    # L1
    fruit_quantity_per_batch = 3 # 3 kilograms of fruit
    fruit_cost_per_kg = 2 # fruit at $2 per kilogram
    fruit_cost_per_batch = fruit_quantity_per_batch * fruit_cost_per_kg

    # L2
    milk_quantity_per_batch = 10 # 10 liters of milk
    milk_cost_per_liter = 1.5 # Milk is bought at $1.5 per liter
    milk_cost_per_batch = milk_quantity_per_batch * milk_cost_per_liter

    # L3
    total_cost_per_batch = milk_cost_per_batch + fruit_cost_per_batch

    # L4
    num_batches = 3 # three batches of yogurt
    total_cost_three_batches = num_batches * total_cost_per_batch

    # FA
    answer = total_cost_three_batches
    return answer