def solve():
    """Index: 3014.
    Returns: the net amount Travis should be paid.
    """
    # L1
    lost_bowls = 12 # 12 bowls are lost
    broken_bowls = 15 # 15 bowls are broken
    total_lost_broken_bowls = lost_bowls + broken_bowls

    # L2
    cost_per_lost_broken_bowl = 4 # $4 each for any bowls that are lost or broken
    payment_for_lost_broken = total_lost_broken_bowls * cost_per_lost_broken_bowl

    # L3
    total_bowls_to_take = 638 # 638 bowls from the factory
    safely_delivered_bowls = total_bowls_to_take - total_lost_broken_bowls

    # L4
    payment_per_safe_bowl = 3 # $3 for every bowl that is delivered safely
    payment_for_safe_delivery = safely_delivered_bowls * payment_per_safe_bowl

    # L5
    initial_fee = 100 # a $100 fee
    total_gross_payment = payment_for_safe_delivery + initial_fee

    # L6
    net_payment = total_gross_payment - payment_for_lost_broken

    # FA
    answer = net_payment
    return answer