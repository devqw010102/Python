from collections import deque

def process(priorities, location):

    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while queue :
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue) :
            queue.append(current)
        else :
            answer += 1
            if current[1] == location :
                return answer
    return None


print(process([1, 1, 9, 1, 1, 1], 0))