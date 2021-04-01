# Project_01_CSP_AI

## Student Name

| ID  | Name |
| ------------- | ------------- |
| 1651049  | Chu Đức Khánh  |
| 1651009   | Giảng Thanh Danh |
| 1751062   | Lê Quốc Anh Duy|


## Step
    Install library Pytho
    ```
    python3 -m pip install name_library
    
    ```
    Example: python3 -m pip install z3-solver

## Form to Input.txt

    ```
    SEND + MORE == MONEY
    ```

## Run project

    ```
    python3 main.py
    ```

## Output

    Level 1: Solve the addition equation or subtraction equation with 2 operands.
    ```
    Example Input: SEND + MORE == MONEY

    Output: 
    Given a cryptarithmetic problem: 
    SEND + MORE == MONEY
    Solution: 
    {'SEND': 9567, 'MORE': 1085, 'MONEY': 10652}
    == 1 solutions found in 0.1s ==
    
    ```

    Level 2: Solve the multiplication equation with 2 operands.
    ```

    Example Input: ONE * TWO == THREE

    Output:
    Given a cryptarithmetic problem: 
    ONE * TWO == THREE
    Solution: 
    {'ONE': 105, 'TWO': 831, 'THREE': 87255}
    {'ONE': 105, 'TWO': 371, 'THREE': 38955}
    {'ONE': 104, 'TWO': 361, 'THREE': 37544}
    {'ONE': 105, 'TWO': 271, 'THREE': 28455}
    {'ONE': 104, 'TWO': 861, 'THREE': 89544}
    {'ONE': 108, 'TWO': 461, 'THREE': 49788}
    {'ONE': 104, 'TWO': 561, 'THREE': 58344}
    == 7 solutions found in 25.7s ==

    ```

    Level 3: Solve any kind of equation with multiple operands and single operator (+ - *).

    ```
    Example Input: SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+ THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+ SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+ MAN+TRY+TO+MEET+THE+TEAM+ON+THE+ MOON+AS+HE+HAS+AT+THE+OTHER+TEN == TESTS

    OutPut: 
    Given a cryptarithmetic problem: 
    SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+ THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+ SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+ MAN+TRY+TO+MEET+THE+TEAM+ON+THE+ MOON+AS+HE+HAS+AT+THE+OTHER+TEN == TESTS
    Solution: 
    {'SO': 31, 'MANY': 2764, 'MORE': 2180, 'MEN': 206, 'SEEM': 3002, 'TO': 91, 'SAY': 374, 'THAT': 9579, 'THEY': 9504, 'MAY': 274, 'SOON': 3116, 'TRY': 984, 'STAY': 3974, 'AT': 79, 'HOME': 5120, 'AS': 73, 'SEE': 300, 'OR': 18, 'HEAR': 5078, 'THE': 950, 'SAME': 3720, 'ONE': 160, 'MAN': 276, 'MEET': 2009, 'TEAM': 9072, 'ON': 16, 'MOON': 2116, 'HE': 50, 'HAS': 573, 'OTHER': 19508, 'TEN': 906, 'TESTS': 90393}
    == 1 solutions found in 141.6s ==

    ```

    Level 4: Solve any kind of equation with multiple operands and operators (+ - *).

    ```
    Example Input: SEND+(MORE+MONEY)-OR*DIE == NUOYI

    OutPut: (Run more 2 solutions and 626.1s)
    Given a cryptarithmetic problem: 
    SEND+(MORE+MONEY)-OR*DIE==NUOYI
    Solution: 
    {'SEND': 1264, 'MORE': 8752, 'MONEY': 87623, 'OR': 75, 'DIE': 492, 'NUOYI': 60739}
    {'SEND': 4691, 'MORE': 8726, 'MONEY': 87965, 'OR': 72, 'DIE': 106, 'NUOYI': 93750}
    == 2 solutions found in 626.1s == 
    

    ```
