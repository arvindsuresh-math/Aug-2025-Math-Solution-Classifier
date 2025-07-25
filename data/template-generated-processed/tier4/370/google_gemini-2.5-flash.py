from fractions import Fraction

def solve():
    """Index: 370.
    Returns: the total time to serve dinner to all patients.
    """
    # L1
    total_patients = 12 # 12 patients
    special_diet_fraction = Fraction(1, 3) # one-third of her patients
    special_needs_patients = total_patients * special_diet_fraction

    # L2
    standard_care_patients = total_patients - special_needs_patients

    # L3
    serving_time_standard = 5 # 5 minutes to serve each standard care patient
    special_care_increase_factor = 1.2 # increases the serving time by 20%
    serving_time_special = special_care_increase_factor * serving_time_standard

    # L4
    total_time_standard_care = serving_time_standard * standard_care_patients

    # L5
    total_time_special_care = serving_time_special * special_needs_patients

    # L6
    total_serving_time = total_time_standard_care + total_time_special_care

    # FA
    answer = total_serving_time
    return answer