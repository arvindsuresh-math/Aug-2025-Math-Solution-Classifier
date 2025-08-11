def solve():
    """Index: 573.
    Returns: how much more Bert earned than Tory.
    """
    # L1
    bert_phones_sold = 8 # Bert was able to sell 8 toy phones
    bert_phone_price = 18 # for $18 each
    bert_earnings = bert_phones_sold * bert_phone_price

    # L2
    tory_guns_sold = 7 # Tory was able to sell 7 toy guns
    tory_gun_price = 20 # for $20 each
    tory_earnings = tory_guns_sold * tory_gun_price

    # L3
    bert_more_than_tory = bert_earnings - tory_earnings

    # FA
    answer = bert_more_than_tory
    return answer