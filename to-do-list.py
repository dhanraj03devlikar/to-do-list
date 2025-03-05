class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f" {task}    ADDED")
    
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f" {task}    REMOVED")
        else:
            print(f"{task} is not in list")

    def view_task(self):
        if not self.tasks:
            print("nothing inside tasks...")
        else:
            for idx, task in enumerate(self.tasks,start =1):
                print(f" {idx}. {task}")


if __name__ == "__main__":
    to_do_list = ToDoList()

    while True:
        print("\n OPTIONS THAT YOU CAN PERFORM...")
        print("1. ADD TASK")
        print("2. REMOVE TASK")
        print("3. VIEW TASK")
        print("4. EXIT")
        choice = input("Enter The choice : ")

        choice = int(choice)
        if(choice == 1):
            task = input("Enter Task to Add : ")
            to_do_list.add_task(task)
        elif(choice == 2):
            task = input("Enter task for remove : ")
            to_do_list.remove_task(task)
        elif(choice == 3):
            to_do_list.view_task()
        elif(choice == 4):
            break
        else:
            print("Please enter valid input")


