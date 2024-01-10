import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_full_snowflake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

def main():
    # Введення рівня рекурсії від користувача
    order = int(input("Введіть рівень рекурсії (ціле число): "))

    # Створення вікна для малювання
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Створення черепашки
    fractal_turtle = turtle.Turtle()
    fractal_turtle.shape("classic")
    fractal_turtle.color("blue")
    fractal_turtle.speed(2)

    # Позиціонуємо черепашку відповідно до рівня рекурсії
    fractal_turtle.penup()
    fractal_turtle.goto(-150, -150)
    fractal_turtle.pendown()

    # Викликаємо функцію для малювання повної сніжинки Коха
    draw_full_snowflake(fractal_turtle, order, 300)

    # Закриваємо вікно при кліку
    screen.exitonclick()

if __name__ == "__main__":
    main()