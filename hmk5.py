#exercise 1 
def song(animal, sound):
    print("Let me tell you about Old MacDonald.")
    print("He had a farm, Ee-igh, Ee-igh, Oh!")
    print(f"On that farm, he had a {animal}, Ee-igh, Ee-igh, Oh!")
    print(f"With a {sound} here and a {sound} there.")
    print(f"Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")

# Now, let's sing about five different animals!
song("cow", "moo")
song("pig", "oink")
song("duck", "quack")
song("sheep", "baa")
song("horse", "neigh")


#exercise 2

def calculate_average(num_count):
    total = 0
    for _ in range(num_count):
        number = float(input("Enter a number: "))
        total += number

    return total / num_count

def main():
    count = int(input("How many numbers will you enter? "))
    average = calculate_average(count)
    print(f"The average of the entered numbers is: {average:.2f}")

if __name__ == "__main__":
    main()

#exercise 3

import tkinter as tk
import math

def on_click(event):
    points.append((event.x, event.y))
    if len(points) == 2:
        x1, y1 = points[0]
        x2, y2 = points[1]
        length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
        mid = ((x1 + x2) / 2, (y1 + y2) / 2)

        canvas.create_line(points[0], points[1], fill='black')
        canvas.create_oval(mid[0] - 5, mid[1] - 5, mid[0] + 5, mid[1] + 5, fill='cyan')
        print(f"Length: {length:.2f}, Slope: {slope:.2f}, Midpoint: {mid}")
        points.clear()

points = []
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()
canvas.bind("<Button-1>", on_click)
root.mainloop()


#exercise 4

def calculate_epact(year):
    C = year // 100
    epact = (8 + (C // 4) - C + (80 + 13) // 25 + (11 * (year % 19))) % 30
    return epact

def main():
    year = int(input("Enter a 4-digit year: "))
    epact = calculate_epact(year)
    print(f"The Gregorian epact for the year {year} is: {epact}")

if __name__ == "__main__":
    main()

#exercise 5

def get_some_strings(num_strings):
    return [input("Enter a string: ") for _ in range(num_strings)]

def main():
    count = int(input("How many strings will you enter? "))
    strings = get_some_strings(count)
    print("You entered:", strings)

if __name__ == "__main__":
    main()

