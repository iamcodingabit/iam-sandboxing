from enum import Enum

class Status(Enum):
    BACKLOG = "backlog"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

def main():
    todolist = [{
        "task": "Clean up room",
        "status": Status.IN_PROGRESS.value
    }, {
        "task": "Start coding",
        "status": Status.IN_PROGRESS.value
    }]
    
    commands = {
        "clear": 
            {
                "function": lambda todolist, arg: clearTasks(todolist),
                "description": "Clear the whole list"
            },
        "add": 
            {
                "function": lambda todolist, arg: addTask(todolist, arg),
                "description": "Clear the whole list"
            },
        "finish": 
            {
                "function": lambda todolist, arg: finishTask(todolist, arg),
            },
        "help": 
            {
                "function": lambda todolist, arg: helpCommands(),
            },
        "exit":
            {
                "function": lambda todolist, arg: exitProgram(),
            }
    }
    
    displayTasks(todolist)
    print("type 'clear' to clear up the sample")
    
    while True:
        user_input = input("I want to: ")
        command_input = processCommand(user_input)
        
        command_function = commands.get(command_input[0])
        
        if command_function["function"]:
            result = command_function["function"](todolist, command_input[1])
            
            if result is False:
                break
        else:
            print("Invalid command")
        
        displayTasks(todolist)
    
    print("Bye, people!")
    
def processCommand(input_string):
    input_string = input_string.split(" ", 1)
    
    if(len(input_string) <= 1):
        input_string.append(0)
        
    return input_string

def displayTasks(todolist):
    for index, task_item in enumerate(todolist):
        print(f"{index+1}. {task_item["task"]} | {task_item["status"]}")
    
def clearTasks(todolist):
    todolist.clear()
    
def addTask(todolist, task):
    todolist.append({"task": task,
                     "status": Status.BACKLOG.value})
    
def finishTask(todolist, taskNumber):
    taskIndex = int(taskNumber) - 1
    todolist[taskIndex]["status"] = Status.COMPLETED.value

def exitProgram():
    return False
    

# def helloWorld():
if __name__ == "__main__":
    main()