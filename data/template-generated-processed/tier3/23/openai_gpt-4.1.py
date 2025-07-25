def solve():
    """Index: 23.
    Returns: the cost of each top Ann bought.
    """
    # L1
    shorts_count = 5 # 5 pairs of shorts
    shorts_price = 7 # $7 each
    shorts_total = shorts_count * shorts_price

    # L2
    shoes_count = 2 # 2 pairs of shoes
    shoes_price = 10 # $10 each
    shoes_total = shoes_count * shoes_price

    # L3
    shorts_and_shoes_total = shorts_total + shoes_total

    # L4
    total_spent = 75 # $75 she bought
    difference = total_spent - shorts_and_shoes_total

    # L5
    tops_count = 4 # 4 tops
    top_price = difference / tops_count

    # FA
    answer = top_price
    return answer