def solve():
    """Index: 2600.
    Returns: how much more money Emir needs to buy all three books.
    """
    # L1
    dictionary_cost = 5 # dictionary that costs $5
    dinosaur_book_cost = 11 # dinosaur book that costs $11
    cookbook_cost = 5 # children's cookbook that costs $5
    total_cost = dictionary_cost + dinosaur_book_cost + cookbook_cost

    # L2
    saved_money = 19 # saved $19 from his allowance
    money_needed = total_cost - saved_money

    # FA
    answer = money_needed
    return answer