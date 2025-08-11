def solve():
    """Index: 4754.
    Returns: the total of the numbers they have.
    """
    # L1
    coraline_number = 80 # Coraline's number is 80
    jayden_less_than_coraline = 40 # Jayden's number is 40 less than Coraline's number
    jayden_number = coraline_number - jayden_less_than_coraline

    # L2
    jayden_coraline_total = coraline_number + jayden_number

    # L3
    mickey_greater_than_jayden = 20 # Mickey's number is greater than Jayden's number by exactly 20
    mickey_number = jayden_number + mickey_greater_than_jayden

    # L4
    total_numbers = jayden_coraline_total + mickey_number

    # FA
    answer = total_numbers
    return answer