def solve():
    """Index: 248.
    Returns: how many dollars cheaper the promotional subscription is than the normal one.
    """
    # L1
    issues_per_month = 2 # twice-a-month issue
    subscription_months = 18 # 18-month magazine subscription
    total_issues = issues_per_month * subscription_months

    # L2
    discount_per_issue = 0.25 # $0.25 off each
    total_discount = total_issues * discount_per_issue

    # FA
    answer = total_discount
    return answer