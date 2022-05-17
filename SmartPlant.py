humidite = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
    while True:
        if input.temperature() < 10:
            basic.show_string("Place the plant in a warmer environment")
        break
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.light_level())
    while True:
        if input.light_level() < 120:
            basic.show_string("Plant needs more light!")
        break
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    while True:
        if humidite < 60:
            basic.show_string("Watering the plant")
        break
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_every_interval():
    global humidite
    humidite = randint(0, 100)
    while True:
        if humidite < 60:
            basic.show_string("Pas d'humidite")
        break
loops.every_interval(120000, on_every_interval)
