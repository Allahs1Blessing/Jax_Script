from time import sleep
from pynput import keyboard
from pyautogui import typewrite, hotkey

n = 0
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='+')}
    ]

current = set()


def execute():
    global n
    while n == 0:

        sleep(1)

        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)
        #btw if you ask yourself why it isn't typewrite("ACTIVE: Jax enters Evasion,"), it's because if I do it like that it cuts out some letters, sometimes.
        typewrite("ACTIVE:")
        typewrite(" Jax enters Evasion,")

        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)
        typewrite("a defensive stance")
        typewrite(", for 2 seconds,")

        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)

        typewrite("causing all non-turret ")
        typewrite(" basic attacks against him to be dodged.")


        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)

        typewrite(" Jax")
        typewrite(" also takes 25% reduced damage")
        typewrite(" from all")
        typewrite(" champion area of effect abilities.")


        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)

        typewrite("Counter Strike")
        typewrite(" can be recast after 1 second.")

        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)

        typewrite(" At the end of the duration,")
        typewrite(" Jax stuns all nearby enemies for 1 second")
        typewrite(" and deals physical damage to them,")


        hotkey('enter')
        sleep(0.10)
        hotkey('enter')
        typewrite("/all ")
        sleep(0.25)

        typewrite("increased by")
        typewrite(" 20% for each attack dodged")
        typewrite(", up to a 100% increase.")
        hotkey('enter')
        sleep(1)

        n = n + 1

        break




def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)



with keyboard.Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join()






