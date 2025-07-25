def solve():
    """Index: 1829.
    Returns: the total amount Harry will pay in silvers.
    """
    # L1
    num_spellbooks = 5 # 5 spellbooks
    cost_per_spellbook_gold = 5 # 5 gold
    total_spellbooks_gold = num_spellbooks * cost_per_spellbook_gold

    # L2
    cost_owl_gold = 28 # 28 gold
    total_gold_books_owl = total_spellbooks_gold + cost_owl_gold

    # L3
    silver_per_gold = 9 # 9 silver to a gold
    total_silver_books_owl = total_gold_books_owl * silver_per_gold

    # L4
    num_potion_kits = 3 # three potion kits
    cost_per_potion_kit_silver = 20 # 20 silver
    total_potion_kits_silver = num_potion_kits * cost_per_potion_kit_silver

    # L5
    total_spending_silver = total_potion_kits_silver + total_silver_books_owl

    # FA
    answer = total_spending_silver
    return answer