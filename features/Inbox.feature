#language: es

Característica:
  Como usuario quiero poder volcar un nuevo input dentro del sistema
  El input no puede volver al inbox si ya fue clarificado o procesado
  No se puede poner dos veces el mismo input en el sistema

  Escenario: Como usuario deseo poder ingresar nueva informacion
    Dado que recivo nueva informacion y deseo almacenarla en el sistema
    Cuando la cargue en el inbox 
    Entonces La informacion debera quedar disponible para clarificarse mas adelante

  # Escenario: El input a ingresar ya existe en el inbox
  #   Dado que la informacion ya existe en el sistema
  #   Cuando intente cargarla nuevamente el inbox 
  #   Entonces el sistema me debera avisar que la informacion ya existe
  #   Y no debe permitirme ingresarla
  #
  # Escenario: Un input no puede volver al inbox si ya fue clarificado o procesado 
  #   Dado que estoy en la etapa de clarificar la informacion
  #   Entonces el input no debe volver a estar en el inbox.
  #

