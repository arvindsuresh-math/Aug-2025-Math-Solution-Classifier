def solve():
    """Index: 6160.
    Returns: how much money Samantha would have saved by paying cash.
    """
    # L1
    monthly_installment_amount = 300 # 300 each
    num_installments = 30 # 30 equal monthly installments
    total_installments_paid = monthly_installment_amount * num_installments

    # L2
    deposit_amount = 3000 # deposit of $3000
    total_higher_purchase_price = deposit_amount + total_installments_paid

    # L3
    cash_price = 8000 # cash price of a refrigerator was $8000
    money_saved = total_higher_purchase_price - cash_price

    # FA
    answer = money_saved
    return answer