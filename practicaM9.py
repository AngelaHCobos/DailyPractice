N = [(1, 100, 2, "single", 32), (2, 1000, 2, "single", 30), (3, 10000, 3, "single", 40), (4, 1000000, 2, "single", 39, 5, 12, 1, "divorced", 34)]

def person(N):
    maxi_salary1 = 0
    maxi_salary2 = 0
    maxi_salary3 = 0
    id1 = 0
    id2 = 0
    id3 = 0
    for p in N:
        conditions = [
            p[3] == "single",
            p[2] >= 1,
            p[2] <= 3,
            p[4] >= 30,
            p[4] <= 40
        ]
        if all(conditions):
            net_salary = (p[1] - p[1] * 0.15) - ((p[1] - p[1] * 0.15) * max([0, 0.04 - p[2] * 0.01]))
            if net_salary > maxi_salary1:
                maxi_salary3 = maxi_salary2
                maxi_salary2 = maxi_salary1
                maxi_salary1 = net_salary
                id3 = id2
                id2 = id1
                id1 = p[0]
            elif net_salary > maxi_salary2:
                maxi_salary3 = maxi_salary2
                maxi_salary2 = net_salary
                id3 = id2
                id2 = p[0]
            elif net_salary > maxi_salary3:
                maxi_salary3 = net_salary
                id3 = p[0]
    return id3

print(person(N))