# QUESTION 3: LIST ELEEMENT PRINTING WITH DELAY OF 2 MULTIPLE
import thread
import time

def print_element(threadName, lis):
    """
    printing element of list
    :param threadname: Name of thread
    :param lis: List of element
    :return:
    """
    print("\t\t%s" % (threadName))
    delay = 0
    count = 0
    while count < len(lis):
        print(lis[count])
        delay += 2
        time.sleep(delay)

ele_list = list(input("\nENTER THE ELEMENT OF LIST").strip().split(" "))
# CREATING THREAD FOR PRINTING ELEMENT OF LIST
try:
    thread.start_new_thread(print_element, ("ELEMENT_OF_LIST", ele_list) )

except:
    print("UNABLE TO CREATE THREAD")