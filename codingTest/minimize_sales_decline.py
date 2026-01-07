import sys

adj = []
dp = []
sales_list = []


def dfs(u):
    dp[u][0] = 0
    dp[u][1] = sales_list[u - 1]

    # 팀원만 있는 경우
    if not adj[u]:
        return

    total_sum = 0
    is_any_child_attended = False
    min_diff = float('inf')

    for v in adj[u]:
        dfs(v)
        # 팀원이 참석하는게 싼지, 안하는게 싼지 결정
        if dp[v][0] < dp[v][1]:
            total_sum += dp[v][0]
        else:
            total_sum += dp[v][1]
            is_any_child_attended = True  # 한 명이라도 참석함

        # 강제로 보낼 경우를 대비해 '참석-미참석' 비용 차이의 최소값 보관
        min_diff = min(min_diff, dp[v][1] - dp[v][0])

    # 팀장 참석 시: 팀원들은 자유롭게 선택
    dp[u][1] += total_sum

    # 팀장 미참석 시:
    if is_any_child_attended:
        dp[u][0] = total_sum
    else:
        # 아무도 안 갔다면 가장 손해 적은 팀원 한 명을 강제로 보냄
        dp[u][0] = total_sum + min_diff


def solution(sales, links):
    global adj, dp, sales_list
    n = len(sales)
    sales_list = sales
    adj = [[] for _ in range(n + 1)]
    dp = [[0, 0] for _ in range(n + 1)]

    for p, c in links:
        adj[p].append(c)

    dfs(1)  # 루트 노드인 1번부터 시작
    return min(dp[1][0], dp[1][1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))



# https://school.programmers.co.kr/learn/courses/30/lessons/72416
# Programmers
# 2021 KAKAO BLIND RECRUITMENT 매출 하락 최소화
# https://github.com/devqw010102/Python/issues/8