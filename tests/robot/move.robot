*** Settings ***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***              StartingX   StartingY   Direction   EndingX EndingY
Move west to middle of board    0           9           WEST        0       8
Move east out of bound          0           9           EAST        0       9
Move north out of bound         0           9           NORTH       0       9
Move south to middle of board   0           9           SOUTH       1       9
Move west out of bound          9           0           WEST        9       0
Move east to middle of board    9           0           EAST        9       1
Move north to middle of board   9           0           NORTH       8       0
Move south out of bound         9           0           SOUTH       9       0

*** Keywords ***
Move character
    [Arguments]     ${startingX}       ${startingY}     ${direction}    ${endingX}      ${endingY}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with    ${startingY}
    Move in direction   ${direction}
    Character xposition should be   ${endingX}
    Character yposition should be   ${endingY}