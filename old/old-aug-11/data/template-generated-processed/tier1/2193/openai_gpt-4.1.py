def solve():
    """Index: 2193.
    Returns: the total amount of money Niles collects from all members.
    """
    # L1
    hardcover_price = 30 # $30 each for six hardcover books
    num_hardcover = 6 # six hardcover books
    hardcover_total = hardcover_price * num_hardcover

    # L2
    paperback_price = 12 # $12 each for six paperback books
    num_paperback = 6 # six paperback books
    paperback_total = paperback_price * num_paperback

    # L3
    annual_fee = 150 # $150/year towards snacks
    total_per_member = hardcover_total + paperback_total + annual_fee

    # L4
    num_members = 6 # six members
    total_collected = total_per_member * num_members

    # FA
    answer = total_collected
    return answer