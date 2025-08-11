def solve():
    """Index: 228.
    Returns: the difference between employees who don't drive and those who take public transportation.
    """
    # L1
    total_employees = 200 # A company has 200 employees
    drive_percent = 0.60 # 60% of the employees drive to work
    employees_drive = total_employees * drive_percent

    # L2
    employees_dont_drive = total_employees - employees_drive

    # L3
    public_transport_fraction = 0.50 # half take public transportation
    employees_public_transport = employees_dont_drive * public_transport_fraction

    # L4
    difference_dont_drive_public_transport = employees_dont_drive - employees_public_transport

    # FA
    answer = difference_dont_drive_public_transport
    return answer