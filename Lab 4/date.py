from datetime import datetime, timedelta

today = datetime.now()

print("Exercise 1")
print(today - timedelta(days=5))

print()

print("Exercise 2")
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

print()

print("Exercise 3")
print(today.replace(microsecond=0))

print()

print("Exercise 4")
date1 = datetime(2026, 10, 5, 10, 0, 0)
date2 = datetime(2026, 10, 5, 12, 0, 0)

difference = date2 - date1
print(difference.total_seconds())