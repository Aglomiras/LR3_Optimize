import numpy as np
import matplotlib.pyplot as plt

capacity = 12500
initCharge = 2700
priceSchedule = [12, 1.4, 1.5, 1.6, 1.7, 1.8,
                 2, 3, 4, 5, 5, 4.5,
                 3, 3, 2.7, 3.2, 4.5, 5,
                 7, 9, 10, 12, 8, 3]
loadSchedule = [480, 320, 320, 360, 360, 360,
                420, 920, 1200, 720, 680, 720,
                800, 820, 960, 1200, 1380, 1380,
                1520, 1800, 1920, 1920, 1640, 1020]
constantLoad = 150
targetCharge = 700
maxCharge = 4000
minCharge = 1000

accrc = 10
num = 12

def calc(schs):
    res = 1000
    t = 0
    for i in schs:
        res = res - i * priceSchedule[t]
        t += 1
    return res

print(calc([]))
# + зарядка
# - выпуск

def main():
    pr_res = []
    pr_res.append({initCharge: []})
    res = {}
    for i in range(0, num):
        res.clear()
        for j in pr_res[i].keys():
            curr_charge = j
            curr_qq = pr_res[i][j]
            curr_money = calc(pr_res[i][j])
            #print(curr_charge)
            for k in range(-maxCharge, -minCharge+1, +accrc):
                #print(float(j)+k)
                #print(curr_money)
                if (curr_charge + (k-loadSchedule[i] - constantLoad) >= 0) and (curr_money - k * priceSchedule[i] >= 0) and (curr_charge + (k-loadSchedule[i] - constantLoad) <= capacity):
                    if (res.get(curr_charge + k - loadSchedule[i] - constantLoad) != None):
                        if (curr_money - k * priceSchedule[i] > calc(res.get(curr_charge + k - loadSchedule[i] - constantLoad))):
                            res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                            for qq in curr_qq:
                                res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                            res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))
                    else:
                        res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                        for qq in curr_qq:
                            res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                        res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))

            k = 0
            if (curr_charge + (k - loadSchedule[i] - constantLoad) >= 0) and (
                    curr_money - k * priceSchedule[i] >= 0) and (
                    curr_charge + (k - loadSchedule[i] - constantLoad) <= capacity):
                if (res.get(curr_charge + k - loadSchedule[i] - constantLoad) != None):
                    if (curr_money - k * priceSchedule[i] > calc(
                            res.get(curr_charge + k - loadSchedule[i] - constantLoad))):
                        res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                        for qq in curr_qq:
                            res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                        res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))
                else:
                    res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                    for qq in curr_qq:
                        res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                    res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))

            for k in range(+minCharge, +maxCharge+1, +accrc):
                #print(float(j)+k)
                #print(curr_money)
                if (curr_charge + (k - loadSchedule[i] - constantLoad) >= 0) and (
                        curr_money - k * priceSchedule[i] >= 0) and (
                        curr_charge + (k - loadSchedule[i] - constantLoad) <= capacity):
                    if (res.get(curr_charge + k - loadSchedule[i] - constantLoad) != None):
                        if (curr_money - k * priceSchedule[i] > calc(
                                res.get(curr_charge + k - loadSchedule[i] - constantLoad))):
                            res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                            for qq in curr_qq:
                                res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                            res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))
                    else:
                        res[curr_charge + k - loadSchedule[i] - constantLoad] = []
                        for qq in curr_qq:
                            res[curr_charge + k - loadSchedule[i] - constantLoad].append(qq)
                        res[curr_charge + k - loadSchedule[i] - constantLoad].append(int(k))

        pr_res.append({})
        for j in res.keys():
            pr_res[i+1][j] = res[j]
        print(pr_res)
    max = []
    print(pr_res[num])
    for i in pr_res[num].keys():
        if calc(pr_res[num][i]) > calc(max):
            max = pr_res[num][i]
    print(max)
    print(calc(max))

    plt.figure()
    plt.title('Заряд')
    y = [initCharge]
    for i in range(len(max)):
        y.append(y[i] + max[i] - loadSchedule[i] - constantLoad)
    plt.plot(y, 'tab:red')
    plt.grid()
    plt.show()
    return max

def main2():
    pr_res = []
    pr_res.append({initCharge: []})
    res = {}
    for i in range(0, num):
        res.clear()
        for j in pr_res[i].keys():
            curr_charge = j
            curr_qq = pr_res[i][j]
            curr_money = calc(pr_res[i][j])
            #print(curr_charge)
            for k in range(-maxCharge, -minCharge+1, +accrc):
                #print(float(j)+k)
                #print(curr_money)
                if (curr_charge + k >= targetCharge) and (curr_money - k * priceSchedule[i] >= 0) and (curr_charge + k <= capacity):
                    if (res.get(curr_charge + k) != None):
                        if curr_money - k * priceSchedule[i] > calc(res.get(curr_charge + k)):
                            res[curr_charge + k] = []
                            for qq in curr_qq:
                                res[curr_charge + k].append(qq)
                            res[curr_charge + k].append(int(k))
                    else:
                        res[curr_charge + k] = []
                        for qq in curr_qq:
                            res[curr_charge + k].append(qq)
                        res[curr_charge + k].append(int(k))

            k = 0
            if (curr_charge + k >= targetCharge) and (curr_money - k * priceSchedule[i] >= 0) and (
                    curr_charge + k <= capacity):
                if (res.get(curr_charge + k) != None):
                    if curr_money - k * priceSchedule[i] > calc(res.get(curr_charge + k)):
                        res[curr_charge + k] = []
                        for qq in curr_qq:
                            res[curr_charge + k].append(qq)
                        res[curr_charge + k].append(int(k))
                else:
                    res[curr_charge + k] = []
                    for qq in curr_qq:
                        res[curr_charge + k].append(qq)
                    res[curr_charge + k].append(int(k))

            for k in range(+minCharge, +maxCharge+1, +accrc):
                #print(float(j)+k)
                #print(curr_money)
                if (curr_charge + k >= targetCharge) and (curr_money - k * priceSchedule[i] >= 0) and (
                        curr_charge + k <= capacity):
                    if (res.get(curr_charge + k) != None):
                        if curr_money - k * priceSchedule[i] > calc(res.get(curr_charge + k)):
                            res[curr_charge + k] = []
                            for qq in curr_qq:
                                res[curr_charge + k].append(qq)
                            res[curr_charge + k].append(int(k))
                    else:
                        res[curr_charge + k] = []
                        for qq in curr_qq:
                            res[curr_charge + k].append(qq)
                        res[curr_charge + k].append(int(k))

        pr_res.append({})
        for j in res.keys():
            pr_res[i+1][j] = res[j]
        print(pr_res)
    max = []
    print(pr_res[num])
    for i in pr_res[num].keys():
        if calc(pr_res[num][i]) > calc(max):
            max = pr_res[num][i]
    print(max)
    print(calc(max))

    plt.figure()
    plt.title('Заряд')
    y = [initCharge]
    for i in range(len(max)):
        y.append(y[i] + max[i])
    plt.plot(y, 'tab:red')
    plt.grid()
    plt.show()
    return max

def visual():
    plt.figure()
    plt.title('Заряд')
    y = [initCharge]
    for i in range(num):
        y.append(y[i] - loadSchedule[i] - constantLoad)
    plt.plot(y, 'tab:red')
    plt.grid()
    plt.show()
    return 0

result = main()
