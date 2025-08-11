from fractions import Fraction

def solve():
    """Index: 5290.
    Returns: the total number of important emails.
    """
    # L1
    total_emails = 400 # 400 emails
    spam_fraction = Fraction(1, 4) # 1/4 were spam emails
    spam_emails = spam_fraction * total_emails

    # L2
    non_spam_emails = total_emails - spam_emails

    # L3
    promotional_fraction = Fraction(2, 5) # 2/5 of the remaining emails were promotional messages
    promotional_emails = promotional_fraction * non_spam_emails

    # L4
    important_emails = non_spam_emails - promotional_emails

    # FA
    answer = important_emails
    return answer