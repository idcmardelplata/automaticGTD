# Gtd es una metodologia de organizacion personal/empresarial

que tiene raices en el concepto de "fluye como el agua" de las artes marciales.

La idea es que uno pueda ir poniendo dentro del sistema
distintos tipos de tareas como notas (grandes o pequeñas) y olvidarse por completo de ello,
asumiendo que el usuario revisara las tareas y las organizara 1 o 2 veces por semana.
Tambien permite enviar notificaciones de tareas que tienen una fecha limite de ejecucion.


## Los 5 pasos clave son:

### Recopilar/Capturar informacion

El objetivo de este paso es descargar la mente, en este paso
debemos descargar lo que se nos ocurra en una "bandeja de entrada" o "input" (podemos tener varias bandejas de entrada)

### Procesar/Aclarar esa informacion

En este paso se aclara la informacion, en este paso debemos decidir que es esa informacion que hemos recopilado.

### organizar

En este paso debemos organizar las tareas segun lo que sea y su objetivo, para ello primero hay que preguntarse
si esa tarea requiere o no alguna accion y si:


#### No require accion

La tarea puede ir a 3 sitios especificos:

##### A la basura (porque es una tarea inutil)


##### A incubar (si es algo interesante pero no sabemos cuando lo vamos a hacer)


##### A referencias (informacion que puede ser util en cualquier otro momento).


#### Requiere accion

La tarea puede ir principalmente a dos lugares distintos

##### Un proyecto (se usa para tareas que requieran multiple subtareas para completarse)


##### Una tarea

La haremos nosotros u alguna otra persona?

###### La haremos nosotros: 

1. Si lleva menos de 2 minutos hacerla, entonces conviene hacerla ahi mismo.
2. Si require una accion o un contexto o mas de 2 o 5 minutos entonces podemos moverla a 2 puntos:
2.1 Listas de verificacion (todo aquello que tengamos que hacer en el dia o que necesite un contexto determinado)
2.2 Agendar la tarea para cierto dia/hora

###### La hace otra persona:

lo delegamos a la espera (conviene ponerle un vencimiento para que no se diluya entre todas las tareas delegadas)


### Evaluar/Reflexionar

En esta etapa debemos evalular los objetivos y metas de forma periodica, para saber que esta funcionando y que no 
Aca podemos hacer varios tipos de evaluaciones:


#### Evaluacion semanal

Aca podemos evalular que esta funcionando y que se puede mejorar.


#### Evaluacion mensual

Aca podemos evalular que tareas nos van acercando cada vez mas a nuestros objetivos.
en esta etapa podemos revisar las tareas que estan en estado "incubadas" o "algun dia..."


#### Evaluacion anual

Aca podemos evaluar si hemos podido alcanzar los objetivos marcados para este año y que tan cerca estamos
de cumplirlos, que tareas nos han acercado mas a ese objetivo y tambien plantear los objetivos para el año proximo


### Hacer/Ejecutar

En este paso simplemente ejecutamos las tareas



## Aplicaciones similares probadas

### DGT GTD (open source)

    - Environment: Android
        - Pros:
            - Muy completa
            - Open source
        - Contras:
            - Descontinuada
            - Interfaz poco intuitiva


### Chaos Control

    - Environment: Android
        - Pros:
            - Intuitiva
            - Facil de organizar
        - Contras:
            - Propietaria
            - Limita el numero de tareas a realizar por dia.


### TodoIst

    - Environment: Multiplataforma
        - Pros:
            - Multiplataforma
            - Intuitiva
            - Muy configurable
            - Facil de organizar
        - Contras:
            - Propietaria
            - Limita bastante en la version gratuita


Puntos en comun de las aplicaciones analizadas:
- Todas las aplicaciones de pago basan su modelo de negocio en limitar tareas o proyectos
- Muy pocas aplicaciones permiten sincronizacion entre dispositivos
- Interfaces rigidas (no se permite reordenar widgets)
- Unicamente trabajan con texto como input
- No se adaptan a distintos entornos (cli, desktop, movile etc).
- Si bien se permite la sincronizacion en la nube los provedores de cloud soportados son muy pocos.
- Las notificaciones unicamente son en el dispositivo local (no se pueden configurar distintos tipos de notificaciones)
- Muchas veces es dificil encontrar una tarea en particular
- Unicamente TodoIst permite la integracion con IFTTT
- Notificar a las personas a las cuales se les delego una tarea
- Si bien en la mayoria se pueden exportar las tareas estas se exportan en formato markdown y pierden sus relaciones y contexto




## Casos de uso:

- Volcar ideas dentro del sistema VP: 5, SP: 8
- Poder procesar esas ideas (**profundizar en lo que procesar significa en este contexto**) VP: 8, SP: 13
  


# Proyecto GTD

## Objetivos del Proyecto

- Poder organizar facilmente las tareas, volcar ideas y poder organizarlas
- Poder procesar ideas y evalularlas facilmente. 


## Casos de uso elementales

- Poder estudiar sobre un tema en particular
- Poder alcanzar una meta en particular mediante una serie de pasos (tareas)
- Poder organizar todas las tareas que debo hacer durante el dia/semana/mes/año
- Para cada tarea, necesito poder priorizar segun la informacion.


## Publico Objetivo

- Estudiantes
- Empresarios
- Cualquier persona que desee organizar sus tareas para ser mas productivo


## Plazos y tiempos de entrega

- En la primera semana se tiene que poder agregar tareas al sistema

- Tambien se debe configurar bien el proceso de scafolding de la aplicacion para detectar
  y automatizar toda tarea que resulte ser repetitiva o lleve tiempo hacerla manualmente o que
  sea propensa a equivocaciones.



## Tecnologias recomendadas

Lenguaje: Python (Es simple, portable y permite hacer facilmente lo que necesitamos)
Frameworks/Librerias: ://ptg.bczsalba.com:} [pytermgui]
Environment: CLI



## Roles y entidades de dominio

### Roles:

- Usuario:
- Sistema


### Objetos de dominio

- Inputs (tareas)
- Proyectos



# Restricciones

- Descargar elementos en la bandeja de entrada debe ser igual de sencillo que enviar un tweet
  o enviar un mensaje por whatsapp.

- se debe notificar que tareas no poseen ni fecha limite ni contexto cada cierto tiempo
  para recordar al usuario que las gestione. 


# Observaciones:

- Es necesario crear una forma de relacionar ciertas tareas (¿extendiendo markdown?)


## User Histories

1. Como usuario, quiero que el sistema separe las funcionalidades relacionadas con el flujo de informacion a trabajo en 5 pasos diferentes, Inbox, clarificar, Organizar, Revisar, Ejecutar // dudosa, no es concreta

2. Como usuario, quiero CrUD una descripción de identidad deseada, para poder relacionarla con mis Objetivos

3. Como usuario, quiero CrUD un objetivo de medio Plazo

4. Como usuario, quiero CrUD proyectos

5. Como usuario, quiero CrUD acciones que pertenezan a un proyecto o más

6. Como usuario, quiero que el sistema me presente un metodo ordenado por defecto para hacer revisiones semanales basado en la metodologia Avanzar Posiciones

8. Como usuario, quiero ver informacion unicamente necesaria segun la etapa en la que este en el momento actual de GTD // dudoso, no es simple ni concreta

9. Como usuario, quiero poder asignarle uno o mas contextos a una accion

10. Como usuario, quiero que el sistema me muestre una lista de acciones correspondientes segun el/los contexto/s que elija

11. Como usuario, quiero poder relacionar un proyecto con uno o mas objetivos de medio Plazo

12. Como usuario, quiero agregar inputs audiovisuales y textuales a una bandeja de entrada centralizada

13. Como usuario, quiero que el sistema me presente un metodo ordenado por defecto para clarificar 

14. Como usuario, quiero poder crear contextos en el sistema

15. Como usuario, quiero que el sistema me presente un metodo ordenado de Organizacion 

16. Como usuario, quiero que el sistema me presente un metodo ordenado de Revision por cada lista por defecto del sistema 

17. Como usuario, quiero que el sistema me presente un metodo ordenado de Ejecucion 

18. Como usuario, quiero que el sistema me permita modificar los metodos ordenados por defecto para los estados de gtd

## Value Points

El formato es: Value Point(17) -> Índice, Índice

17 -> 12
16 -> 5
15 -> 4
14 -> 9
13 -> 10
12 -> 17
11 -> 18
10 -> 14
9 -> 16
8 -> 13
7 -> 1
6 -> 15
5 -> 3
4 -> 11
3 -> 6
2 -> 2
1 -> 8

## Interdependencias de las 5 más importantes (12,5,4,9,10)

12 no tiene dependencia con las listadas
5 depende de 4
4 no tiene dependencia con las listadas
9 depende de 14
10 depende de 5 y de 14

## acciones de las 5 más importantes

14:
  - Determinar almacenamiento de los contextos en el dispositivo
  - Determinar el modelo de datos que debería tener un contexto
  - Permitir ingresar un texto como nombre del contexto
  - Asegurarme de que no sea repetible un contexto
  - Permitir visualizar en una lista todos los contextos almacenados
  - Permitir modificar el nombre de un contexto
  - Permitir eliminar un contexto 
4:
  - Determinar almacenamiento de los proyectos en el dispositivo
  - Determinar el modelo de datos que debería tener un proyecto 
  - Asegurarme que no sean repetibles en el sistema 
  - Permitir crear un nuevo proyecto 
  - Permitir almacenar un nuevo proyecto 
  - Permitir modificar los atributos de un proyecto existente
  - Permitir eliminar un proyecto existente
  - Indicar llamativamente cuando un proyecto no tenga al menos 1 acción 
5: 
  - Determinar almacenamiento de las acciones en el dispositivo
  - Determinar el modelo de datos que debería tener una acción
  - Asegurarme que no sean repetibles en el sistema
  - Permitir crear una acción
  - Permitir modificar una acción existente 
  - Permitir indicar si una acción está desbloqueada  para accionarse o está bloqueada por otra
  - Indicar en caso de estar bloqueada por otra acción o varias, por cuales
  - Permitir eliminar una acción existente
  - Indicar llamativamente cuando una acción no tenga al menos un contexto
  - Indicar llamativamente cuando una acción no tenga al menos un proyecto 
  - Permitir agendar la fecha en la cual se creó la acción en el sistema
9:  
  - Permitir ingresar uno o varios contextos existentes a una acción ya existente
  - Permitir ingresar uno o varios contextos existentes a una acción cuando ésta se está creando
  - Permitir eliminar uno o varios contextos de una acción
  - Al intentar eliminar un contexto que tiene relacionadas acciones, indicarlo de forma llamativa e informativa al usuario mostrando cuales acciones quedan sin contexto
  - Al eliminar un contexto que tiene relacionadas acciones, asegurarme que no se puedan listar al filtrar acciones por el contexto eliminado
  - Al eliminar "" "" "", asegurarme que acciones relacionadas con el contexto eliminado, pero también con otros, puedan ser listadas al filtrar acciones por esos otros contextos existentes
10:
  - Permitir ingresar un contexto o varios por los cuales filtrar las acciones existentes 
  - Crear una lista filtrada por demanda según el contexto ingresado


## Requerimientos para las 5 historias más importantes
 
12. Como usuario, quiero agregar inputs audiovisuales y textuales a una bandeja de entrada centralizada

1. Tecnologias:
  - Python para la lógica de negocio
  - Python para la interfaz de usuario
  - x para almacenamiento de los inputs -> decidir
  - ¿Cómo grabar una nota de audio? -> aprender
  - Cómo se almacenan los caractéres especiales y emoticones? deberían almacenarse de qué forma? -> aprender
  - ¿Cómo almacenar una imagen? -> aprender
  - ¿Cómo almacenar un video?
2. Casos de uso 
  - Agregar input de texto
  - Agregar input de audio
  - Agregar input de video
  - Agregar input de imagen
3. Reestricciones
  ?
4. Atributos de calidad
  - Accesibilidad
  - Facilidad de uso 
  - Fiabilidad de almacenamiento
5. Lenguaje Obicuo:
  - Inbox: Es una bandeja de entrada con la responsabilidad de almacenar información nueva para el individuo
  - Input: Es la información nueva que el individuo debe almacenar en el inbox
  - Clarificar: Es un proceso donde se extrae conocimiento significativo para la persona de un input y se la organiza en el sistema
