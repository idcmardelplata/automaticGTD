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
