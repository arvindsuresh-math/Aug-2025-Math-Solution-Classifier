def solve():
    """Index: 5415.
    Returns: the number of contacts equal to $1 worth in the chosen box.
    """
    # L1
    contacts_box_a = 50 # 50 contacts
    cost_box_a = 25 # $25
    contacts_per_dollar_a = contacts_box_a / cost_box_a

    # L2
    contacts_box_b = 99 # 99 contacts
    cost_box_b = 33 # $33
    contacts_per_dollar_b = contacts_box_b / cost_box_b

    # FA
    answer = contacts_per_dollar_b
    return answer