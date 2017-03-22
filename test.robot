*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library  RequestDemoLibrary.py

*** Variables ***
${STREAMCOUNT}    7
${USERNAME}       200
${PASSWORD}       200
${STATUSCODE}     200
${AUTH STATUS}    True

*** Test Cases ***
Valid Stream
    test request stream

Valid Auth
    test request auth

Valid Get
    test request get

Test auth
    [Template]  auth and check status code
    # name        # pwd    # expected response code
    qwe           qwe      200
    asd           asd      200

*** Keywords ***
Test request auth
    Request Auth  ${USERNAME}   ${PASSWORD}
    Status Code Should Be  ${STATUSCODE}
    Authorization Status Should Be  ${AUTH STATUS}

Test request stream
    Request Stream  ${STREAMCOUNT}
    Status Code Should Be  ${STATUSCODE}
    Number Of Lines Should Be  ${STREAMCOUNT}

Test request get
    Request Get
    Status Code Should Be  ${STATUSCODE}
    ${result} =  Get Response Status Code
    Status Code Should Be  ${result}

Auth and check status code
    [Arguments]  ${name}  ${pwd}  ${expected_response_code}
    Request Auth  ${name}  ${pwd}
    ${status}  Get Response Status Code
    Should Be Equal  ${status}  ${expected_response_code}