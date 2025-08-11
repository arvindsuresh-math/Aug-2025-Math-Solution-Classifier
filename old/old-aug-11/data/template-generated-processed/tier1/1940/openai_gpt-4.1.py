def solve():
    """Index: 1940.
    Returns: the total number of legs for all animals in the pet shop.
    """
    # L1
    num_birds = 3 # 3 birds
    legs_per_bird = 2 # 2 legs each (birds)
    bird_legs = num_birds * legs_per_bird

    # L2
    num_dogs = 5 # 5 dogs
    legs_per_dog = 4 # 4 legs each (dogs)
    dog_legs = num_dogs * legs_per_dog

    # L3
    num_spiders = 1 # 1 spider
    legs_per_spider = 8 # 8 legs (spider)
    spider_legs = num_spiders * legs_per_spider

    # L4
    total_legs = bird_legs + dog_legs + spider_legs

    # FA
    answer = total_legs
    return answer