def on_gesture_shake():
    basic.show_number(randint(1, 6))
    pass

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
