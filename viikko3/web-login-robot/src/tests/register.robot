*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  miiris
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  miiris
    Set Password  word1
    Set Password Confirmation  word1
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long


Register With Nonmatching Password And Password Confirmation
    Set Username  miiris
    Set Password  password123
    Set Password Confirmation  password12
    Submit Credentials
    Register Should Fail With Message  Password confirmation does not match

Login After Successful Registration
    Set Username  mirelle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  mirelle
    Set Password  salasana123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  mii
    Set Password  salasana124
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Password confirmation does not match
    Go To Login Page
    Set Username  mii
    Set Password  salasana124
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password
    


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}