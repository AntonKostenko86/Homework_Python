from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:admin@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    max_id = connection.execute(text(
        "SELECT MAX(subject_id) FROM subject"
    )).scalar()
    new_id = max_id + 1 if max_id else 1
    title = "Инженер по тестированию"

    new_subject = text(
        "INSERT INTO subject(\"subject_id\", \"subject_title\")"
        " VALUES (:id, :title)"
    )
    connection.execute(new_subject, {"id": new_id, "title": title})

    created_subject = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(created_subject, {"id": new_id})
    rows = result.mappings().all()

    delete_subject = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(delete_subject, {"id": new_id})

    assert len(rows) == 1
    assert rows[0]["subject_id"] == new_id
    assert rows[0]["subject_title"] == title

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    max_id = connection.execute(text(
        "SELECT MAX(subject_id) FROM subject"
    )).scalar()
    new_id = max_id + 1 if max_id else 1
    title = "Инженер по тестированию"
    new_title = "QA"

    new_subject = text(
        "INSERT INTO subject(\"subject_id\", \"subject_title\") "
        "VALUES (:id, :title)"
    )
    connection.execute(new_subject, {"id": new_id, "title": title})

    update_subject = text(
        "UPDATE subject SET subject_title = :title "
        "WHERE subject_id = :id "
    )
    connection.execute(update_subject, {"title": new_title, "id": new_id})

    updated_subject = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(updated_subject, {"id": new_id})
    rows = result.mappings().all()

    delete_subject = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(delete_subject, {"id": new_id})

    assert len(rows) == 1
    assert rows[0]["subject_id"] == new_id
    assert rows[0]["subject_title"] == new_title

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    max_id = connection.execute(text(
        "SELECT MAX(subject_id) FROM subject"
    )).scalar()
    new_id = max_id + 1 if max_id else 1
    title = "Инженер по тестированию"

    new_subject = text(
        "INSERT INTO subject(\"subject_id\", \"subject_title\") "
        "VALUES (:id, :title)"
    )
    connection.execute(new_subject, {"id": new_id, "title": title})

    delete_subject = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(delete_subject, {"id": new_id})

    deleted_subject = text("SELECT * FROM subject WHERE subject_id = :id")
    result = connection.execute(deleted_subject, {"id": new_id})
    rows = result.mappings().all()

    assert len(rows) == 0

    transaction.commit()
    connection.close()
