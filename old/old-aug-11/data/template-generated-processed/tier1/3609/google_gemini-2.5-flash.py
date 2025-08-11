def solve():
    """Index: 3609.
    Returns: the total number of students the buses can accommodate.
    """
    # L1
    rows_per_bus = 10 # 10 rows of seats
    columns_per_bus = 4 # 4 columns
    students_per_bus = rows_per_bus * columns_per_bus

    # L2
    num_buses = 6 # 6 buses
    total_students = students_per_bus * num_buses

    # FA
    answer = total_students
    return answer