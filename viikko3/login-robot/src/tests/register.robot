*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  miiris  miiris123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  mi  miiris123
    Output Should contain  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  miiris  miiris1
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  miiris  miirisonbest
    Output Should Contain  Password can not only contain letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
