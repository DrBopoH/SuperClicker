from rich.console import Console
from threading import Thread
import pyautogui as root
import keyboard

#Variables, other
console = Console() #Coloring the text of lines in the console
cleaner_on = False
click_on = False

#Functions
def console_clear(n): #Removes a given number of console lines
    for _ in range(n):
        print('\033[F\033[K', end='')

def thread_spawner(n): #Spawns the specified number of running threads
    for _ in range(n):
        Thread(target=click_trigger).start()

def ask_n_threads(): #When the program starts, it asks the user for the number of click spam threads running in parallel. If you press enter and the field remains empty (""), then the value will automatically == 1
    number_of = input("Enter the desired number of threads (1 thread = ~9.5 kps, and this increases exponentially with the number of threads): ")
    if number_of != "":
        try:
            if 64 >= int(number_of) > 0:
                thread_n = int(number_of)
                thread_spawner(thread_n)
            else:
                console_clear(4)
                console.print("[red]The number of threads has been exceeded or the value is not natural.\nTry again:[/]")
                ask_n_threads()
        except:
            console_clear(4)
            console.print("[red]The number of threads entered is incorrect.\nTry again:[/]")
            ask_n_threads()
    else:
        thread_spawner(1)

def click_trigger(): #Reacts to pressing the SPACEBAR, the clicker will start working while it is held down
    while(True):
        global click_on
        if click_on:
            root.click()

def on_key_event(e, click_on, cleaner_on): #Checks which key is pressed and sends a signal to the trigger if the spacebar is held down
    if cleaner_on:
        console_clear(1)
    else:
        cleaner_on = True
    print(f"Key {e.name} {'pressed' if e.event_type == keyboard.KEY_DOWN else 'released'}")

    if e.name == "space":
        click_on = True
    else:
        click_on = False

    return click_on, cleaner_on
        
#Core
ask_n_threads() #Program start
keyboard.hook(lambda e: on_key_event(e, click_on, cleaner_on)) #Checks the keys pressed
keyboard.wait('esc') #When pressed, ESC completely turns off the program
