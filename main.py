import mysql.connector
# Connection with Database:
mydb = mysql.connector.connect(host='localhost', database="entertainment" ,user='root', passwd='admin')

try:
    print(mydb.connection_id)

except:
    print("Connection Failure")

cursor = mydb.cursor()
#Command for Creating Database:
Q1 = "create database entertainment"
cursor.execute(Q1)

# Command for creating Table Movies:
Q2 = 'create table movies (MovieName varchar(50)primary key,ActorName varchar(50),ActressName varchar(50),DirectorName varchar(50),YearOfRelease int(4))'
cursor.execute(Q2)
print("Table Created Successfully")
# Command for Inserting Data Into Table:
query = 'insert into movies values (%s,%s,%s,%s,%s)'
record=  ('Harry Potter', 'Dainel Radcliffe','Emma Watson','David Yates', '2001')
record1= ('Fast and Furious', 'Vin Diesel', 'Jordana Brewster', 'Justin Lin', '2001')
record2= ('Iron Man', 'Robert Downey, Jr.', 'Gwyneth Paltrow', 'Jon Favreau', '2008')

#cursor.execute(query, record)
cursor.execute(query,record1)
cursor.execute(query,record2)
mydb.commit()
print('Records Inserted into Database')

# Command for Fetching Data:
cursor.execute('select * from movies')
data = cursor.fetchall()

for row in data:
    print('Movie Name:', row[0])
    print('Actor Name:', row[1])
    print('Actress Name:', row[2])
    print('Director Name:', row[3])
    print('Year of Release:', row[4])
    print()
