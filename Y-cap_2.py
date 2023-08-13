n = int(input())
hh, mm, ss = map(int, input().split(":"))
days = 1

for i in range(n - 1):
    hh1, mm1, ss1 = map(int, input().split(":"))

    if (hh1 < hh) or (hh1 == hh) and (mm1 < mm) or \
            (hh1 == hh) and (mm1 == mm) and (ss1 <= ss):
        days += 1

    hh = hh1
    mm = mm1
    ss = ss1
print(days)
