def solve():
    """Index: 5449.
    Returns: the number of pieces of junk mail each of the red and white mailbox houses will get.
    """
    # L1
    total_junk_mail = 48 # 48 pieces of junk mail
    total_houses = 8 # 8 houses on the block
    pieces_per_house = total_junk_mail / total_houses

    # L2
    num_white_mailboxes = 2 # 2 of the houses have white mailboxes
    junk_mail_white_mailboxes = num_white_mailboxes * pieces_per_house

    # L3
    num_red_mailboxes = 3 # 3 have red mailboxes
    junk_mail_red_mailboxes = num_red_mailboxes * pieces_per_house

    # L4
    total_junk_mail_red_white = junk_mail_white_mailboxes + junk_mail_red_mailboxes

    # L5
    num_red_white_mailboxes = num_white_mailboxes + num_red_mailboxes # 2 of the houses have white mailboxes and 3 have red mailboxes
    pieces_per_red_white_house = total_junk_mail_red_white / num_red_white_mailboxes

    # FA
    answer = pieces_per_red_white_house
    return answer