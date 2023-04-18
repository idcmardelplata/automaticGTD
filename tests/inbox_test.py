import pytest
from core.inbox_text import InboxText
import os

# TODO: Refactorizar el codigo fuente.
# TODO: Refactorizar las pruebas
# TODO - Buscar si existe algun before para cargar estado en memoria de los testeos unitarios y así remover el clean()
# TODO: Probar los siguientes escenarios:
# Las tareas no pueden estar duplicadas : DONE
# Es necesario establecer un formato para agregar un input (fecha de expiracion, importancia etc..) : 
# TODO: determinar el uso del almacenamiento en memoria de los inputs, en la principal y en el disco... ¿Por que dejarías algo en memoria en el objeto inbox si lo estas persistiendo automáticamente al añadirse con add()?

inbox = InboxText()
#necesita refactor

def test_should_store_a_new_input_in_text_format():
    user_input = "this is a test"

#    inbox = InboxText()
    inbox.add(user_input)

    assert inbox.count() == 1


# @pytest.mark.skip(reason="Not work yet")
def test_should_store_a_new_input():
    user_input = "this is a test"

#    inbox = InboxText()
    inbox.add(user_input)

    inboxes = inbox.load()

    assert len(inboxes) == 1

# @pytest.mark.skip(reason="Not work yet")
def test_should_ask_for_where_persist():
    user_input = "thing"
    user_saving_election = "/home/martin/josu_diagrams/automaticOrganization/inputsDB"
    inbox = InboxText(metadata = {'path': user_input })
    
    inbox.add(user_input)
    assert inbox.count() == 1

def test_inputs_cannot_be_duplicated():
    inbox.clean()
    inbox.add("non duplicable input")
    inbox.add("non duplicable input")
    assert inbox.count() == 1
    with open("/tmp/inputs.txt","r+") as file:
        assert file.read().count("non duplicable input") == 1
