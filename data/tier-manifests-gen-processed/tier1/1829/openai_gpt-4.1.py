def solve():
    """Index: 1829.
    Returns: the total amount Harry will pay, in silvers.
    """
    # L1
    num_spellbooks = 5 # 5 spellbooks
    price_per_spellbook_gold = 5 # each cost 5 gold
    spellbooks_total_gold = num_spellbooks * price_per_spellbook_gold

    # L2
    owl_price_gold = 28 # one owl that costs 28 gold
    books_and_owl_gold = spellbooks_total_gold + owl_price_gold

    # L3
    silver_per_gold = 9 # There are 9 silver to a gold
    books_and_owl_silver = books_and_owl_gold * silver_per_gold

    # L4
    num_potion_kits = 3 # three potion kits
    price_per_potion_kit_silver = 20 # each cost 20 silver
    potion_kits_total_silver = num_potion_kits * price_per_potion_kit_silver

    # L5
    total_silver = potion_kits_total_silver + books_and_owl_silver

    # FA
    answer = total_silver
    return answer