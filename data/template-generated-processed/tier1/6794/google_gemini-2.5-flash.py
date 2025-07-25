def solve():
    """Index: 6794.
    Returns: the total cost of their breakfast.
    """
    # L1
    muffin_cost = 2 # Muffins cost $2 each
    francis_muffins_count = 2 # Francis had 2 muffins
    francis_muffin_cost = francis_muffins_count * muffin_cost

    # L2
    fruit_cup_cost = 3 # fruit cups cost $3 each
    francis_fruit_cups_count = 2 # Francis had 2 fruit cups
    francis_fruit_cup_cost = francis_fruit_cups_count * fruit_cup_cost

    # L3
    kiera_muffins_count = 2 # Kiera had 2 muffins
    kiera_muffin_cost = kiera_muffins_count * muffin_cost

    # L4
    kiera_fruit_cups_count = 1 # Kiera had 1 fruit cup
    kiera_fruit_cup_cost = kiera_fruit_cups_count * fruit_cup_cost

    # L5
    total_cost = francis_muffin_cost + francis_fruit_cup_cost + kiera_muffin_cost + kiera_fruit_cup_cost

    # FA
    answer = total_cost
    return answer