def solve():
    """Index: 6183.
    Returns: the number of hours each trainer will spend training the dolphins.
    """
    # L1
    num_dolphins = 4 # 4 dolphins
    hours_per_dolphin = 3 # 3 hours of training daily
    total_training_hours = num_dolphins * hours_per_dolphin

    # L2
    num_trainers = 2 # 2 trainers
    hours_per_trainer = total_training_hours / num_trainers

    # FA
    answer = hours_per_trainer
    return answer