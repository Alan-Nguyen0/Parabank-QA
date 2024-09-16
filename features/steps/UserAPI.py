from behave import *
import requests
from xml.etree import ElementTree
import json

@given(u'a request url https://parabank.parasoft.com/parabank/services/bank')
def step_impl(context):
    context.url = "https://parabank.parasoft.com/parabank/services/bank"
    context.response = requests.get(context.url)

@when(u'User sends Account ID "15231"')
def step_impl(context):
    payload = {
        "accountId" : "15231"
    }
    account_id = "15231"
    context.response = requests.get(context.url + "/accounts/" + account_id, headers={'Accept': 'application/json'})
    assert context.response.headers['content-type'] == "application/json"


@then(u'User verifies the status code is "200"')
def step_impl(context):
    assert context.response.status_code == 200


@then(u'User verifies "Get Account ID" response contains following information')
def step_impl(context):
    #WIP
    print(context.response.json)
