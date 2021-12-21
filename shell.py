from os import system

def inputShell():
    shell = str(input('|-> '))
    if shell == 'exit' or shell == 'quit':
        exit()

    if shell == 'clear':
        system('clear')

    backShell(shell)

def backShell(shell):
    cmd = shell
    system(cmd)

if __name__ == '__main__':
    while True:
        inputShell()