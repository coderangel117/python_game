# just create function who concatenate user input if user write something
def myprint(input):
    if input == "":
        print('No input')
    else:
        print(f"You have write {input}")  # concatenate with f string method
        print("You have write", input)  # easier concatenation method


if __name__ == '__main__':
    inputuser = input('enter something and press enter key \n')  # ask user to write something in console
    myprint(inputuser)  # use function defined before
