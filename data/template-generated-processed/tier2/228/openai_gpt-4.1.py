def solve():
    """Index: 228.
    Returns: how many more employees drive to work than take public transportation.
    """
    # L1
    total_employees = 200 # 200 employees
    drive_percent = 0.60 # 60% of the employees drive to work
    drive_count = total_employees * drive_percent

    # L2
    dont_drive_count = total_employees - drive_count

    # L3
    public_transport_percent = 0.50 # half take public transportation
    public_transport_count = dont_drive_count * public_transport_percent

    # L4
    difference = drive_count - public_transport_count

    # FA
    answer = difference
    return answer