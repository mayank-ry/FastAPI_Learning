from fastapi import FastAPI
from app.models import Task


app = FastAPI()

tassk = [Task(id = 1,name = "Mayank",desc = "The Name Is Yashhh")]


@app.get("/")
def home():
    return {"message":"Welcome To iNotes"}


@app.get("/Task")
def read():
    return tassk

@app.get("/Task/{task_id}")
def read_id(task_id:int):
    for object in tassk:
        if object.id==task_id:
            return object
    return {"message":"Task Id Not Found"}

@app.post("/Create_Task")
def create_task(object : Task):
    for items in tassk:
        if object.id == items.id:
            return {"message":"Id Already Register"}
    tassk.append(object)
    return {"message":"Task Added Successfully"}     
    
    
@app.delete("/Delete/{task_id}")
def delete_task(task_id : int):
    for object in tassk:
     if object.id==task_id:
        tassk.remove(object)
        return {"message" : "Task Deleted Successfully"}
    return {"message":"Task Not Found"}

@app.put("/update/{task_id}")
def update_task(task_id : int,newNode : Task):
    for object in tassk:
        if object.id ==task_id:
            tassk.remove(object)
            tassk.append(newNode)
            return {"message":"Updated Successfully"}
    return {"message":"Id Not Found"}
    


