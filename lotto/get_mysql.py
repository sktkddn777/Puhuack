import pymysql


def get_data():
    db = pymysql.connect(host='localhost', user='root', password='password', db='lotto_db', charset='utf8')
    curs = db.cursor()

    sql = "select * from new_table"
    curs.execute(sql)
    rows = curs.fetchall()

    db.close()
    return rows

