# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# Time Complexity : O(n^2) 
# 정확성: 40.2
# 효율성: 0.0

"""
* Author    : SHIM SOMIN
* Date      : 2024.10.01 (Tues)
* Runtime   : 시간 초과
* Memory    : 실패
* Algorithm : 문자열 선형 탐색
 """

def solution(food_times, k):
    idx = list(range(0, len(food_times)))
    min_time = min(food_times)

    while k >= len(idx):
        if max(food_times) == 0: return -1
        for i in idx:
            food_times[i] = (food_times[i] - min_time)

        k -= min_time * len(idx)

        idx = [i for i in idx if food_times[i] != 0]

    while k >= 0:
        if max(food_times) == 0: return -1

        for i in idx:
            if food_times[i] == 0:
                continue
            elif k == 0: 
                return i+1
            else:
                food_times[i] -= 1
                k -= 1