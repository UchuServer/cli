import sys
import json
import requests
from typing import List

# PyLance doesn't like these imports for some reason
# But Jedi does :tada:
from . import worlds, commands, utils

@commands.RegisterCommand(command="broadcast", help="Send an announcement to all players", arguments=["title", "message"])
def Broadcast(SubCommand, SubcommandArgs):
    r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
    jsonData = json.loads(r.text)

    if jsonData["Success"]:
        for item in jsonData["Instances"]:
            r2 = requests.get("http://" + IP + ":" + str(item["ApiPort"]) + "/world/announce?title=" + SubcommandArgs[0] + "&message=" + SubcommandArgs[1])
            if r2.status_code != 200:
                print("Failed to announce at " + worlds.GetWorldName(str(item["Zones"][0])))
    else:
        print("Listing all servers for broadcasting failed")
    exit()

@commands.RegisterCommand(command="shutdown", help="Shutsdown all worlds", arguments=[""])
def Shutdown(SubCommand, SubcommandArgs):
    r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
    jsonData = json.loads(r.text)

    if jsonData["Success"]:
        for item in jsonData["Instances"]:
            if item["Type"] != 0 and item["Type"] != 1:
                print("Shutting down " + worlds.GetWorldName(str(item["Zones"][0])))
                r2 = requests.get("http://" + IP + ":" + str(Port) + "/instance/decommission?" + item["Id"])
                
                if r2.status_code != 200:
                    print("Failed to close " + worlds.GetWorldName(str(item["Zones"][0])))
    else:
        print("Listing all servers for shutdown failed")
    exit()
    
    
@commands.RegisterCommand(command="shutdown-world", help="Shutsdown specific world", arguments=["GUID/Port"]) 
def ShutdownWorld(SubCommand, SubcommandArgs):
    Found: bool = False
    if len(SubcommandArgs) >= 1:
        r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
        jsonData = json.loads(r.text)
        if jsonData["Success"]:
            for item in jsonData["Instances"]:
                if item["Id"] == SubcommandArgs[0] or str(item["Port"]) == SubcommandArgs[0]:
                    Name: str
                    if item["Type"] == 0:
                        Name = "Authentication"
                    elif item["Type"] == 1:
                        Name = "Character"
                    else:
                        Name = worlds.GetWorldName(str(item["Zones"][0]))

                    r2 = requests.get("http://" + IP + ":" + str(Port) + "/instance/decommission?" + item["Id"])
                    
                    if r2.status_code != 200:
                        print("Failed to close " + "/" + str(SubcommandArgs[0]))

                    print("Closed " + Name + ":" + str(item["Port"]))
                    Found = True
        else:
            print("Listing all servers for shutdown-world failed")

    if not Found:
        utils.Help()

    exit()

@commands.RegisterCommand(command="start", help="Start a new world server", arguments=["WorldID"])
def Start(SubCommand, SubcommandArgs):
    if len(SubcommandArgs) >= 1:
        r = requests.get("http://" + IP + ":" + str(Port) + "/instance/commission?" + SubcommandArgs[0])
        if r.status_code != 200:
            print("Failed to start " + worlds.GetWorldName(str(SubcommandArgs[0])))
        else:
            print("Started world " + worlds.GetWorldName(str(SubcommandArgs[0])))
    else:
        utils.Help()

    exit()

@commands.RegisterCommand(command="list", help="Lists all active servers", arguments=[""])
def List(SubCommand, SubcommandArgs):
    r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
    jsonData = json.loads(r.text)
    
    if jsonData["Success"]:
        if len(jsonData["Instances"]) >= 1:
            print("Instances: (Name - GUID - Port)", end="\n\n")
            for item in jsonData["Instances"]:
                Name: str

                if item["Type"] == 0:
                    Name = "Authentication"
                elif item["Type"] == 1:
                    Name = "Character"
                else:
                    Name = worlds.GetWorldName(str(item["Zones"][0]))
                    
                print(Name + " "*(30-len(Name)) + " - " + item["Id"] + " - " + str(item["Port"]))
        else:
            print("No instances are open")
            exit()
    else:
        print("List request failed")

##################################################################################################

if not len(sys.argv) >= 4:
    utils.Help()

IP: str = sys.argv[1]
Port: int = int(sys.argv[2])
utils.CheckNetworkConnection(IP, Port)
Subcommand: str = sys.argv[3]
SubcommandArgs = []

i: int = 0
for x in range(len(sys.argv) - 4):
    SubcommandArgs.append(sys.argv[4 + i])
    i += 1

if Subcommand not in commands.CommandList: 
    utils.Help()

if commands.ArgsList[Subcommand][0] != "":
    if len(SubcommandArgs) != len(commands.ArgsList[Subcommand]): 
        utils.Help()

commands.CommandFunction[Subcommand](Subcommand, SubcommandArgs)


