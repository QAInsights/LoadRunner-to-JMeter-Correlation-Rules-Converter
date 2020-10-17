from colorit import *

def print_message(message, message_color):
    """
    Prints message in a given color
    """
    if message_color == 'red':
        print(color(f"{message}", Colors.red))
    elif message_color == 'green':
        print(color(f"{message}", Colors.green))