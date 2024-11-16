from tinydb import TinyDB, Query

db = TinyDB('./db.json')

todos = Query()

def create():
    inputTask = input("Enter a task to create: ")
    print("add task:", db.insert({'task': inputTask}))
    
def read():
    inputTask = input("Enter the task to read: ")
    print("read task:", db.search(todos.task == inputTask))

def update():
    inputTask = input("Enter the task to update: ")
    inputInfo = input("Enter new info: ")
    update = db.update({'task': inputTask}, todos.task == inputInfo)
    print(update)
    
def delete():
    inputTask = input("Enter the task to delete: ")
    print("delete task:", db.remove(todos.task == inputTask))

loop = True

while loop:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    userinput = input("Enter your command: ")
    if userinput == "1":
        create()
    elif userinput == "2":
        read()
    elif userinput == "3":
        update()
    elif userinput == "4":
        delete()
    loop = False
        
        
    
    # create
    # read
    # update
    # delete