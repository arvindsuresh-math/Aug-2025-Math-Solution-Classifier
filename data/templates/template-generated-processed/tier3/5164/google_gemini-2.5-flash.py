def solve():
    """Index: 5164.
    Returns: the total number of 20 dollar bills Tye received.
    """
    # L1
    withdrawal_amount_per_bank = 300 # withdraws $300 from each bank
    number_of_banks = 2 # two different banks
    total_withdrawal = withdrawal_amount_per_bank * number_of_banks

    # L2
    bill_denomination = 20 # 20 dollar bills
    number_of_bills = total_withdrawal / bill_denomination

    # FA
    answer = number_of_bills
    return answer