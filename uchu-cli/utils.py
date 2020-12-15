import requests
from commands import CommandList, HelpList, ArgsList

def WorkOutLargestCommand() -> int:
    return 30

def GetArgs(Command: str) -> str:
    Return: str = ""
    if ArgsList[Command][0] == "": return Return
    for x in ArgsList[Command]:
        Return += "[" + x + "] "
    return Return

def Help() -> None:
    print("Uchu CLI: ", end="\n\n")
    print("\tuchu-cli [IP] [Port] [Subcommand]", end="\n\n")
    print("Subcommands: ", end="\n\n")
    i: int = 0
    Largest: int = WorkOutLargestCommand()
    for x in CommandList:
        print("\t" + x, end="") # Print Commands
        print(" " + GetArgs(x), end="") # Print Args
        print(" "*(Largest-(len(x) + 1 + len(GetArgs(x)))), end="") # Print Gap
        print(" - " + HelpList[x]) # Print Help List

    print("")

def CheckNetworkConnection(IP: str, Port: int) -> None:
    try:
        r = requests.get("http://" + IP + ":" + str(Port) + "/")
        if r.status_code != 200:
            exit()
    except:
        print("Couldn't connect to master server")
        exit()