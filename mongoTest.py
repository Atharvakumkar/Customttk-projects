from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
task_collection = db.task

def create_task(description):
    task = {
        'task' : description
    }
    result = task_collection.insert_one(task)
    print(f'Task created with id {result.inserted_id}')

def show_task():
    showTask = list(task_collection.find())
    if not showTask:
        print("No tasks found.")
    else:
        for task in showTask:
            print(f"- {task['task']} (ID: {task['_id']})")

while True:
    print("\n1. Create task: ")
    print("2. View task: ")
    print("3. Exit: ")

    choice = input("Enter choice: ")

    if choice == '1':
        description = input("Enter your task: ")
        create_task(description)
    elif choice == '2':
        show_task()
    elif choice == '3':
        break
    else:
        print('Please enter valid input!')
