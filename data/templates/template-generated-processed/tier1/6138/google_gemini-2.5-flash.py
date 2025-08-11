def solve():
    """Index: 6138.
    Returns: how much money Heaven's brother spent on highlighters.
    """
    # L1
    sharpeners_bought = 2 # two sharpeners
    sharpener_price = 5 # $5 each
    heaven_sharpeners_cost = sharpeners_bought * sharpener_price

    # L2
    notebooks_bought = 4 # four notebooks
    notebook_price = 5 # $5 each
    heaven_notebooks_cost = notebooks_bought * notebook_price

    # L3
    erasers_bought = 10 # ten erasers
    eraser_price = 4 # $4 each
    brother_erasers_cost = erasers_bought * eraser_price

    # L4
    total_spent_on_known_items = brother_erasers_cost + heaven_notebooks_cost + heaven_sharpeners_cost

    # L5
    total_money_given = 100 # $100 in total
    brother_highlighters_cost = total_money_given - total_spent_on_known_items

    # FA
    answer = brother_highlighters_cost
    return answer