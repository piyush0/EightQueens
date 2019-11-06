from core import runner
from db.create_answer_table import db, answers, conn
from sqlalchemy.dialects.postgresql import insert


def put_answers(n):
    # If we already put the answer once, don't put it again
    query = insert(answers).on_conflict_do_nothing()
    values_list = list()
    for i in range(1, n + 1):
        values_list.append({'Num': i, 'Ans': runner(i)})
    conn.execute(query, values_list)


def get_answers():
    results = conn.execute(db.select([answers])).fetchall()
    print(results)


def clear_answers():
    query = answers.delete()
    conn.execute(query)
    print('Deleted all entries of the table')
