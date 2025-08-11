def solve():
    """Index: 6025.
    Returns: the number of friends they will give pens to.
    """
    # L1
    kendra_packs = 4 # Kendra has 4 packs of pens
    pens_per_pack = 3 # 3 pens in each pack
    kendra_pens = kendra_packs * pens_per_pack

    # L2
    tony_packs = 2 # Tony has 2 packs of pens
    tony_pens = tony_packs * pens_per_pack

    # L3
    total_pens = kendra_pens + tony_pens

    # L4
    pens_to_keep_each = 2 # keep two pens each
    num_people = 2 # WK
    total_pens_kept = num_people * pens_to_keep_each

    # L5
    friends_to_give_pens = total_pens - total_pens_kept

    # FA
    answer = friends_to_give_pens
    return answer