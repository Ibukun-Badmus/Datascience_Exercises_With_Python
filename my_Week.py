my_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "'Thursday", "Friday", "Saturday"]


def modify_week(weeks):
    weeks.append(weeks.pop(0))
    return weeks


print(modify_week(my_week))

tasks = ["Java", "Sleep", "Python", "Data Science", "Catch Cruise", "Flex"]

print(dict(zip(my_week, tasks)))
