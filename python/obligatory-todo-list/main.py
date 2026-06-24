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
                "description": "Clear the whole list",
                
            },
        "add": 
            {
                "function": lambda todolist, arg: addTask(todolist, arg),
                "description": "Add a new task to the least",
                "example": "add code the Read class",
            },
        "finish": 
            {
                "function": lambda todolist, arg: finishTask(todolist, arg),
                "description": "Set a task to completed, using the tasks current number",
                "example": "finish 2",
            },
        "help": 
            {
                "function": lambda todolist, arg: helpCommands(arg),
                "description": "See all commands"
            },
        "exit":
            {
                "function": lambda todolist, arg: exitProgram(),
                "description": "Exit the programs"
            }
    }
    
    displayTasks(todolist)
    print("type 'clear' to clear up the sample")
    
    while True:
        user_input = input("I want to (type 'help' for command lists): ")
        command_input = processCommand(user_input)
        
        command_function = commands.get(command_input[0])
        
        try:
            if command_function["function"]:
                if command_input[0] == "help":
                    command_input[1] = commands
                result = command_function["function"](todolist, command_input[1])
                
                if result is False:
                    break
        except ValueError as e:
            print(f"Invalid command\n{e}")
        print()
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

def helpCommands(commands):
    for command, attribute in commands.items():
        description = attribute.get("description", "N/A")
        example = attribute.get("example", "N/A")
        
        print(f"- Command Name: {command}")
        print(f"Description: {description}")
        print(f"Example: {example}")

def exitProgram():
    return False

# def helloWorld():
if __name__ == "__main__":
    main()