def solve():
    """Index: 4457.
    Returns: the number of cookies left after Jim eats some.
    """
    # L1
    num_flour_bags = 4 # 4 bags of flour
    weight_per_bag = 5 # weighing 5 pounds
    total_flour_pounds = num_flour_bags * weight_per_bag

    # L2
    flour_per_batch = 2 # using 2 pounds of flour
    num_batches = total_flour_pounds / flour_per_batch

    # L3
    cookies_per_dozen = 12 # a dozen cookies
    total_cookies_cooked = num_batches * cookies_per_dozen

    # L4
    cookies_jim_ate = 15 # Jim eats 15 cookies
    cookies_left = total_cookies_cooked - cookies_jim_ate

    # FA
    answer = cookies_left
    return answer