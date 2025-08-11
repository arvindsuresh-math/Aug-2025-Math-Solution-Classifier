def solve():
    """Index: 7361.
    Returns: the total number of patients John treats in a year.
    """
    # L1
    patients_first_hospital = 20 # sees 20 different patients each day
    extra_patients_percent = 0.2 # sees 20% more individual patients
    extra_patients = patients_first_hospital * extra_patients_percent

    # L2
    patients_second_hospital = patients_first_hospital + extra_patients

    # L3
    total_patients_per_day = patients_first_hospital + patients_second_hospital

    # L4
    work_days_per_week = 5 # He works 5 days a week
    total_patients_per_week = total_patients_per_day * work_days_per_week

    # L5
    work_weeks_per_year = 50 # he works 50 weeks a year
    total_patients_per_year = total_patients_per_week * work_weeks_per_year

    # FA
    answer = total_patients_per_year
    return answer