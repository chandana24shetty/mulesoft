import sqlite3

#Creating a connectrion object for DB
dbname="Movies.db"
connect=sqlite3.connect(dbname)

cursor=connect.cursor()

def createTable():
    stmt=" CREATE TABLE IF NOT EXISTS Movies (actor text, actress text, year integer, director text) "

    cursor.execute(stmt)
    connect.commit()
    print("QUERY EXECUTED SUCCESSFULLY AND COMMITED TO MOVIES TABLE...")

def addMovie(actor,actress,year,director):
    stmt=" INSERT INTO Movies (actor,actress,year,director) VALUES (?,?,?,?)"
    args=actor,actress,year,director
    cursor.execute(stmt,args)
    connect.commit()
    print("QUERY EXECUTED SUCCESSFULLY AND COMMITED TO MOVIES TABLE...")

def retrieveMovieDetails(query):

    cursor.execute(query)
    connect.commit()
    print("QUERY EXECUTED SUCCESSFULLY AND COMMITED TO MOVIES TABLE...")

    for row in cursor.execute(query):
        print(row)


def main():
    welcome=""" 
                1. CREATE TABLE
                
                2. ADD MOVIE
                3. QUERYING
            """

    print(welcome)

    choice=int(input("ENTER 1, 2, 3 BASED ON YOUR NEED \n"))

    if choice == 1 :
        createTable()

    elif choice == 2 :
        actor=input("ENTER THE ACTOR NAME: ")
        actress=input("ENTER THE ACTRESS NAME: ")
        year=int(input("ENTER THE YEAR OF RELEASE: "))
        director=input("ENTER THE DIRECTOR NAME: ")

        addMovie(actor,actress,year,director)

    elif choice == 3:

        query=input("TYPE THE QUERY IN CORRECT SYNTAX: ")
        retrieveMovieDetails(query)

    else:
        print("INVALID CHOICE")




if __name__ == "__main__":
    flag="y"
    while(flag == "y"):
        main()
        flag=input("Do you wish to continue Y/N:").lower()
    print("EXITING...")
