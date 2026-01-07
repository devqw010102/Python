import math

def develop(progresses, speeds) :
    answer = []
    days = []

    for progress, speed in zip(progresses, speeds) :
        count = math.ceil((100 - progress) / speed)
        days.append(count)

    if not days : return []
    max_day = days[0]
    count = 0

    for day in days :
        if day <= max_day :
            count += 1
        else :
            answer.append(count)
            max_day = day
            count = 1

    answer.append(count)
    return answer


print(develop([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))