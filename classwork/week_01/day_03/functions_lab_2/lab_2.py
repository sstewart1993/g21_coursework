tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasksd
# Print a list of completed tasks
# Print a list of all task descriptions
# Print a list of tasks where time_taken is at least a given time
# Print any task with a given description


def uncompleted_tasks_list(tasks):    
    uncompleted_tasks = []
    for task in tasks:
        if (task["completed"] == False):
            uncompleted_tasks.append(task)
    return(uncompleted_tasks)
    
print(uncompleted_tasks_list(tasks))

def completed_tasks_list(tasks):    
    completed_tasks = []
    for task in tasks:
        if (task["completed"] == True):
            completed_tasks.append(task)
    return(completed_tasks)
    
print(completed_tasks_list(tasks))

def task_descriptions(tasks):
    all_tasks = []
    for task in tasks:
        all_tasks.append(task["description"])
    return all_tasks

print(task_descriptions(tasks))

def at_least_time(tasks, time_taken):
    timed_tasks = []
    for task in tasks:
        if (task["time_taken"] >= time_taken):
            timed_tasks.append(task)
    return timed_tasks

print(at_least_time(tasks, 30))

def task_with_given_description(tasks, description):
    described_task_list = []
    for task in tasks:
        if (task["description"] == description):
            described_task_list.append(task)
    return described_task_list

print(task_with_given_description(tasks, "Walk Dog"))

def mark_complete(tasks, description):
    for task in tasks:
        if (task["description"] == description):
            task["completed"] = True

mark_complete(tasks, "Clean Windows")

print(tasks)

def add_to_list(tasks, new_task):
    tasks.append(new_task)

added_task = { "description" : "Go To Sleep" , "completed" : False , "time_taken" : 480}

add_to_list(tasks, added_task)
print(tasks)


