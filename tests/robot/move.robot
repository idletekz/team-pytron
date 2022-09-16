*** Settings ***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***              StartingX   StartingY   Direction   StartMoveCount EndingX EndingY EndMoveCount
Move west to middle of board    0           9           WEST        1              0       8       2
Move east out of bound          0           9           EAST        17             0       9       18
Move north out of bound         0           9           NORTH       13             0       9       14
Move south to middle of board   0           9           SOUTH       11             1       9       12
Move west out of bound          9           0           WEST        33             9       0       34
Move east to middle of board    9           0           EAST        77             9       1       78
Move north to middle of board   9           0           NORTH       81             8       0       82
Move south out of bound         9           0           SOUTH       23             9       0       24

*** Keywords ***
Move character
    [Arguments]     ${startingX}       ${startingY}     ${direction}    ${start_move_count}    ${endingX}      ${endingY}    ${end_move_count}
    Initialize character xposition with     ${startingX}
    Initialize character yposition with    ${startingY}
    Initialize character move count with     ${start_move_count}
    Move in direction   ${direction}
    Character xposition should be   ${endingX}
    Character yposition should be   ${endingY}
    Character Move Count should be   ${end_move_count}