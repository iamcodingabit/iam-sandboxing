interface Task{
    task_name: string,
    task_status: TaskStatus,
}

type TaskStatus = "backlog" | "in-progress" | "finished";


const tasks: Task[] = [
    {
        task_name: "make coffee",
        task_status: "backlog"
    },
    {
        task_name: "try typescript again",
        task_status: "in-progress"
    }
];

const add = (task_name: string) => {
    tasks.push({
        task_name: task_name,
        task_status: "backlog"
    })
}

const remove = (task_number: number) => {
    const index_to_remove:number = task_number-1;
    tasks.splice(index_to_remove, 1);
}

const list = () => {
    if (tasks.length > 0) {
        tasks.forEach((value: Task, index: number) => {
            console.log(`${index+1}. ${value.task_name} - ${value.task_status}`);
        });
    } else {
        console.log("No tasks!")
    }
}

function clearTasks(){
    tasks.splice(0, tasks.length)
}

function main(): void{
    add("Do the chores now");
    add("Do the laundry");
    list();
    remove(4);
    list();
}

main()