from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

class Todo(BaseModel):

    name: str
    due_date: str
    description: str
    status: str

app = FastAPI(title="API TODO")

templates = Jinja2Templates(directory="templates")

# Create, Read, Update, Delete items

store_todo = []

@app.get("/APITODO/{id}", response_class=HTMLResponse)
async def read(request: Request, id: int):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})

@app.post('/todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo

@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo

@app.get('/todo/{id}')
async def get_todo_id(id: int):

    try:
        
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

@app.put('/todo/{id}')
async def update_todo_via_id(id: int, todo: Todo):

    try:

        store_todo[id] = todo
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

@app.delete('/todo/{id}')
async def delete_todo_via_id(id: int):

    try:

        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

