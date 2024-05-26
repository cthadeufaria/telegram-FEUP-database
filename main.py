from database import Database
from bot import Bot

import time



def main():
    database = Database()
    bot = Bot()
    tries = 0

    while True:
        time.sleep(300)
        test, message = database.test_database()

        if test is True:
            bot.send_message(message)

        elif test is False:
            tries += 1

            if tries == 3:
                bot.send_message(message)
                tries = 0



if __name__ == "__main__":
    main()