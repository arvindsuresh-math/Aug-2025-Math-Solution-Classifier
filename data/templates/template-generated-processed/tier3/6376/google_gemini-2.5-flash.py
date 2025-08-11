def solve():
    """Index: 6376.
    Returns: the amount of money made if a different number of people attended.
    """
    # L1
    total_school_people = 400 # the school had 400 people
    half_divisor = 2 # Half the school attended
    people_in_attendance = total_school_people / half_divisor

    # L2
    total_collected_money = 2000 # collects $2000
    cost_per_person = total_collected_money / people_in_attendance

    # L3
    hypothetical_attendees = 300 # if 300 people attended
    hypothetical_earnings = hypothetical_attendees * cost_per_person

    # FA
    answer = hypothetical_earnings
    return answer