import pytest
from core.inbox_text import InboxText

# TODO: Refactorizar el codigo fuente.
# TODO: Refactorizar las pruebas
# TODO: Probar los siguientes escenarios:
# Las tareas no pueden estar duplicadas.
# Es necesario establecer un formato para agregar un input (fecha de expiracion, importancia etc..)



def test_should_store_a_new_input_in_text_format():
    user_input = "this is a test"

    inbox = InboxText()
    inbox.add(user_input)

    assert inbox.count() == 1


# @pytest.mark.skip(reason="Not work yet")
def test_should_store_a_new_input():
    user_input = "this is a test"

    inbox = InboxText()
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
