def isExpectedToPassExam(N, P, q, pc, pw):
    expected_total = 0
    for c in range(N):
        probability_win = 1 / q[c]
        probability_lose = 1 - probability_win
        expected_score = probability_win * pc[c] - probability_lose * pw[c]
        if expected_score > 0:
            expected_total += expected_score
    if expected_total >= P:
        return "YES"
    return "NO" 

print(isExpectedToPassExam(2, 1, [2, 2], [2, 2], [1, 1]))    
print(isExpectedToPassExam(3, 2, [2, 4, 2], [1, 4, 1], [0.5, 1, 1])) 
