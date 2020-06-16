import sqlite3

db = "test.db"
tablesql = 'create table data(No int,User text,Stock_name text,Date text,Price int,Sell_price int,Quantity int,Description text);'
insertsql = '''insert into data(No, User, Stock_name, Date,Price, Sell_price, Quantity, Description) values(?,?,?,?,?,?,?,?)'''

def connect():
    return sqlite3.connect(db)

def main():
    con = connect()
    cur = con.cursor()
    if cur:
        #create table
        cur.execute(tablesql)   
        con.commit()


def insert_data(User, Stock_Name , Date, Price, Sell_Price, Quantity, Description):
    con = connect()
    cur = con.cursor()
    No = cur.execute("select * from data").fetchall().__len__() + 1
    values = [No, User, Stock_Name, Date, Price,
              Sell_Price, Quantity, Description]
    cur.execute(insertsql, values)
    con.commit()

def get_data():
    con = connect()
    cur = con.cursor()
    a = cur.execute("select * from data")
    return a.fetchall()

if __name__ == "__main__":
    main()
