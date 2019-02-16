# ACM Fall 2018 Advanced Coding Challenge

This program was submitted for the ACM Fall 2018 Coding Challenge on HackerRank for the advanced division. My team won first place for this division at the University of Colorado: Denver. See the References and Links section for the prompt and more information about the ACM.

Included are two versions of the program. One is the bare version used for competitions submission (original_submission.py), and the other version is the same code with comments and formatting added to enhance readability and explain how the code is working (comments_added.py)

## Advanced - Tournament Bracket Maker

You will create a tournament bracket for a two player game, for example Ping Pong, for a tournament size of N players. Your N is specified in the Input constraint according to your level. In general, the tournament bracket should be intuitive and applicable for a real tournament. Your solution will be for the general case restricted by the number of players entered into your tournament, so you will not use player's names. Instead, you will use P1, P2,... and W1 for Winner of game 1, W2 for Winner of game 2,... and L1 for Loser of game 1, L2 for Loser of game 2,... Games will be specifed as G1 for game 1, G2 for game 2,... In addition to a Winners bracket, you will also need to allow for Losers to get back into the Final game with a separate Losers bracket. You will need to print all rounds from the Winners bracket first. Then you will be able to determine the games and rounds in the Losers bracket accordingly. The overall winners in each bracket will face off in the final game.

#### Input Format

N = number of players, for 2 <= N <= 20

#### Constraints

Ordering rules: You need to order player numbers in a consecutive manner. You need to order the games according to rounds. All game numbers in round 1 < game numbers in round 2, so forth. You will need to print all the games and rounds in the Winners Bracket prior to printing the Losers Bracket. The last game printed will be the Final game between the overall winners of the winner and loser brackets.

If necessary, players do not get a bye week, except for case N = 3, 7, 15. If necessary, you would need to implement prelimnary games for all cases other than N = 3, 7, 15. Hint: Draw out the brackets and you will see for yourself!

NOTE: You are not allowed to create N case statements or N if/else statements. We will check your code submission for hard coded answers! Your submission will not be considered if you hard code your answers.

#### Sample Input 0

    2
    
#### Sample Output 0

    G1: P1 P2
    
#### Sample Input 1

    3
    
#### Sample Output 1

    G1: P1 P2
    G2: W1 P3
    G3: L1 L2
    G4: W2 W3
    
#### Sample Input 2

    4
    
#### Sample Output 2

    G1: P1 P2
    G2: P3 P4
    G3: W1 W2
    G4: L1 L2
    G5: W4 L3
    G6: W3 W5
    
#### Sample Input 3

    5
    
#### Sample Output 3

    G1: P1 P2
    G2: W1 P3
    G3: P4 P5
    G4: W2 W3
    G5: L1 L2
    G6: L3 L4
    G7: W5 W6
    G8: W4 W7
    
#### Sample Input 4

    6
    
#### Sample Output 4

    G1: P1 P2
    G2: P3 P4
    G3: W1 W2
    G4: P5 P6
    G5: W3 W4
    G6: L1 L2
    G7: W6 L3
    G8: L4 L5
    G9: W7 W8
    G10: W5 W9
    
#### Sample Input 5

    7
    
#### Sample Output 5

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: W1 W2
    G5: W3 P7
    G6: W4 W5
    G7: L1 L2
    G8: L3 L4
    G9: W7 W8
    G10: L5 L6
    G11: W9 W10
    G12: W6 W11
    
#### Sample Input 6

    8
    
#### Sample Output 6

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: W1 W2
    G6: W3 W4
    G7: W5 W6
    G8: L1 L2
    G9: L3 L4
    G10: L5 L6
    G11: W8 W9
    G12: W10 L7
    G13: W11 W12
    G14: W7 W13
    
#### Sample Input 7

    9
    
#### Sample Output 7

    G1: P1 P2
    G2: W1 P3
    G3: P4 P5
    G4: P6 P7
    G5: P8 P9
    G6: W2 W3
    G7: W4 W5
    G8: W6 W7
    G9: L1 L2
    G10: L3 L4
    G11: L5 L6
    G12: L7 L8
    G13: W9 W10
    G14: W11 W12
    G15: W13 W14
    G16: W8 W15
    
#### Sample Input 8

    10
    
#### Sample Output 8

    G1: P1 P2
    G2: P3 P4
    G3: W1 W2
    G4: P5 P6
    G5: P7 P8
    G6: P9 P10
    G7: W3 W4
    G8: W5 W6
    G9: W7 W8
    G10: L1 L2
    G11: W10 L3
    G12: L4 L5
    G13: L6 L7
    G14: L8 L9
    G15: W11 W12
    G16: W13 W14
    G17: W15 W16
    G18: W9 W17
    
#### Sample Input 9

    11
    
#### Sample Output 9

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: W1 W2
    G5: W3 P7
    G6: P8 P9
    G7: P10 P11
    G8: W4 W5
    G9: W6 W7
    G10: W8 W9
    G11: L1 L2
    G12: L3 L4
    G13: W11 W12
    G14: L5 L6
    G15: L7 L8
    G16: L9 L10
    G17: W13 W14
    G18: W15 W16
    G19: W17 W18
    G20: W10 W19
    
#### Sample Input 10

    12
    
#### Sample Output 10

     G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: W1 W2
    G6: W3 W4
    G7: P9 P10
    G8: P11 P12
    G9: W5 W6
    G10: W7 W8
    G11: W9 W10
    G12: L1 L2
    G13: L3 L4
    G14: L5 L6
    G15: W12 W13
    G16: W14 L7
    G17: L8 L9
    G18: L10 L11
    G19: W15 W16
    G20: W17 W18
    G21: W19 W20
    G22: W11 W21
    
#### Sample input 11

    13
    
#### Sample Output 11

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: P9 P10
    G6: W1 W2
    G7: W3 W4
    G8: W5 P11
    G9: P12 P13
    G10: W6 W7
    G11: W8 W9
    G12: W10 W11
    G13: L1 L2
    G14: L3 L4
    G15: L5 L6
    G16: L7 L8
    G17: W13 W14
    G18: W15 W16
    G19: L9 L10
    G20: L11 L12
    G21: W17 W18
    G22: W19 W20
    G23: W21 W22
    G24: W12 W23
    
#### Sample input 12

    14
    
#### Sample Output 12

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: P9 P10
    G6: P11 P12
    G7: W1 W2
    G8: W3 W4
    G9: W5 W6
    G10: P13 P14
    G11: W7 W8
    G12: W9 W10
    G13: W11 W12
    G14: L1 L2
    G15: L3 L4
    G16: L5 L6
    G17: L7 L8
    G18: L9 L10
    G19: W14 W15
    G20: W16 W17
    G21: W18 L11
    G22: L12 L13
    G23: W19 W20
    G24: W21 W22
    G25: W23 W24
    G26: W13 W25
    
#### Sample Input 13

    15
    
#### Sample Output 13

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: P9 P10
    G6: P11 P12
    G7: P13 P14
    G8: W1 W2
    G9: W3 W4
    G10: W5 W6
    G11: W7 P15
    G12: W8 W9
    G13: W10 W11
    G14: W12 W13
    G15: L1 L2
    G16: L3 L4
    G17: L5 L6
    G18: L7 L8
    G19: L9 L10
    G20: L11 L12
    G21: W15 W16
    G22: W17 W18
    G23: W19 W20
    G24: L13 L14
    G25: W21 W22
    G26: W23 W24
    G27: W25 W26
    G28: W14 W27
    
#### Sample Input 14

    16
    
#### Sample Output 14

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: P9 P10
    G6: P11 P12
    G7: P13 P14
    G8: P15 P16
    G9: W1 W2
    G10: W3 W4
    G11: W5 W6
    G12: W7 W8
    G13: W9 W10
    G14: W11 W12
    G15: W13 W14
    G16: L1 L2
    G17: L3 L4
    G18: L5 L6
    G19: L7 L8
    G20: L9 L10
    G21: L11 L12
    G22: L13 L14
    G23: W16 W17
    G24: W18 W19
    G25: W20 W21
    G26: W22 L15
    G27: W23 W24
    G28: W25 W26
    G29: W27 W28
    G30: W15 W29
    
#### Sample Input 15

    17
    
#### Sample Output 15

    G1: P1 P2
    G2: W1 P3
    G3: P4 P5
    G4: P6 P7
    G5: P8 P9
    G6: P10 P11
    G7: P12 P13
    G8: P14 P15
    G9: P16 P17
    G10: W2 W3
    G11: W4 W5
    G12: W6 W7
    G13: W8 W9
    G14: W10 W11
    G15: W12 W13
    G16: W14 W15
    G17: L1 L2
    G18: L3 L4
    G19: L5 L6
    G20: L7 L8
    G21: L9 L10
    G22: L11 L12
    G23: L13 L14
    G24: L15 L16
    G25: W17 W18
    G26: W19 W20
    G27: W21 W22
    G28: W23 W24
    G29: W25 W26
    G30: W27 W28
    G31: W29 W30
    G32: W16 W31
    
#### Sample Input 16

    18
    
#### Sample Output 16

    G1: P1 P2
    G2: P3 P4
    G3: W1 W2
    G4: P5 P6
    G5: P7 P8
    G6: P9 P10
    G7: P11 P12
    G8: P13 P14
    G9: P15 P16
    G10: P17 P18
    G11: W3 W4
    G12: W5 W6
    G13: W7 W8
    G14: W9 W10
    G15: W11 W12
    G16: W13 W14
    G17: W15 W16
    G18: L1 L2
    G19: W18 L3
    G20: L4 L5
    G21: L6 L7
    G22: L8 L9
    G23: L10 L11
    G24: L12 L13
    G25: L14 L15
    G26: L16 L17
    G27: W19 W20
    G28: W21 W22
    G29: W23 W24
    G30: W25 W26
    G31: W27 W28
    G32: W29 W30
    G33: W31 W32
    G34: W17 W33
    
#### Sample Input 17

    19
    
#### Sample Output 17

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: W1 W2
    G5: W3 P7
    G6: P8 P9
    G7: P10 P11
    G8: P12 P13
    G9: P14 P15
    G10: P16 P17
    G11: P18 P19
    G12: W4 W5
    G13: W6 W7
    G14: W8 W9
    G15: W10 W11
    G16: W12 W13
    G17: W14 W15
    G18: W16 W17
    G19: L1 L2
    G20: L3 L4
    G21: W19 W20
    G22: L5 L6
    G23: L7 L8
    G24: L9 L10
    G25: L11 L12
    G26: L13 L14
    G27: L15 L16
    G28: L17 L18
    G29: W21 W22
    G30: W23 W24
    G31: W25 W26
    G32: W27 W28
    G33: W29 W30
    G34: W31 W32
    G35: W33 W34
    G36: W18 W35
    
#### Sample Input 18

    20
    
#### Sample Output 18

    G1: P1 P2
    G2: P3 P4
    G3: P5 P6
    G4: P7 P8
    G5: W1 W2
    G6: W3 W4
    G7: P9 P10
    G8: P11 P12
    G9: P13 P14
    G10: P15 P16
    G11: P17 P18
    G12: P19 P20
    G13: W5 W6
    G14: W7 W8
    G15: W9 W10
    G16: W11 W12
    G17: W13 W14
    G18: W15 W16
    G19: W17 W18
    G20: L1 L2
    G21: L3 L4
    G22: L5 L6
    G23: W20 W21
    G24: W22 L7
    G25: L8 L9
    G26: L10 L11
    G27: L12 L13
    G28: L14 L15
    G29: L16 L17
    G30: L18 L19
    G31: W23 W24
    G32: W25 W26
    G33: W27 W28
    G34: W29 W30
    G35: W31 W32
    G36: W33 W34
    G37: W35 W36
    G38: W19 W37

## Additional Links and References

* [ACM Challenge Competition Page](https://www.hackerrank.com/acm-coding-challenge#rules)
* [Link to This Problem](https://www.hackerrank.com/contests/acm-coding-challenge/challenges/advanced-tournament-bracket-maker/problem)
