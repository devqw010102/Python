def ponketmon(nums) :
    answer = len(set(nums)) if len(nums) // 2 > len(set(nums)) else len(nums) // 2

    return answer

print(ponketmon([3,3,3,2,2,2]))