#language: es

Característica:
  Como usuario quiero poder ingresar un nuevo Input dentro del sistema
  El Input no puede volverse a ingresar o mantenerse en el Inbox si ya fue clarificado o procesado
  No se puede poner dos veces el mismo Input en el sistema

  Escenario: Como usuario, quiero ingresar un nuevo Input
    Dado que recivo un nuevo Input y deseo almacenarlo en el sistema
    Cuando lo cargue en el Inbox 
    Entonces el Input debera quedar disponible para clarificarse mas adelante

  Escenario: Como usuario, quiero ingresar un Input que ya existe en el Inbox 
    Dado que ya he cargado x Input en el sistema
    Cuando lo vuelva a ingresar 
    Entonces el Input no debera quedar disponible para clarificarse mas adelante y el sistema debe indicarme que no puedo duplicar un Input

  Escenario: Como usuario, quiero ingresar un Input de texto
    Dado que tengo un Input textual a guardar
    Cuando la ingrese en el Inbox
    Entonces debería quedar almacenada y disponible para clarificarse más adelante

  Escenario: Como usuario, quiero ingresar un Input de texto que contiene emoticones 
    Dado que el usuario ingresa un Input que contiene un emoticon o mas 
    Cuando lo ingrese en el Inbox 
    Entonces debería quedar disponible con el emoticon visualmente entendible

  Escenario: Como usuario, quiero ingresar un Input de audio 
    Dado que tengo un Input en audio a guardar
    Cuando la ingrese en el Inbox
    Entonces debería quedar almacenada y disponible para ser oida y clarificarse más adelante

  Escenario: Como usuario, quiero ingresar un Input de audio que no tiene audio
    Dado que tengo un archivo de audio que quiero guardar 
    Cuando lo intente ingresar en el Inbox
    Entonces el sistema no deberia permitirlo y deberia informarme que esta vacio

  Escenario: Como usuario, quiero poder grabar un Input de audio en el Inbox para luego agregarlo a el 
    Cuando quiera grabar un Input de audio para ser agregado al Inbox 
    Entonces el sistema deberia permitirme grabar ese audio y agregarlo al Inbox 

  Escenario: Como usuario, quiero que el sistema me permita escuchar el Inbox en audio que quiero agregar antes de agregarlo  
    Dado que tengo un audio listo para agregar al Inbox
    Cuando quiera escucharlo para asegurarme
    Entonces el sistema deberia permitirme reproducirlo

  Escenario: Como usuario, quiero ingresar un Input de video 
    Dado que tengo un Input en video a guardar
    Cuando la ingrese en el Inbox
    Entonces debería quedar almacenada y disponible para clarificarse más adelante

    Escenario: Como usuario, quiero ingresar un Input de video que supera los 5 minutos de duracion
    Dado que tengo un video a ingresar en Inbox que dura mas de 5minutos
    Cuando intente ingresarlo al Inbox 
    Entonces el sistema no deberia permitirlo, y deberia informarme que no puedo almacenar videos de mas de 5 minutos

  Escenario: Como usuario, quiero poder reveer el video antes de ingresarlo al Inbox
    Dado que tengo un video que quiero ingresar al Inbox 
    Cuando quiera verlo para asegurarme
    Entonces el sistema deberia permitirme reproducirlo 

  Escenario: Como usuario, quiero ingresar un Input de imagen 
    Dado que tengo un Input en imagen a guardar
    Cuando la ingrese en el Inbox
    Entonces debería quedar almacenada y disponible para clarificarse más adelante

  Escenario: Como usuario, quiero poder reveer la imagen antes de ingresarlo al Inbox
    Dado que tengo una imagen que quiero ingresar al Inbox 
    Cuando quiera verla para asegurarme
    Entonces el sistema deberia permitirme visualizarla 

