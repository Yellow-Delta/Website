import sqlite3


def delete_row(table, where: dict, db):
    conn = sqlite3.connect(f"databases/{db}")
    c = conn.cursor()

    where_clause = " AND ".join([f"{col}=?" for col in where])
    values = list(where.values())

    sql = f"DELETE FROM {table} WHERE {where_clause}"
    c.execute(sql, values)

    conn.commit()
    conn.close()


def select_rows(table, db, where: dict = None):
    conn = sqlite3.connect(f"databases/{db}")
    c = conn.cursor()

    if where:
        where_clause = " AND ".join([f"{col}=?" for col in where])
        values = list(where.values())
        sql = f"SELECT * FROM {table} WHERE {where_clause}"
        c.execute(sql, values)
    else:
        sql = f"SELECT * FROM {table}"
        c.execute(sql)

    rows = c.fetchall()
    conn.close()
    return rows


def insert_row(table, data: dict, db):
    conn = sqlite3.connect(f"databases/{db}")
    c = conn.cursor()

    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    values = list(data.values())

    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    c.execute(sql, values)

    conn.commit()
    conn.close()


def update_row(table, data: dict, where: dict, db):
    conn = sqlite3.connect(f"databases/{db}")
    c = conn.cursor()

    set_clause = ", ".join([f"{col}=?" for col in data])
    where_clause = " AND ".join([f"{col}=?" for col in where])

    values = list(data.values()) + list(where.values())

    sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    c.execute(sql, values)

    conn.commit()
    conn.close()
