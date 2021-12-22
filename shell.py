from os import system

def inputCommand():
    shell = str(input('>>> '))
    if shell == 'exit' or shell == 'quit':
        exit()

    if shell == 'clear':
        system('clear')

    runCommand(shell)

def runCommand(shell):
    cmd = shell
    system(cmd)

if __name__ == '__main__':
    while True:
        inputCommand()
