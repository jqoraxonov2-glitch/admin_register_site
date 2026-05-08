from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone() # row bittasini oladi
    if row is None:
        return False
    columns = [col[0] for col in cursor.description] # column key valueni 1 tasini oladi
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subjact():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_subjact""")
        subjact = dictfetchall(cursor)
        return subjact


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_teachers""")
        teacher = dictfetchall(cursor)
        return teacher


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_groups""")
        group = dictfetchall(cursor)
        return group


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_students""")
        student = dictfetchall(cursor)
        return student

















