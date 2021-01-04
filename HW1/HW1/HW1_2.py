time = int(input("Введите время в секундах"))
time_hours = time // 3600
time_min = (time - (time_hours * 3600)) // 60
time_sec = time - (time_hours * 3600) - (time_min * 60)
print(f"{time_hours}:{time_min}:{time_sec}")
