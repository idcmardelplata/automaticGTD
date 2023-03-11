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


