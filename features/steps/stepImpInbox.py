from behave import *

class Core:
    def __init__(self) -> None:
        self.inbox = []
        return None

    def add(self, input):
        self.inbox.append(input)


@given("que recivo nueva informacion y deseo almacenarla en el sistema")
def receive_new_info(context):
    context.core = Core()
    context.new_info = "hola que tal"

@when("la cargue en el inbox")
def add_new_info(context):
    context.core.add(context.new_info)

@then("La informacion debera quedar disponible para clarificarse mas adelante")
def info_is_stored(context):
    len(context.core.inbox) == 1

