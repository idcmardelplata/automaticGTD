##Sys goals

1. To get a simplier work managment than notion is, about
  - Getting simplier relationships
  - Getting clearer gtd sections, like weekly review and the all 5 main flow states
2. To enhance focus state while working
3. To improve task single responsabilities
4. To separate defining to working
5. To get a better conection between task and higher lever specifications and projects work
6. To be able to set reminders and see them easyly and no fail
7. To be able to work in habits optimally
8. To incorpore easyly work on contexts
9. To filter task for priority

## quality attrs priorizados


1- Disponibiildad
2- Facilidad de uso
3- Mantenibilidad
4- Extensibilidad
5- Rendimiento

#Decisiones de desarrollo

La persistencia de objetos, y la configuración, se llevará a cabo mediante python y toml, y los módulos nativos de escritura de archivos de python

El cliente será linea de comandos

Patrones de arquitectura: 

Cliente servidor para disponibilidad y facilidad de desarrollo

Patrones de diseño: Singleton para la instanciación en tiempo de ejecución de los copmonentes fundamentales del server

se valora el patrón observador para transmitir eventos desde el cliente

#techs

Python will be used for implement the first step system, then when it's working i can consider to switch to another language

# User histories

1. As user, i want to separate my gtd workflow into different sections like "inputs" "Get clear" "Organize" "Review" "Run" | Story point: 24 | Bussiness Value: 10
* Subtasks:
- Hacer listas separadas para la información de las acciones según quiera el "día a día" (trabajo) o quiera pensar sobre proyectos (especificación) (3)
- Hacer que al seleccionar esas secciones aparezcan las acciones relacionadas con cada uno, junto al texto informativo(6)
- Hacer que run muestre una lista de tareas organizadas por energía y tiempo estimado (6)
  - En el daily, muestra solamente las de la semana, sin categoría de inactivas. (3)
  - EN el especification, muestra tanto las de esta semana como todas, incluso inactivas. (3)
- Hacer que organize permita seleccionar de la lista de "aclarado" algún elemento para comenzar el flujo de procesamiento de gtd (6)
- Hacer que se pueda fácilmente ingresar cualquier información a una bandeja de inputs sin entrar a ésta (3)

2. As user, i want to crud tasks, projects, responsability areas, Goals, Vision and Life-Vision | Story point: 20 | Bussiness Value: 10
* * Subtasks::
- Ver donde guardar cada uno de esos archivos (3)
- Crear un script para crear cada uno de esos archivos a elección (5)
- Pensar cómo los voy a relacionar para: (4) 
    - Generar una estructura para cada uno (5)
    - Generar mecanismo de relación (3)

3. As user, i want to do gtd weekly reviews, to keep up the date my system | Story point: 12 | Bussines value: 10
* Subtasks:
- Hacer que al seleccionar review aparezca información al respecto de la revisión semanal (3)
- Revisar cada paso de la revisión semanal propia para determinar como automatizarlo (9)

4. As user, i want to see only necessary info both while i'm specifing and working | Story point: 19 | Bussiness Value: 9
* Subtasks:
- Pensar que información necesito para especificar (5)
- Pensar que información necesito para trabajar (6)
- Pensar como mostrar la información necesaria (3)
- Mostrar la información necesaria al iniciar especificación o ver tareas en el dia a día (5)

5. As user, i want to set the context when i want to get back the reminder to my mind | Story point: 17 | Bussiness Value: 8 
* Subtasks:
- Crear una lista de mis contextos (1)
- Crear una ventana para mostrar el texto del recordatorio (10)
- Hacer que la ventana aparezca cuando el evento desencadenante suceda sea del tipo que sea (6)

6. As user, i want the system to show me a list of tasks depending on my selected context | Story point: 6 | Bussiness Value 8 
* Subtasks:
- Crear alguina asociación entre tareas y contextos (2)
- Crear filtro por contexto en la visualización de listas de tareas (4)

7. As user, i want to set reminders for the daily  | Story point: 8 | Bussiness Value: 7
* Subtasks:
- Determinar desencadenantes del recordatorio (5)
- Pensar donde guardar los recordatorios (3)
- Pensar cómo organizar recordatorios para llevarlos a los lugares y contextos necesarios

8. As user, i want simply relate my tasks with higher perspetctives | Story point: 5 | Bussiness Value: 6
* Subtasks
- Crear una relación entre tarea y proyectos, objetivos, visiones, areas de responsability y objetivos de vida (5)

9. As user, i want to track an Habit incorporation | Story point: 11 | Bussiness Value: 1

  * Planification:
    - RealLife habit apliying cases
    - Trigger, routine, gratification
  * Revision:
    - Done times 
    - Fail times 
    - Comments for improvement (feelings, ideas...)

* Subtasks:
- Crear registro en algún lugar de los hábitos (2)
- Crear atributos de estado para los hábitos (activo, inactivo) (2)
- Crear automatización para la creación de un hábito según SMART objetives y casos de aplicación real (7)


