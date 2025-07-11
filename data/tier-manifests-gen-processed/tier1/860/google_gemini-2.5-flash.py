def solve():
    """Index: 860.
    Returns: the total amount Greg and Earl will have together in dollars.
    """
    # L1
    earl_initial_money = 90 # Earl has $90
    earl_owes_fred = 28 # Earl owes Fred $28
    earl_after_paying_fred = earl_initial_money - earl_owes_fred

    # L2
    fred_initial_money = 48 # Fred has $48
    fred_after_earl_pays = fred_initial_money + earl_owes_fred

    # L3
    fred_owes_greg = 32 # Fred owes Greg $32
    fred_after_paying_greg = fred_after_earl_pays - fred_owes_greg

    # L4
    greg_initial_money = 36 # Greg has $36
    greg_after_fred_pays = greg_initial_money + fred_owes_greg

    # L5
    greg_owes_earl = 40 # Greg owes Earl $40
    greg_after_paying_earl = greg_after_fred_pays - greg_owes_earl

    # L6
    earl_final_money = earl_after_paying_fred + greg_owes_earl

    # L7
    total_greg_earl = greg_after_paying_earl + earl_final_money

    # FA
    answer = total_greg_earl
    return answer