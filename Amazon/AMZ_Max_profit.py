'''
https://leetcode.com/discuss/interview-question/1532572/amazon-oa-max-profit
'''


def max_profit(k: int, profit: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(profit)//2
    sum = 0
    for i in range(k):
        sum += profit[i] + profit[i+n]
    max_sum = sum
    for i in range(1, n):
        sum = sum + profit[(i+k-1)%n] - profit[i-1] + profit[(i+k-1)%n+n] - profit[i+n-1]
        if sum > max_sum:
            max_sum = sum
    return max_sum

print(max_profit(2, [1,3,5,8,9,-5,4,-2]))