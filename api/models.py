import peewee as pw


def get_db():
    db = pw.SqliteDatabase('my_app.db')
    return db


class CategoryModel(pw.Model):
    id = pw.AutoField()
    name = pw.CharField(unique=True)
    description = pw.TextField()

    class Meta:
        database = get_db()


DB = get_db()
DB.create_tables((
    CategoryModel,
))
