#QUESTION 1: CREATING THREADING PROCESS AND SLEEPS FOR 5 SECOND
import threading
import time


def threading_process():
    """
    SLEEP FOR 5 SECOND AND PRINT OUT MESSAGE
    :return:
    """
    print(threading.currentThread().getName(), 'THREAD PROCESS STARTING')
    time.sleep(5)
    print("\n AFTER SLEEP FOR 5 SECONDS PROCESS ENDING ")


thread1 = threading.Thread(name="THREAD_1", target=threading_process)
thread1.start()