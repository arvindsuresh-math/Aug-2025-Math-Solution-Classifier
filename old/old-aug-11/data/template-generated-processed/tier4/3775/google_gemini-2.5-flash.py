def solve():
    """Index: 3775.
    Returns: the reward Greg's PPO algorithm obtained.
    """
    # L1
    procgen_max_reward = 240 # ProcGen reward of 240
    coinrun_max_reward_divisor = 2 # half as much
    coinrun_max_reward = procgen_max_reward / coinrun_max_reward_divisor

    # L2
    ppo_reward_percent = 0.9 # 90% of the possible reward
    greg_ppo_reward = coinrun_max_reward * ppo_reward_percent

    # FA
    answer = greg_ppo_reward
    return answer