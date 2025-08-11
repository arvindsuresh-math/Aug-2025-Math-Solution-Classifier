def solve():
    """Index: 4884.
    Returns: the amount James has to pay for the puppy.
    """
    # L1
    adoption_fee = 200 # The adoption fee is $200
    friend_pay_percent = 0.25 # friend agrees to pay 25% of that
    friend_payment_amount = adoption_fee * friend_pay_percent

    # L2
    james_payment_amount = adoption_fee - friend_payment_amount

    # FA
    answer = james_payment_amount
    return answer