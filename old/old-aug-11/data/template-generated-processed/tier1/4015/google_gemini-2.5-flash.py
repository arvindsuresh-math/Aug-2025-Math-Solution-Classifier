def solve():
    """Index: 4015.
    Returns: the total number of emails in Jackson's inbox now.
    """
    # L1
    first_received_emails = 15 # gets another 15 sent to him
    second_received_emails = 5 # receives 5 more emails
    initial_new_emails = first_received_emails + second_received_emails

    # L2
    final_received_emails = 10 # 10 more that were sent to him
    total_new_emails = final_received_emails + initial_new_emails

    # FA
    answer = total_new_emails
    return answer