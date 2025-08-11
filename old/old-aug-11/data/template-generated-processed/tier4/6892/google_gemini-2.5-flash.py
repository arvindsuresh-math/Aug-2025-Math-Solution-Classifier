def solve():
    """Index: 6892.
    Returns: the number of solving linear equations problems Sadie has to solve.
    """
    # L1
    total_problems = 140 # 140 math homework problems for the week
    algebra_percent = 0.40 # 40 percent are Algebra problems
    algebra_problems = total_problems * algebra_percent

    # L2
    linear_equation_divisor = 2 # half of the Algebra problems
    linear_equation_problems = algebra_problems / linear_equation_divisor

    # FA
    answer = linear_equation_problems
    return answer