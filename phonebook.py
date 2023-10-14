import mysql.connector as ab
from tabulate import tabulate
conn = ab.connect(host="localhost", user="root", password="1234")
conn.autocommit=True
cur = conn.cursor()
cur.execute("create database if not exists phone")
cur.execute("use phone")
cur.execute("create table if not exists mob(name varchar(30),country_code varchar(30),phone int)")
cur.execute("create table if not exists tel(name varchar(30),std_code int,phone int)")
def add_contacts():
    
print("TELEPHONE DIRECTORY")
dict = {}
while True:
    n = input("\nSelect one (useA,B,C,D,E or F):-\nA)Add a contact\nB)View contacts\nC)Search a contact\nD)Delete a contact\nE)update a contact\nF)Exit from directory\n")
    if n == "A":
        q = int(input("how many contacts to be saved:"))
        for i in range(q):
            choice = input("\nSelect type of number to be entered:-\nX)Mobile number\nY)Telephone number\n")
            if choice == "X":
                a = (input("Enter your name:"))
                t = input("Enter country name:")
                r = t.lower()
                l1 = ["india", "usa", "uk", "uae", "saudi arabia", "russia", "singapore", "bahrin", "australia",
                      "qatar"]
                l2 = ["+91", "+1", "+44", "+971", "+966", "+7", "+65", "+973", "+61", "+974"]
                if r in l1:
                    s = l1.index(r)
                    code = str(l2[s])
                    f = int(input("Enter phone number"))
                    cur.execute(f'insert into mob values("{a}","{code}","{f}")')
            elif choice=="Y":
                a = input("Enter your name:")
                t=int(input("Enter standard code"))
                f=int(input("Enter phone number"))
                cur.execute(f'insert into tel values("{a}","{t}","{f}")')
            else:
                print("wrong entry")
        print("contacts saved successfully")
    if n=="B":
        choice = input("\nSelect the contacts you want to view:-\nX)Mobile number\nY)Telephone number\n")
        if choice=="X":
            cur.execute("select * from mob")
            o=cur.fetchall()
            h=["name","country_code","number"]
            print(tabulate(o,headers=h,tablefmt='psql'))
        elif choice=="Y":
            cur.execute("select * from tel")
            o=cur.fetchall()
            h=["name","std_code","number"]
            print(tabulate(o,headers=h,tablefmt='psql'))
        else:
            print("Wrong Entry")
    if n=="C":
        choice = input("\nSelect type of contact you want to search:-\nX)Mobile number\nY)Telephone number\n")
        if choice=="X":
            b=input("Enter name of contact")
            cur.execute(f'select * from mob where name="{b}"')
            c=cur.fetchall()
            h=["name","country_code","number"]
            print(tabulate(c,headers=h,tablefmt='psql'))
        if choice=="Y":
            b=input("Enter name of contact")
            cur.execute(f'select * from tel where name="{b}"')
            c=cur.fetchall()
            h=["name","std_code","number"]
            print(tabulate(c,headers=h,tablefmt='psql'))
        else:
            print("Wrong Entry")
            
    if n=="D":
        choice = input("\nSelect type of contact you want to delete:-\nX)Mobile number\nY)Telephone number\n")
        if choice=="X":
            e=input("Enter name of conatct to be deleted: ")
            cur.execute(f'delete from mob where name="{e}"')
            print("Contact successfully deleted")
        elif choice=="Y":
            e=input("Enter name of conatct to be deleted: ")
            cur.execute(f'delete from tel where name="{e}"')
            print("Contact successfully deleted")
        else:
            print("Wrong Entry")
            
    if n=="E":
        choice = input("\nSelect type of number to be updates:-\nX)Mobile number\nY)Telephone number\n")
        if choice=="X":
            e=input("Enter the name of contact to be updated: ")
            f=int(input("Enter the new phone number"))
            c=input("enter name of country")
            r=c.lower()
            if r in l1:
                s = l1.index(r)
                code = str(l2[s])
            cur.execute(f'update mob set phone="{f}",country_code="{code}" where name="{e}"')
        elif choice=="Y":
            e=input("Enter the name of contact to be updated: ")
            f=int(input("Enter the new phone number"))
            c=input("enter standard code")
            cur.execute(f'update tel set phone="{f}",std_code="{c}" where name="{e}"')
        else:
            print("Wrong Entry")
             
        print("contact successfully updated")
    if n=="F":
        conn.close()
        print("THANK YOU FOR USING TELEPHONE DIRECTORY")
        f=open('project.txt','r')
        print(f.read())
        exit()
    if n not in ["A","B","C","D","E","F"]:
        print("Wrong Entry,Try Again")
