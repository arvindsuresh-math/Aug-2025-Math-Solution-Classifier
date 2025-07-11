def solve():
    """Index: 860.
    Returns: the total amount Greg and Earl have together after all debts are paid.
    """
    # L1
    earl_initial = 90 # Earl has $90
    earl_owes_fred = 28 # Earl owes Fred $28
    earl_after_paying_fred = earl_initial - earl_owes_fred

    # L2
    fred_initial = 48 # Fred has $48
    fred_after_receiving_from_earl = fred_initial + earl_owes_fred

    # L3
    fred_owes_greg = 32 # Fred owes Greg $32
    fred_after_paying_greg = fred_after_receiving_from_earl - fred_owes_greg

    # L4
    greg_initial = 36 # Greg has $36
    greg_after_receiving_from_fred = greg_initial + fred_owes_greg

    # L5
    greg_owes_earl = 40 # Greg owes Earl $40
    greg_after_paying_earl = greg_after_receiving_from_fred - greg_owes_earl

    # L6
    earl_after_receiving_from_greg = earl_after_paying_fred + greg_owes_earl

    # L7
    total_greg_and_earl = greg_after_paying_earl + earl_after_receiving_from_greg

    # FA
    answer = total_greg_and_earl
    return answer