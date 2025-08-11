def solve():
    """Index: 3201.
    Returns: the total number of cookies baked by the church members.
    """
    # L1
    sheets_per_member = 10 # each member baked 10 sheets
    cookies_per_sheet = 16 # each sheet has 16 cookies
    cookies_per_member = sheets_per_member * cookies_per_sheet

    # L2
    num_members = 100 # 100 members
    total_cookies = cookies_per_member * num_members

    # FA
    answer = total_cookies
    return answer