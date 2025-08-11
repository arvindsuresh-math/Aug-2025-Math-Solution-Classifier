def solve():
    """Index: 3536.
    Returns: the number of more glasses Tina sold than Katya.
    """
    # L1
    katya_sales = 8 # Katya sold 8 glasses of lemonade
    ricky_sales = 9 # Ricky sold 9 glasses of lemonade
    combined_sales = katya_sales + ricky_sales

    # L2
    multiplier_for_tina = 2 # twice as many as Katya and Ricky's combined sales
    tina_sales = combined_sales * multiplier_for_tina

    # L3
    tina_more_than_katya = tina_sales - katya_sales

    # FA
    answer = tina_more_than_katya
    return answer