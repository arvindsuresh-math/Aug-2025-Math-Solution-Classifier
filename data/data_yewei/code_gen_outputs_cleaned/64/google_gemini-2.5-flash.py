def solve_64():
    # Main job details
    main_job_hourly_rate = 20  # dollars per hour
    main_job_hours = 30  # hours per week

    # Second job details
    less_percentage_second_job = 0.20  # 20% less than main job rate

    # L1: Calculate how much less James earns per hour at his second job
    # James earns 20*.2=$[[20*.2=4]]4 less while working his second job
    hourly_rate_reduction_second_job = main_job_hourly_rate * less_percentage_second_job
    
    # L2: Calculate the hourly rate for the second job
    # So he earns 20-4=$[[20-4=16]]16 an hour
    second_job_hourly_rate = main_job_hourly_rate - hourly_rate_reduction_second_job

    # L3: Calculate earnings from the main job
    # At his first job he earns 20*30=$[[20*30=600]]600
    main_job_earnings = main_job_hourly_rate * main_job_hours

    # L4: Calculate hours worked at the second job
    # He works 30/2=[[30/2=15]]15 hours at his second job
    second_job_hours = main_job_hours / 2

    # L5: Calculate earnings from the second job
    # So he earns 15*16=$[[15*16=240]]240
    second_job_earnings = second_job_hours * second_job_hourly_rate

    # L6: Calculate total weekly earnings
    # So he earns 600+240=$[[600+240=840]]840 a week
    total_weekly_earnings = main_job_earnings + second_job_earnings
    
    return total_weekly_earnings