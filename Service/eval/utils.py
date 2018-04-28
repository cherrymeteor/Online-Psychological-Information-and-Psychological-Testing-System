import os
import sqlite3

import pymysql
from django.conf import settings


def gen_db():
    db_url = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    db = sqlite3.connect(db_url)
    cursor = db.cursor()
    for i in range(1, 94):
        for j in range(1, 3):
            sql = """INSERT INTO eval_item_opts (question_id, option_id)
                                          VALUES('%d','%d');""" % \
                  (i, j)
            cursor.execute(sql)
    for i in range(94, 154):
        for j in range(3, 5):
            sql = """INSERT INTO eval_item_opts (question_id, option_id)
                                          VALUES('%d','%d');""" % \
                  (i, j)
            cursor.execute(sql)
    for i in range(154, 194):
        for j in range(5, 11):
            sql = """INSERT INTO eval_item_opts (question_id, option_id)
                                          VALUES('%d','%d');""" % \
                  (i, j)
            cursor.execute(sql)
    db.commit()
    db.close()


def step_2():
    # 打开数据库连接
    db = pymysql.connect("106.14.112.47", "jyedu", "jyedu", "km_jyeduwei", port=3308, charset='utf8')
    cursor = db.cursor()
    cursor.execute("SELECT * from eval_define_option_calrule")
    data = cursor.fetchall()
    db_url = r'C:\Cherrymeteor\Projects\bs-pshy\Service\db.sqlite3'
    db2 = sqlite3.connect(db_url)
    cursor2 = db2.cursor()
    id_ = 0
    for i in range(1, 94):
        for j in 'AB':
            id_ += 1
            for k in range(0, 17):
                if str(i) in data[k][6].split(',') and j == data[k][5]:
                    sql = 'update eval_item_opts set bonus_id = %d where id = %d;' % \
                          (data[k][2], id_)
                    print(i, j, sql)
                    cursor2.execute(sql)
    for i in range(94, 154):
        for j in '是否':
            id_ += 1
            for k in range(16, 29):
                if str(i) in data[k][6].split(',') and j == data[k][5]:
                    sql = 'update eval_item_opts set bonus_id = %d where id = %d;' % \
                          (data[k][2], id_)
                    print(i, j, sql)
                    cursor2.execute(sql)
    for i in range(154, 194):
        for k in range(28, 36):
            if str(i) in data[k][6].split(','):
                for j in range(5, 11):
                    id_ += 1
                    sql = 'update eval_item_opts set bonus_id = %d where id = %d;' % \
                          (data[k][2], id_)
                    print(i, j, sql)
                    cursor2.execute(sql)

    db2.commit()
    db2.close()
    db.close()


if __name__ == '__main__':
    # gen_db()
    step_2()
