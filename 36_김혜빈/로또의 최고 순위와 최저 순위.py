def solution(lottos, win_nums):
    answer = []
    count, zero_cnt = 0, 0
    for i in range(len(lottos)):
        if lottos[i] == 0 :
            zero_cnt += 1
        else :
            for j in range(len(win_nums)):
                if win_nums[j] != 0 and win_nums[j] == lottos[i]:
                    count += 1
    high_rank = (len(lottos)+1) - count - zero_cnt
    low_rank = (len(lottos)+1) - count
    if high_rank > 6 :
        high_rank = 6
    if low_rank > 6:
        low_rank = 6
        
    answer.append(high_rank)
    answer.append(low_rank)
                
    return answer

# a1 = [44, 1, 0, 0, 31, 25]
# a2 = [0 for k in range(6)]
a3 = [45, 4, 35, 20, 3, 9]
# b1 = [31, 10, 45, 1, 6, 19]
# b2 = [38, 19, 20, 40, 15, 25]
b3 = [20, 9, 3, 45, 4, 35]


result = solution(a3, b3)
print(result)
