def solve_78():
    # Number of cookie pies Manny had
    num_cookie_pies = 3
    # Number of slices per cookie pie
    slices_per_pie = 10
    # Number of classmates
    num_classmates = 24
    # Number of teachers (Mr. Keith)
    num_teacher = 1
    # Manny also had one piece
    manny_ate_slice = 1

    # Calculate the total number of cookie slices
    total_slices = num_cookie_pies * slices_per_pie

    # Calculate the total number of people who ate a slice
    total_people_eating = num_classmates + num_teacher + manny_ate_slice

    # Calculate the number of slices eaten (each person had 1 piece)
    slices_eaten = total_people_eating * 1

    # Calculate the number of slices left
    slices_left = total_slices - slices_eaten

    return slices_left

# Execute the function to get the answer
# print(solve_78())