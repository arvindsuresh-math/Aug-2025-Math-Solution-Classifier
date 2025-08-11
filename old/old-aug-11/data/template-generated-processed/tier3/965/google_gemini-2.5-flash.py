def solve():
    """Index: 965.
    Returns: the amount each person needs to contribute to the bill.
    """
    # L1
    total_price = 67 # total price of the meal comes to $67
    coupon_value = 4 # coupon for $4
    price_after_coupon = total_price - coupon_value

    # L2
    number_of_people = 3 # Sarah, Mary, and Tuan decided to go to the restaurant
    contribution_per_person = price_after_coupon / number_of_people

    # FA
    answer = contribution_per_person
    return answer