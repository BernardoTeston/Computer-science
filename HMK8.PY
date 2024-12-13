'''
1--
Definite Loop vs. Indefinite Loop
A definite loop executes a known number of times, often implemented with a `for` loop, like iterating through a list. In contrast, an indefinite loop runs an unspecified number of times, continuing until a certain condition is met, typically using a `while` loop. For example, a definite loop could process each item in a fixed-size array, while an indefinite loop might keep asking for user input until a valid entry is received.

For Loop vs. While Loop
The for loop iterates over a sequence (e.g., a list or a range) with a set number of iterations, making it ideal for scenarios where the count is predetermined. On the other hand, the while loop continues to execute as long as a specified condition remains true, which can lead to potential infinite loops if the condition never changes. For instance, a for loop can sum a list of numbers, while a while loop can repeatedly request user input until the user opts to quit.

Interactive Loop vs. Sentinel Loop
An interactive loop prompts the user for input continuously, requiring user engagement to control its duration. In contrast, a sentinel loop operates until a specific value, known as the sentinel, is encountered, signaling the loop to terminate. For example, an interactive loop might ask for names until the user types "exit," while a sentinel loop would read numbers until a user inputs `-1` to stop.

Sentinel Loop vs. End-of-File Loop
A sentinel loop uses a predefined value to indicate when to stop executing, making it reliant on user input to determine its end. In comparison, an end-of-file loop reads input from a file until the end is reached, which signals that no more data is available to process. For instance, a sentinel loop could continue collecting grades until the user enters `-1`, whereas an end-of-file loop would read lines from a text file until it reaches the final line.

2--

Truth Table

| P | Q | R | P and Q | not (P and Q) | not P | not Q | (not P) and Q | (not P) or (not Q) | P and Q or R | (P or R) and (Q or R) |
|---|---|---|---------|----------------|-------|-------|----------------|---------------------|---------------|-----------------------|
| T | T | T |    T    |        F       |   F   |   F   |       F        |          F          |       T       |           T           |
| T | T | F |    T    |        F       |   F   |   F   |       F        |          F          |       T       |           T           |
| T | F | T |    F    |        T       |   F   |   T   |       F        |          T          |       T       |           T           |
| T | F | F |    F    |        T       |   F   |   T   |       F        |          T          |       F       |           F           |
| F | T | T |    F    |        T       |   T   |   F   |       T        |          T          |       T       |           T           |
| F | T | F |    F    |        T       |   T   |   F   |       T        |          T          |       F       |           F           |
| F | F | T |    F    |        T       |   T   |   T   |       F        |          T          |       T       |           T           |
| F | F | F |    F    |        T       |   T   |   T   |       F        |          T          |       F       |           F           |

 Explanation of Columns:
- P, Q, R: Possible values (True or False) for inputs \( P \), \( Q \), and \( R \).
- P and Q: Result of the AND operation between \( P \) and \( Q \).
- not (P and Q): Negation of the AND result.
- not P: Negation of \( P \).
- not Q: Negation of \( Q \).
- (not P) and Q: Result of the AND operation between \( not P \) and \( Q \).
- (not P) or (not Q): Result of the OR operation between \( not P \) and \( not Q \).
- P and Q or R: Result of the OR operation between \( P \) AND \( Q \) and \( R \).
- (P or R) and (Q or R): Result of the AND operation between \( (P or R) \) and \( (Q or R) \).
'''
#3--
#A--
n = int(input("Enter a positive integer n: "))
sum_counting_numbers = 0
i = 1

while i <= n:
    sum_counting_numbers += i
    i += 1

print("Sum of the first", n, "counting numbers is:", sum_counting_numbers)

#C--
sum_user_numbers = 0
number = 0

while number != 999:
    number = int(input("Enter a number (999 to stop): "))
    if number != 999:  # Ensure 999 is not included in the sum
        sum_user_numbers += number

print("Sum of the entered numbers is:", sum_user_numbers)


#4--

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter the position n to find the nth Fibonacci number: "))
result = fibonacci(n)

print(f"The {n}th Fibonacci number is: {result}")

#5--

def syracuse_sequence(start):
    sequence = []  
    x = start      

    while x != 1:
        sequence.append(x) 
        if x % 2 == 0:      
            x //= 2        
        else:               
            x = 3 * x + 1   

    sequence.append(1) 
    return sequence

start_value = int(input("Enter a natural number to start the Syracuse sequence: "))
if start_value > 0:
    result = syracuse_sequence(start_value)
    print("Syracuse sequence starting from", start_value, "is:", result)
else:
    print("Please enter a natural number greater than 0.")