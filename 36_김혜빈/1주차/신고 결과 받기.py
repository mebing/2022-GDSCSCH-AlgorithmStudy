# id_list : 이용자의 id 가 담긴 문자열 배열
# report : 각 이용자가 신고한 이용자의 id 정보가 담긴 문자열 배열
# k : 정지 기준이 되는 신고 횟수
# result : 각 유저별로 처리 결과 메일을 받은 횟수

def solution(id_list, report, k):
    n = [[id_list[x]] for x in range(len(id_list))]
    answer = [0] * len(id_list)
    for i in range(len(report)):
        tmp = report[i].split(' ')
        idx = id_list.index(tmp[1])
        if tmp[0] not in n[idx]:
            n[idx].append(tmp[0])
        if (k == len(n[idx])-1):
            for j in range(len(n[idx])-1):
                answer_idx = id_list.index(n[idx][j+1])
                answer[answer_idx] += 1
    return answer

# id_list, report, k = ["muzi", "frodo", "apeach", "neo"],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
id_list, report, k = ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3
result = solution(id_list, report, k)
