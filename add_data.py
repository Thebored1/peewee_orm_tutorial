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

data = [
    { 'name': 'Sandhya', 'admission': datetime.date(2018, 10, 20) },
    { 'name': 'Aarav', 'admission': datetime.date(2018, 10, 12) },
    { 'name': 'Mohammed', 'admission': datetime.date(2018, 10, 5) },
    { 'name': 'Vihaan', 'admission': datetime.date(2018, 10, 28) },
    { 'name': 'Aditya', 'admission': datetime.date(2018, 10, 14) },
    { 'name': 'Sai', 'admission': datetime.date(2018, 10, 22) },
    { 'name': 'Dev', 'admission': datetime.date(2018, 10, 28) }
]

with database.atomic():

    query = Students.insert_many(data)
    query.execute()