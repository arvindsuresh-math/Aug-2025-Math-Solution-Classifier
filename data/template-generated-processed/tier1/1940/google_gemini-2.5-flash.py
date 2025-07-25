def solve():
    """Index: 1940.
    Returns: the total number of legs (paws) of the animals for sale.
    """
    # L1
    num_birds = 3 # 3 birds
    legs_per_bird = 2 # WK
    total_bird_paws = num_birds * legs_per_bird

    # L2
    num_dogs = 5 # 5 dogs
    legs_per_dog = 4 # WK
    total_dog_paws = num_dogs * legs_per_dog

    # L4
    # L3 states that a spider has 8 legs, which is used in this sum.
    spider_legs = 8 # WK
    total_paws = total_bird_paws + total_dog_paws + spider_legs

    # FA
    answer = total_paws
    return answer