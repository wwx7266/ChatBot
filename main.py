# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from LLM.ERNIE.ERNIE import ERNIE


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chat_bot = ERNIE()
    while True:
        message = input("User: ")
        chat_bot.chat(message)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
