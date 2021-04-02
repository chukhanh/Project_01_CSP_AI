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
    SEND + MORE = MONEY
    ```

## Run project

    ```
    python3 main.py
    ```

## Output

    Level 1: Solve the addition equation or subtraction equation with 2 operands.
    ```
    Example Input: SEND + MORE = MONEY

    Given a cryptarithmetic problem: 
    SEND + MORE = MONEY
    Solution: 
    DEMNORSY = 75160892
    == 1 solutions found in 0.1s ==
    
    ```

    Level 2: Solve the multiplication equation with 2 operands.
    ```

    Example Input: ONE * TWO = THREE

    Given a cryptarithmetic problem: 
    ONE * TWO = THREE
    Solution: 
    EHNORTW = 5701283
    EHNORTW = 4801356
    EHNORTW = 8901746
    EHNORTW = 5801937
    EHNORTW = 5801427
    EHNORTW = 4701536
    EHNORTW = 4901586
    == 7 solutions found in 10.0s ==

    ```

    Level 3: Solve any kind of equation with multiple operands and single operator (+ - *).

    ```
    Example Input: SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+ THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+ SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+ MAN+TRY+TO+MEET+THE+TEAM+ON+THE+ MOON+AS+HE+HAS+AT+THE+OTHER+TEN = TESTS

    OutPut: 
    Given a cryptarithmetic problem: 
    SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+ THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+ SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+ MAN+TRY+TO+MEET+THE+TEAM+ON+THE+ MOON+AS+HE+HAS+AT+THE+OTHER+TEN = TESTS
    Solution: 
    AEHMNORSTY = 7052618394
    == 1 solutions found in 133.8s ==

    ```

    Level 4: Solve any kind of equation with multiple operands and operators (+ - *).

    ```
    Example Input: SEND+(MORE+MONEY)-OR*DIE = NUOYI

    OutPut: (Run more 2 solutions and 933.6)
    Given a cryptarithmetic problem: 
    SEND+(MORE+MONEY)-OR*DIE = NUOYI
    Solution: 
    DEIMNORSUY = 4298675103
    DEIMNORSUY = 2986713504
    == 2 solutions found in 933.6s ==
    

    ```
