import pymysql
import requests
import json

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber'

lotto = {}


def put_data():
    conn = pymysql.connect(host='localhost', user='root', password='password', db='lotto_db', charset='utf8')
    curs = conn.cursor()
    sql = """REPLACE INTO new_table (round,num1,num2,num3,num4,num5,num6,bnus)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
             """

    for cnt in range(1, 924):
        params = {'drwNo': cnt}

        res = requests.get(URL, params=params)

        asdf = res.text
        ffff = json.loads(asdf)

        temporary = []
        for num in range(1, 7):
            temporary.append(ffff.get("drwtNo" + str(num)))
        temporary.append(ffff.get("bnusNo"))
        lotto[cnt] = temporary

        curs.execute(sql, (
        int(cnt), int(temporary[0]), int(temporary[1]), int(temporary[2]), int(temporary[3]), int(temporary[4]),
        int(temporary[5]), int(temporary[6])))
        lotto[cnt] = temporary

    conn.commit()
    conn.close()

    return cnt
