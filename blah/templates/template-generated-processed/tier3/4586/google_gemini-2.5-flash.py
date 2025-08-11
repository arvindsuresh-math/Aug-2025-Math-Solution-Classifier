from fractions import Fraction

def solve():
    """Index: 4586.
    Returns: the total number of valid documents.
    """
    # L1
    total_papers = 400 # 400 A4 pieces of paper
    invalid_percentage = Fraction(40, 100) # 40% of the papers
    invalid_papers = invalid_percentage * total_papers

    # L2
    valid_documents = total_papers - invalid_papers

    # FA
    answer = valid_documents
    return answer