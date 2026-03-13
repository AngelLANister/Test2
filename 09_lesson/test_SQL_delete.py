from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = "postgresql://postgres:postgres@localhost:5432/QA"


def test_insert():
    db = create_engine(db_connection_string)
    list_of_subjects_before = db.execute("select * from subject").fetchall()
    len_before = len(list_of_subjects_before)
    sql = text("insert into subject(subject_title) values (:new_subject)")
    db.execute(sql, {"new_subject": "Chinese"})
    sql_delete = text("delete from subject where subject_title = 'Chinese'")
    db.execute(sql_delete)
    list_of_subjects_after = db.execute("select * from subject").fetchall()
    len_after = len(list_of_subjects_after)
    assert len_before == len_after
