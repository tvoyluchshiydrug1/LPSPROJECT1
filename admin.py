"""admin.py has its own functions so it doesn't import patient.py and works on MasterTables Only

Two more function are left please make it * admsearch() and * update()'''  

import main
import sys
t,w=0,0
def tw(n):
    global t
    global w
    t=a.execute("desc {}").format(n)
    w=a.execute("select * from {}").format(n)
Lfield,LType,LKey=[],[],[]
    for i in t
        Lfield=i[0];LType=i[1];LKey=i[3]#Will have to be adjusted
    
def admsee(n):
    while true:
        o=input('''a.Structure
        b.Records
        c.Back To Menu''')
        if o=='a':
            print(t)
        elif o=='b':
            op=input("""a.All 
            b.Specific""")
            if op=='a':
                print (w)
            elif op=='b':
                admsearch()
            elif op=='c':
                return
            else:
                print("Invalid Input option .\n Enter Again:-")


def admmod(o,to='a'):
    n=o
    tw(o)
    print(w)
    if o=='a':
        b,p,pvalue,v=admsearch()
        #Input here the varables and check their Data Types if ok then execute insertinto command
        update()
    if o=='b':
        b,p,pvalue,v=admsearch()
        
        if b==True:
            print("values are :-",Lfield,v)
            update()
        else:
            return

def update():
    return
    #this function will be discussed at th last of the project
    # this function will update all non master tables according to changes done in master tables
    pass
def admsearch(o):
    #This is crucial function used by all search functions.
    tw(o)
    
def adst():
    
    while True:
        op=input('''A.Modify 
        C.LogOut''')
        if op=='A':
            o=input("""Tables :- """,T)
            to=input("""a.Insert New Data Record
            b.ModifyExisting Record
            """)
            admmod(o,to)
            print("done")
        if op=='B':
            print("logging out")
            main.start()
        else :
            print("Invalid Input option .\n Enter Again:-")
'''decide T'''
