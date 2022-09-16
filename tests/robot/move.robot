*** Settings ***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***              StartingX   StartingY   Direction   EndingX EndingY MoveCount
Move west to middle of board    0           9           WEST        0       8       2
Move east out of bound          0           9           EAST        0       9       3
Move north out of bound         0           9           NORTH       0       9       4
Move south to middle of board   0           9           SOUTH       1       9       5
Move west out of bound          9           0           WEST        9       0       6
Move east to middle of board    9           0           EAST        9       1       7
Move north to middle of board   9           0           NORTH       8       0       8
Move south out of bound         9           0           SOUTH       9       0       9

*** Keywords ***
Move character
    [Arguments]     ${startingX}       ${startingY}     ${direction}    ${endingX}      ${endingY}    ${move_count}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with    ${startingY}
    Move in direction   ${direction}
    Character xposition should be   ${endingX}
    Character yposition should be   ${endingY}
    Character Move Count should be   ${move_count}