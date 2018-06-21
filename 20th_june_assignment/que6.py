# USER DEFINED EXCEPTION

class AgeTooSmallError(Exception):
    """
    RAISED WHEN INPUT AGE IS LESS THEN 18 (AGE<18)
    """
    pass

while True:
    try:
        age = int(input("Enter the age"))
        if age < 18:
            raise AgeTooSmallError

        break
    except AgeTooSmallError:
        print(" You enter age smaller than 18\n")

print("Now your age is appropriate for voting")