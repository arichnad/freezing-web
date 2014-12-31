# See: https://docs.djangoproject.com/en/1.6/topics/db/sql/#executing-custom-sql-directly
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    
def dictfetchone(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone))
    