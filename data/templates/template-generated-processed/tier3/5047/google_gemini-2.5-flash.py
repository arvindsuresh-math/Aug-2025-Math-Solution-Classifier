from fractions import Fraction

def solve():
    """Index: 5047.
    Returns: the total number of messages sent in three days.
    """
    # L1
    lucia_messages_day1 = 120 # Lucia, who sent 120 messages
    alina_fewer_messages = 20 # Alina sent 20 fewer messages
    alina_messages_day1 = lucia_messages_day1 - alina_fewer_messages

    # L2
    total_messages_day1 = alina_messages_day1 + lucia_messages_day1

    # L3
    lucia_fraction_day2 = Fraction(1, 3) # Lucia sent 1/3 of the messages she sent the previous day
    lucia_messages_day2 = lucia_fraction_day2 * lucia_messages_day1

    # L4
    alina_multiplier_day2 = 2 # Alina doubled the messages she sent on the first day
    alina_messages_day2 = alina_messages_day1 * alina_multiplier_day2

    # L5
    total_messages_day2 = lucia_messages_day2 + alina_messages_day2

    # L6
    total_messages_day3 = total_messages_day1 # sent the same number of messages on the third day as the first day
    total_messages_three_days = total_messages_day1 + total_messages_day3 + total_messages_day2

    # FA
    answer = total_messages_three_days
    return answer