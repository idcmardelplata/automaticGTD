from behave import *
from server.inbox import inboxmodule as inbox 
from mocks import listener
from server.router import router
from server.store import store

@given("i've started listener service")
def impl_bk(context):
    listener.run()

@when("i indicate that i want to store a new input")
def impl_bk(context):
    context.stored = router.route("i want to store a new input")

@then("the system should let me store it")
def impl_bk(context):
    return store.stored=="i want to store a new input"

