import peewee
import datetime

database = peewee.SqliteDatabase("test.db")

class Students(peewee.Model):
    """
    ORM model of the Students table
    """
    name = peewee.CharField()
    admission = peewee.DateField(default=datetime.date.today)

    
    class Meta:
        database = database
        

class Schools(peewee.Model):
    """
    ORM model of Schools table
    """
    school = peewee.CharField()
    location = peewee.CharField()
    
    class Meta:
        database = database
        
        
if __name__ == "__main__":
    """
    Handling exceptions
    """
    try:
        Students.create_table()
    except peewee.OperationalError:
        print ("Students table already exists!")
    
    try:
        Schools.create_table()
    except peewee.OperationalError:
        print ("Schools table already exists!")

query = Students.update(admission=datetime.date(2018, 10, 27)).where(Students.id == 1)
n = query.execute()

print('# of rows updated: {}'.format(n))