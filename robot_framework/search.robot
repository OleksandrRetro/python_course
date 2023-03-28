*** Settings ***
Library  Selenium2Library
Library  Collections
Resource    variables.robot
Resource    keys.robot
Suite Teardown  Close All Browsers


*** Test Cases ***
Search test
    [Tags]    search
    Open Browser To Landing Page
    Wait Until Element Is Visible   ${search_button_locator}
    Click Element    ${search_button_locator}
    Wait Until Element Is Visible   ${search_input_locator}
    Input Text      ${search_input_locator}    Python
    Click Element    ${find_button_locator}
    ${tmp}=     Get Text    ${results_count_locator}
    log to console  Results found: ${tmp}
    Run Keyword And Expect Error    ${search_error}  Should Contain  ${tmp}      10
