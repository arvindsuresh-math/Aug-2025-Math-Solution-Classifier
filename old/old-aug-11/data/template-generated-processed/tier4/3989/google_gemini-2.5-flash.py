from fractions import Fraction

def solve():
    """Index: 3989.
    Returns: the total number of students in the class.
    """
    # L1
    total_gift_card_value = 50 # If she got $50 in gift cards
    gift_card_value_per_card = 10 # a gift card for $10
    num_gift_cards = total_gift_card_value / gift_card_value_per_card

    # L2
    fraction_with_gift_card = Fraction(1, 3) # 1/3 of these contained a gift card
    num_thank_you_cards = num_gift_cards / fraction_with_gift_card

    # L3
    class_thank_you_percent = 0.3 # 30% of her class
    total_students = num_thank_you_cards / class_thank_you_percent

    # FA
    answer = total_students
    return answer