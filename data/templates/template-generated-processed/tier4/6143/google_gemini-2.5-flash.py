def solve():
    """Index: 6143.
    Returns: the number of emails left in the inbox.
    """
    # L1
    initial_emails = 400 # 400 new emails
    trash_divisor = 2 # half of them
    emails_moved_to_trash = initial_emails / trash_divisor

    # L2
    emails_after_trash = initial_emails - emails_moved_to_trash

    # L3
    work_folder_percent = 0.40 # 40 percent of the remaining emails
    emails_moved_to_work = emails_after_trash * work_folder_percent

    # L4
    emails_left_in_inbox = emails_after_trash - emails_moved_to_work

    # FA
    answer = emails_left_in_inbox
    return answer