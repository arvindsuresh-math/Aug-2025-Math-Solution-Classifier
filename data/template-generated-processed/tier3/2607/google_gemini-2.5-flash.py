def solve():
    """Index: 2607.
    Returns: the total profit John made.
    """
    # L1
    initial_puppies = 8 # litter of 8 puppies
    given_away_divisor = 2 # gives away half of them
    puppies_after_giving_away = initial_puppies / given_away_divisor

    # L2
    kept_puppies = 1 # He keeps one of the remaining puppies
    puppies_to_sell = puppies_after_giving_away - kept_puppies

    # L3
    sale_price_per_puppy = 600 # sells them each for $600
    money_from_sales = puppies_to_sell * sale_price_per_puppy

    # L4
    stud_fee = 300 # give the owner of the stud $300
    profit = money_from_sales - stud_fee

    # FA
    answer = profit
    return answer