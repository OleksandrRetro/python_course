*** Settings ***
Library  Selenium2Library
Library  Collections
Resource    variables.robot
Resource    keys.robot
Suite Teardown  Close All Browsers


*** Test Cases ***
About test
    [Tags]    about
    Open Browser To Landing Page
    Wait Until Element Is Visible   ${about_locator}
    Click Element    ${about_locator}
    ${current_url}=     Get Location
    log to console  Current URL: ${current_url}
    Should Be Equal   ${current_url}  ${expected_url}
