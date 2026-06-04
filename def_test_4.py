def convert_minutes(number_of_episodes, duration_per_episodes):
    total_minutes = number_of_episodes * duration_per_episodes
    remaining_minutes = total_minutes % 60
    total_hours = (total_minutes - remaining_minutes) // 60
    return remaining_minutes, total_hours
number_of_episodes = 6
duration_per_episodes = 24
print("minutes and hours")
print(convert_minutes(number_of_episodes, duration_per_episodes))