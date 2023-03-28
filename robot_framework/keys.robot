*** Settings ***
Library  Selenium2Library
Library  Collections
Resource    variables.robot


*** Keywords ***
Open Browser To Landing Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    EPAM | Software Engineering & Product Development Services
