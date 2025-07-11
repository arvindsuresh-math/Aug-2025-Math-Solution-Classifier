def solve():
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """
    # L1
    hamburger_price = 3 # $3 each hamburger
    hamburger_qty = 5 # 5 pieces of hamburger
    hamburger_total = hamburger_price * hamburger_qty

    # L2
    fries_price = 1.20 # $1.20 per set of French fries
    fries_qty = 4 # 4 sets of French fries
    fries_total = fries_price * fries_qty

    # L3
    soda_price = 0.5 # $0.5 per cup of soda
    soda_qty = 5 # 5 cups of soda
    soda_total = soda_price * soda_qty

    # L4
    spaghetti_price = 2.7 # $2.7 per platter of spaghetti
    spaghetti_qty = 1 # 1 platter of spaghetti
    spaghetti_total = spaghetti_price * spaghetti_qty
    total_bill = hamburger_total + fries_total + soda_total + spaghetti_total

    # L5
    num_friends = 5 # Five friends
    per_person = total_bill / num_friends

    # FA
    answer = per_person
    return answer