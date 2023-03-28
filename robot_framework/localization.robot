*** Settings ***
Library  Selenium2Library
Library  Collections
Resource    variables.robot
Resource    keys.robot
Suite Teardown  Close All Browsers


*** Test Cases ***
Localization test
    [Tags]    localization
    Open Browser To Landing Page
    Wait Until Element Is Visible   ${lang_prefix}
    ${tmp}=     Get Text    ${lang_prefix}
    Should Be Equal As Strings  ${tmp}  (EN)
    @{elementList} =   Get WebElements     ${header_links_locator}
    @{textList}=    Create List
    FOR  ${element}  IN  @{elementList}
         ${text}=  Get Text  ${element}
         log to console  Item: ${text}
         Append To List  ${textList}  ${text}
    END
    Lists Should Be Equal   ${header_links_text_list}   ${textList}     ignore_order=True
