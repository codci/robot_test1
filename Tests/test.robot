*** Settings ***
Documentation     A test suite with a tests to assert http://httpbin.org/ servises.

Library  ../libraries/RequestDemoLibrary.py
Library  BuiltIn
Library  String
Library  Collections
Suite Setup  Initialize header dictionary

*** Variables ***
${STREAMCOUNT}    7
${STATUSCODE}     200
${AUTH STATUS}    True

*** Test Cases ***
Test request stream
    Request Stream  ${STREAMCOUNT}
    Status Code Should Be  ${STATUSCODE}
    Number Of Lines Should Be  ${STREAMCOUNT}

Test request get
    Request Get  ${HEADERS}
    Status Code Should Be  ${STATUSCODE}
    Header Should Be  ${HEADERS}

Test request auth
    [Template]  auth and check status code
    # name        # pwd     # expected response code     #auth status
    qwe           qwe       200                          True
    asd           asd       200                          True
    ${EMPTY}      pwd       404                          False
    login         ${EMPTY}  404                          False
    ${EMPTY}      ${EMPTY}  404                          False

*** Keywords ***
Number Of Lines Should Be
    [Arguments]  ${expected_stream_lines}
    ${responce text}  Get Response Text
    ${stream_lines}  Get Line Count  ${responce text}
    Should Be Equal As Integers  ${stream_lines}  ${expected_stream_lines}

Status Code Should Be
    [Arguments]  ${expected_response_code}
    ${status}  Get Response Status Code
    Should Be Equal  ${status}  ${expected_response_code}

Header Should Be
    [Arguments]  ${expected_header}
    ${header}  Get Response Header
    Dictionary Should Contain Sub Dictionary  ${header}  ${expected_header}

Auth and check status code
    [Arguments]  ${name}  ${pwd}  ${expected_response_code}  ${auth_status}
    Request Auth  ${name}  ${pwd}
    Status Code Should Be   ${expected_response_code}
    ${auth_status}  Get Response Authorization Status
    Should Be Equal  ${auth_status}  ${auth_status}

Initialize header dictionary
    ${HEADERS}=  Create Dictionary  Test=qwe
    Set Suite Variable  ${HEADERS}