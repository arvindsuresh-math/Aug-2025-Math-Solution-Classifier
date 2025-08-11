from fractions import Fraction

def solve():
    """Index: 2755.
    Returns: the total amount of money Bowen spends.
    """
    # L1
    pens_bought = 40 # 40 pens
    more_pencils_fraction = Fraction(2, 5) # 2/5 times more pencils than pens
    more_pencils = more_pencils_fraction * pens_bought

    # L2
    initial_pencils_base = 40 # 40 pencils
    total_pencils = initial_pencils_base + more_pencils

    # L3
    pencil_cost_dollars = 0.25 # twenty-five cents
    cost_pencils = total_pencils * pencil_cost_dollars

    # L4
    pen_cost_dollars = 0.15 # fifteen cents
    cost_pens = pen_cost_dollars * pens_bought

    # L5
    total_money_spent = cost_pencils + cost_pens

    # FA
    answer = total_money_spent
    return answer