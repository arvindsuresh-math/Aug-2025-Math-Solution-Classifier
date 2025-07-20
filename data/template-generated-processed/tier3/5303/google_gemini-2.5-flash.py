from fractions import Fraction

def solve():
    """Index: 5303.
    Returns: the total time the car traveled that day.
    """
    # L1
    percentage_ningi_to_zipra = Fraction(80, 100) # 80% of the time
    time_ngapara_to_zipra = 60 # 60 hours to travel from Ngapara to Zipra
    time_ningi_to_zipra = percentage_ningi_to_zipra * time_ngapara_to_zipra

    # L2
    total_travel_time = time_ningi_to_zipra + time_ngapara_to_zipra

    # FA
    answer = total_travel_time
    return answer