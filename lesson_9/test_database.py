from sqlalchemy import create_engine, inspect
import pytest

db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"

def test_db_conection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'company'


def test_select():
    db = create_engine(db_connection_string)
    conn = db.connect()
    rows = conn.execute("SELECT * FROM company").fetchall()
    conn.close()
    assert len(rows) > 0

    