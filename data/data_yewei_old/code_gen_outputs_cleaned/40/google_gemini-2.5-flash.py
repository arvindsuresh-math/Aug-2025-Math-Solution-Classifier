def solve_40():
    # Original cost of one concert ticket
    ticket_cost = 40

    # Number of tickets bought by Mr. Benson
    total_tickets_bought = 12

    # Threshold for discount application
    discount_threshold = 10

    # Discount percentage for tickets exceeding the threshold
    discount_percentage = 0.05

    # L1: Calculate the number of tickets that receive a discount.
    # These are the tickets bought that exceed the discount_threshold.
    num_discounted_tickets = total_tickets_bought - discount_threshold
    # num_discounted_tickets = 12 - 10 = 2

    # L2: Calculate the discount amount per ticket.
    # This is 5% of the original ticket cost.
    discount_amount_per_ticket = ticket_cost * discount_percentage
    # discount_amount_per_ticket = 40 * 0.05 = 2

    # L3: Calculate the cost of a single discounted ticket.
    # This is the original ticket cost minus the discount amount.
    cost_per_discounted_ticket = ticket_cost - discount_amount_per_ticket
    # cost_per_discounted_ticket = 40 - 2 = 38

    # L4: Calculate the total cost for the discounted tickets.
    # This is the number of discounted tickets multiplied by the cost per discounted ticket.
    total_cost_discounted_tickets = num_discounted_tickets * cost_per_discounted_ticket
    # total_cost_discounted_tickets = 2 * 38 = 76

    # L5: Calculate the total cost for the full-price tickets.
    # These are the tickets up to the discount_threshold.
    total_cost_full_price_tickets = discount_threshold * ticket_cost
    # total_cost_full_price_tickets = 10 * 40 = 400

    # L6: Calculate the total amount Mr. Benson paid.
    # This is the sum of the cost of full-price tickets and discounted tickets.
    total_amount_paid = total_cost_full_price_tickets + total_cost_discounted_tickets
    # total_amount_paid = 400 + 76 = 476

    return total_amount_paid