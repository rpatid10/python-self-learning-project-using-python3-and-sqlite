import sqlite3

conn= sqlite3.connect('my_daily_task_tracker.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
                task_id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                task_priority TEXT NOT NULL,task_type TEXT NOT NULL,
                task_total_time TEXT NOT NULL,task_spent_time TEXT NOT NULL,
                task_current_status TEXT NOT NULL,task_eta TEXT NOT NULL,
                task_comments TEXT
)
''')

def list_all_tasks():
    try:
        cursor.execute("select * from tasks")
        rows= cursor.fetchall()
        if not  rows:
            print("No rows found: ")
        else:
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def add_task(task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments) :
    cursor.execute('''INSERT INTO tasks (task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments) VALUES (?, ?,?, ?,?, ?,?, ?)''', (task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments))
    conn.commit()

def update_task(task_id,task_name,task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments):
    #list_all_tasks()
    cursor.execute('''update tasks set task_name=?,task_priority=?, task_type=?, task_total_time=?, task_spent_time=?, task_current_status=?, task_eta=?,
         task_comments=? where task_id=?''',(task_name,task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments,task_id))
    if cursor.rowcount == 0:
        print("No video found with that ID!")
    else:
        conn.commit()

def delete_task(task_id):
    cursor.execute('''delete from tasks where task_id=?''',(task_id))
    if cursor.rowcount==0:
        print("No video found with entered Id")
    else:
        conn.commit()

def main():
    while True:
        print("\nMy personal task manager :")
        print("\n1. List all  tasks")
        print("2. Add task")
        print("3. update task")
        print("4. delete task")
        print("5. Exit application: ")
        choice=input("\nPlease enter your choice: ")

        if choice=='1':
            list_all_tasks()
        elif choice=='2':
            task_name=input("Enter task name: ")
            task_priority=input("Enter task priority (P1-P4): ")
            task_type=input("Enter task category (Personal/Professional) : ")
            task_total_time=input("Enter hrs required to complete task: ")
            task_spent_time=input("Enter hrs spent on task: ")
            task_current_status=input("Enter current status of task: ")
            task_eta=input("Enter ETA of task in (YYYY-MM-DD) format: ")
            task_comments=input("Enter comments, if any : ")
            add_task(task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments)
        elif choice=='3':
            list_all_tasks()
            task_id=input("Enter task_id to update task: ")
            task_name = input("Enter new task name: ")
            task_priority = input("Enter new task priority (P1-P4): ")
            task_type = input("Enter  new task category (Personal/Professional) : ")
            task_total_time = input("Enter hrs required to complete task: ")
            task_spent_time = input("Enter hrs spent on task: ")
            task_current_status = input("Enter current status of task: ")
            task_eta = input("Enter ETA of task in (YYYY-MM-DD) format: ")
            task_comments = input("Enter comments, if any : ")
            update_task(task_id,task_name, task_priority, task_type, task_total_time, task_spent_time, task_current_status, task_eta,
         task_comments)
        elif choice=='4':
            list_all_tasks()
            task_id = input("Enter task_id to be deleted : ")
            delete_task(task_id)
        elif choice =='5':
            break
        else:
            print("Please enter valid choice: ")




if __name__=="__main__":
    main()



