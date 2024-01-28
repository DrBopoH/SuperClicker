from rich.console import Console
from threading import Thread
import pyautogui as root
from time import sleep
import keyboard

console = Console()
root.FAILSAFE = False
flows_index = 1
delete = False
def flow_index():
    global flows_index
    Index = input("Введите желаемое количество потоков(1 поток = 9.5 кпс): ")

    if Index != "":
        try:
            if 64 >= int(Index) > 0:
                flows_index = int(Index)
            else:
                print('\033[F\033[K', end='')
                print('\033[F\033[K', end='')
                print('\033[F\033[K', end='')
                print('\033[F\033[K', end='')
                console.print("[red]Количество потоков превышено или значение не натуральное.\nПопробуйте еще раз:[/]")
                flow_index()
        except:
            print('\033[F\033[K', end='')
            print('\033[F\033[K', end='')
            print('\033[F\033[K', end='')
            print('\033[F\033[K', end='')
            console.print("[red]Количество потоков введено не корректно.\nПопробуйте еще раз:[/]")
            flow_index()

def clicked():
    root.click()

flow_index()

def on_key_event(e):
    global delete
    if delete:
        print('\033[F\033[K', end='')
        print(f"Key {e.name} {'pressed' if e.event_type == keyboard.KEY_DOWN else 'released'}")
    else:
        print(f"Key {e.name} {'pressed' if e.event_type == keyboard.KEY_DOWN else 'released'}")
        delete = True

    if e.name == "space":
        for l in range(flows_index):
            Thread(target=clicked).start()

keyboard.hook(on_key_event)
keyboard.wait('esc')