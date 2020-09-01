import numpy as np
from sklearn.linear_model import LinearRegression
import pymysql
import copy
# 정확성 볼라구
from sklearn.metrics import accuracy_score
import time

db = pymysql.connect(host='localhost', user='root', password='1357', db='lotto_db', charset='utf8')
curs = db.cursor()

sql = "select * from new_table"

curs.execute(sql)
rows = curs.fetchall()

db.close()


true = np.array(rows)
array_num = []
cycle_num = [1, 2, 3, 4, 5, 6]



while True:
    if cycle_num[5] == 46:
        cycle_num[4] += 1
        cycle_num[5] = cycle_num[4] + 1

    if cycle_num[4] == 45:
        i = 3
        cycle_num[3] += 1
        while i < 5:
            cycle_num[i + 1] = cycle_num[i] + 1
            i = i + 1

    if cycle_num[3] == 44:
        i = 2
        cycle_num[2] += 1
        while i < 5:
            cycle_num[i + 1] = cycle_num[i] + 1
            i = i + 1

    if cycle_num[2] == 43:
        i = 1
        cycle_num[1] += 1
        while i < 5:
            cycle_num[i + 1] = cycle_num[i] + 1
            i = i + 1

    if cycle_num[1] == 42:
        i = 0
        cycle_num[0] += 1
        while i < 5:
            cycle_num[i + 1] = cycle_num[i] + 1
            i = i + 1
        if cycle_num[0] == 41:
            break

    else:
        temporary_num = copy.deepcopy(cycle_num)
        array_num.append(temporary_num)
        cycle_num[5] += 1
#94.4803376197815

pred_lotto = []
num = []
for i in range(len(true)):
    lotto_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(1, 45):
        if y in true[i]:
            lotto_num[y-1] += 1

    for z in range(len(array_num)):
        temp_lotto = copy.deepcopy(lotto_num)
        pred_lotto.append(temp_lotto)

real_sum = 0
real_sort = []

for i in range(len(array_num)):
    print(i)
    accu_first = []
    sort = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(1, 45):
        if y in array_num[i]:
            sort[y-1] += 1
    for z in range(len(true)):
        accu_first.append(accuracy_score(pred_lotto[z], sort))

    if i == 0:
        sum_fir = sum(accu_first)/len(true)
    sum_sec = sum(accu_first)/len(true)
    if sum_fir >= sum_sec:
        real_sum = sum_fir
        real_sort = sort
    else:
        real_sum = sum_sec
        real_sort = sort
    print(time.time() - start)


'''
pred_arr = []
#814만개 번호 나열
for i in range(len(array_num)):
    sort = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(1, 45):
        if y in array_num[i]:
            sort[y-1] += 1
    temp_pred = copy.deepcopy(sort)
    pred_arr.append(temp_pred)


#회차 1등 번호 나열



score = []
for i in range(len(array_num)):
    for y in range(len(true)):
        score[i] = sum[i].append(accuracy_score(pred_arr[i], pred_lotto[y]))

score = accuracy_score(array_num[0], true[922])

print(array_num[0])

acc_num = []

for i in range(len(array_num)):
    sum_scr = 0
    for y in range(len(true)):
        score = accuracy_score(array_num[i], true[y])
        sum_scr = sum_scr + score
    acc_num.append(sum_scr)

print(acc_num)


'''

#for i in range(len(rows)):

#lotto_array = np.array(rows)

#lotto_Data = pd.DataFrame(rows)




