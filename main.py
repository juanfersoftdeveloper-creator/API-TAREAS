from fastapi import FastAPI
#pydantic es una biblioteca para validar datos, y base model es la clase padre para crear modelos de datos.
from pydantic import BaseModel
#instancia de la clase FastAPI
#crea nuestra aplicación API.
app = FastAPI()

tareas = [{"id": 1, "titulo": "aprender Python", "completada": False},
{"id": 2, "titulo": "aprender CI/CD", "completada": False}]

#creamos un modelo de datos para la tarea para que FastAPI pueda validar los datos que se envían a la API.
class crearTarea(BaseModel):
    titulo:str

class actualizarTarea(BaseModel):
    titulo: str
    completada: bool
    

#ruta raiz
@app.get("/")#decorador que indica que es una ruta GET

#funcion que se ejecuta cuando se accede a la ruta raiz
def inicio():
    return {"mensaje": "mi primera API"}
    

@app.get("/tareas")
def get_tareas():
    return tareas


@app.get("/tareas/{id}")
def get_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    return {"error": "Tarea no encontrada"}


@app.post("/tareas")
def crear_tarea(tarea: crearTarea):
    nueva_tarea = {
    "id": len(tareas) + 1, 
    "titulo": tarea.titulo,
    "completada": False
}
    tareas.append(nueva_tarea)
    
    return nueva_tarea


@app.put("/tareas/{id}")
def update_tarea(id: int, datos: actualizarTarea):
    for tarea in tareas:
       if tarea["id"] == id:
           tarea["titulo"] = datos.titulo
           tarea["completada"] = datos.completada
           return tarea
    return {"error": "tarea no encontrada"}


@app.delete("/tareas/{id}")
def delete_tarea(id:int):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            return {"mensaje":"tarea eliminada"}
    return {"error": "tarea no encontrada"}