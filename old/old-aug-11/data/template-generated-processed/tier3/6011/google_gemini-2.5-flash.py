def solve():
    """Index: 6011.
    Returns: the number of sweet treats each student will receive.
    """
    # L1
    cookies = 20 # 20 cookies
    cupcakes = 25 # 25 cupcakes
    brownies = 35 # 35 brownies
    total_sweet_treats = cookies + cupcakes + brownies

    # L2
    num_students = 20 # class of 20 students
    treats_per_student = total_sweet_treats / num_students

    # FA
    answer = treats_per_student
    return answer