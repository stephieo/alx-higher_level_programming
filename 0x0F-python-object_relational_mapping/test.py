#!/usr/bin/python3
""" learinig sqlalchemy"""
from sqlalchemy import create_engine, Column, String,Integer, Foreignkey, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

#creating the engine
engine = create_engine("sqlite:///orm_db.db", echo=True)

#creating the baseclass for all table/classes in database
Base = declarative_base()

#creating class for a table 
class Person(Base):
    """creating class for the Persons table in database"""
    __tablename__ = "persons" #this is the name of the table in the database

    #this is where the mapping occurs. each atributte corresponds to a column in a DB
    id_no = Column("id", Integer, primary_key=True) #"name of column in database", datatype etc
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    age = Column("age", Integer)
    gender = Column("gender", CHAR)
    country = Colum("country", String)

    def __init__(self,id_no, firstname, lastname, age, gender, country):
        self.id_no id_no
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.country = country

    def __repr__(self):
        return f"{self,firstname} {self.lastname}, ({self.gender}{self.age})"


class Thing(Base):
    """Thing class/ table"""
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, Foreignkey=True("persons.id_no")) #Creates a one to many rltnshp [person -> thing]

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"




#this create all the classes that inherit from Base  as tables in the database
Base.metadata.create.all(bind=engine)

#creating a session object and instance
Session = sessionmaker(bind=engine)
session = Session()

#creating an instance of the Person abject
p1 = Person(2, "Bob", "Fitts", 60, "m", "America")
p2 = Person(12, "Anna", "Cartney", 16, "m", "Australia")
p3 = Person(22, "Hank", "Fitts", 30, "m", "America")
p4 = Person(32, "Max", "Smith", 26, "m", "Btitain")


t1 = Thing(1, "Honda Accord", p1.id_no)
t2 = Thing(21, "Toyota Highlander", p3.id_no)
t3 = Thing(31, "Cadillac Escalade", p3.id_no)
t4 = Thing(41, "Mercedes GLK", p1.id_no)

#adding the instance as an entry to the database
session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.commit() #this "makes changes permanent"



#querying tables (best to do it in a diff file)
results = session.query(Person).all() #this is equivalent to SELECT * FROM persons 
results2 = session.query(Person).filter(Person.lastname == "Fitts") #SELECT  * FROM persons WHERE lastname = "Fitts"
results3 = session.query(Person).filter(Person.lastname.like(%Fi%))#...WHERE lastname LIKE  %Fi%
results4 = session.query(Person).filter(Person.lastnamein_(["Anna", "Bob"])) #... WHERE lastname in (?, ?)


results5 = session.query(Thing).filter(Thing.owner == persion.id_no).filter(Person.firstname == "Anna") #... WHERE ... AND ...
#the printed results will be in the format specified in the repr method
for r in results:
    print(r)