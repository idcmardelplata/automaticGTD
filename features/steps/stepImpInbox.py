from behave import *
from server.inbox import inboxmodule as inbox 
from mocks import listener
from server.router import router
from server.store import store

# step doc 
# run one scenario at time with 'behave -n <SCENARIO>'

@given('i1ve started listener service')
def impl_bk(context):
    listener.run()

@when('i indicate that i want to store a new input')
def impl_bk(context):
    context.stored = router.route('i want to store a new input')

@then('the system should let me store it')
def impl_bk(context):
    return store.stored=='i want to store a new input'

@when('i indicate that i want to store a new input')
def impl_bk(context):
    return True
@then('the system should1nt let me store it')
def impl_bk(context):
    return True
@when('i indicate that i want to write a new input')
def impl_bk(context):
    return True
@then('the system should open a screen for me to do it')
def impl_bk(context):
    return True
@given('i1ve started listener service')
def impl_bk(context):
    return True
@And('i1ve wrote some content in a new input')
def impl_bk(context):
    return True
@when('i want to leave it')
def impl_bk(context):
    return True
@then('the system should ask me if i want to save it or lose it')
def impl_bk(context):
    return True

@when('i tell the system to not save it')
def impl_bk(context):
    return True
@then('create input service should exit')
def impl_bk(context):
    return True

@when('i ask the system to relate the current input i1m creating')
def impl_bk(context):
    return True
@then('system should show me a list of current projects to relate with')
def impl_bk(context):
    return True

@given('that i1ve saved inputs')
def impl_bk(context):
    return True
@when('i ask for search a particular input')
def impl_bk(context):
    return True
@then('the system should show me a list of them filtered by my request')
def impl_bk(context):
    return True
