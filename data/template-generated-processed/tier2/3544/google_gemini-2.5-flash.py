def solve():
    """Index: 3544.
    Returns: the number of employees who use public transportation.
    """
    # L1
    total_employees = 100 # 100 employees
    drive_percent = 0.60 # 60% of the employees drive to work
    employees_drive = total_employees * drive_percent

    # L2
    employees_dont_drive = total_employees - employees_drive

    # L3
    public_transport_fraction = 0.50 # half take public transportation
    employees_public_transport = employees_dont_drive * public_transport_fraction

    # FA
    answer = employees_public_transport
    return answer