#QUESTION 1: CREATING THREAD PROCESS WHICH PRINT NO FROM 1 TO 10
import threading
import time


def printing():
    """
    PRINTING 1 TO 10 AND WAIT FOR 1 SECONDS
    :return:
    """
    print("\t",threading.currentThread().getName(), "\n")
    count = 1
    while count < 11:
        print(count)
        time.sleep(1)
        count += 1



no_thread = threading.Thread(name="NO_1_TO_10", target=printing)
no_thread.start()