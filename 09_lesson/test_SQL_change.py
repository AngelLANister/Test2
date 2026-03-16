from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "postgresql://postgres:postgres@localhost:5432/QA"


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into subject(subject_title, "
               "subject_id) values (:new_subject, :new_subject_id)")
    db.execute(sql, {"new_subject": "Chinese", "new_subject_id": 16})
    sql_update = text("update subject set "
                      "subject_id = 17 where subject_id = 16")
    db.execute(sql_update)
    new_id = db.execute(text("select subject_id from "
                             "subject where subject_title = "
                             "'Chinese'")).scalar()
    assert new_id == 17

    sql_delete = text("delete from subject where subject_title = 'Chinese'")
    db.execute(sql_delete)
