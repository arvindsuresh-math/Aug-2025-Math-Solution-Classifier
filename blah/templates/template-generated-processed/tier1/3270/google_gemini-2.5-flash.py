def solve():
    """Index: 3270.
    Returns: the total amount Granger paid for groceries.
    """
    # L1
    spam_price_per_can = 3 # Spam is $3 per can
    num_spam_cans = 12 # bought 12 cans of spam
    cost_spam = spam_price_per_can * num_spam_cans

    # L2
    pb_price_per_jar = 5 # peanut butter is $5 per jar
    num_pb_jars = 3 # 3 jars of peanut butter
    cost_peanut_butter = pb_price_per_jar * num_pb_jars

    # L3
    bread_price_per_loaf = 2 # bread is $2 per loaf
    num_bread_loaves = 4 # 4 loaves of bread
    cost_bread = bread_price_per_loaf * num_bread_loaves

    # L4
    total_amount_paid = cost_spam + cost_peanut_butter + cost_bread

    # FA
    answer = total_amount_paid
    return answer