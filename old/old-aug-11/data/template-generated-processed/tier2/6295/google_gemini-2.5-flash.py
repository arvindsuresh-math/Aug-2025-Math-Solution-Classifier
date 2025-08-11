def solve():
    """Index: 6295.
    Returns: the total amount earned including bonuses.
    """
    # L1
    recipe_card_cost_per_card = 0.70 # 70 cents for each recipe card
    num_cards_transcribed = 200 # transcribes 200 cards
    earnings_from_cards = recipe_card_cost_per_card * num_cards_transcribed

    # L2
    bonus_amount_per_unit = 10 # 10 dollar bonus
    cards_per_bonus_unit = 100 # transcribes 100 cards
    num_bonus_units = num_cards_transcribed / cards_per_bonus_unit
    total_bonus = bonus_amount_per_unit * num_bonus_units

    # L3
    total_earnings = earnings_from_cards + total_bonus

    # FA
    answer = total_earnings
    return answer