def solve():
    """Index: 6944.
    Returns: the total amount of money raised by the business.
    """
    # L1
    num_tickets = 25 # 25 raffle tickets
    ticket_price = 2.00 # $2.00 apiece
    ticket_sales_revenue = num_tickets * ticket_price

    # L2
    num_donations_15 = 2 # 2 $15 donations
    donation_amount_15 = 15 # $15 donations
    donations_15_total = num_donations_15 * donation_amount_15

    # L3
    donation_amount_20 = 20 # a $20 donation
    total_money_raised = ticket_sales_revenue + donations_15_total + donation_amount_20

    # FA
    answer = total_money_raised
    return answer