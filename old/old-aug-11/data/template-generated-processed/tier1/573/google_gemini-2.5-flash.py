def solve():
    """Index: 573.
    Returns: how much more Bert earned than Tory.
    """
    # L1
    bert_phones_sold = 8 # 8 toy phones
    bert_price_per_phone = 18 # $18 each
    bert_earnings = bert_phones_sold * bert_price_per_phone

    # L2
    tory_guns_sold = 7 # 7 toy guns
    tory_price_per_gun = 20 # $20 each
    tory_earnings = tory_guns_sold * tory_price_per_gun

    # L3
    difference_in_earnings = bert_earnings - tory_earnings

    # FA
    answer = difference_in_earnings
    return answer