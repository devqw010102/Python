from collections import Counter

def participant_completion(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(participant_completion(["leo", "kiki", "eden"], ["eden", "kiki"]))
