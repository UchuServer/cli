import sys
import json
import requests
from setuptools import Command

CommandList: list[str] = [
    "shutdown",
    "shutdown-world",
    "list",
    "start"
]

def Help() -> None:
    print("Uchu CLI: ", end="\n\n")
    print("\tuchu-cli [IP] [Port] [Subcommand]", end="\n\n")
    print("Subcommands: ", end="\n\n")
    print("\tshutdown                   - Shutsdown all worlds")
    print("\tshutdown-world [GUID/Port] - Shutsdown specific world")
    print("\tlist                       - Lists all active servers")
    print("\tstart [WorldID]            - Start a new world server")

    print("")

def GetWorldName(WorldID) -> str: # I am so so sorry that I have to do it like this, you can't include resources in a PyPi package so no CDClient to get the names from
    if WorldID == "1000":
        return "Venture Explorer"
    elif WorldID == "1001":
        return "Return to Venture Explorer"
    elif WorldID == "1100":
        return "Avant Gardens"
    elif WorldID == "1101":
        return "Avant Gardens Survival"
    elif WorldID == "1102":
        return "Spider Queen Battle"
    elif WorldID == "1150":
        return "Block Yard"
    elif WorldID == "1151":
        return "Avant Grove"
    elif WorldID == "1200":
        return "Nimbus Station"
    elif WorldID == "1201":
        return "Pet Cove"
    elif WorldID == "1202":
        return "NS Shooting Gallery"
    elif WorldID == "1203":
        return "Vertigo Loop Racetrack"
    elif WorldID == "1204":
        return "The Battle of Nimbus Station"
    elif WorldID == "1250":
        return "Nimbus Rock"
    elif WorldID == "1251":
        return "Nimbus Isle"
    elif WorldID == "1252":
        return "Nimbus Station Large Property"
    elif WorldID == "1300":
        return "Gnarled Forest"
    elif WorldID == "1301":
        return "Gnarled Forest Survival"
    elif WorldID == "1302":
        return "Cannon Cove Shooting Gallery"
    elif WorldID == "1303":
        return "Keelhaul Canyon Racetrack"
    elif WorldID == "1350":
        return "Chantey Shanty"
    elif WorldID == "1400":
        return "Forbidden Valley"
    elif WorldID == "1401":
        return "Forbidden Valley Siege"
    elif WorldID == "1402":
        return "Forbidden Valley Dragon Battle"
    elif WorldID == "1403":
        return "Dragonmaw Chasm Racetrack"
    elif WorldID == "1450":
        return "Raven Bluff"
    elif WorldID == "1452":
        return "Craggle Rock"
    elif WorldID == "1500":
        return "LUP Station"
    elif WorldID == "1600":
        return "Starbase 3001"
    elif WorldID == "1601":
        return "Deep Freeze"
    elif WorldID == "1602":
        return "Robot City"
    elif WorldID == "1603":
        return "Moon Base"
    elif WorldID == "1604":
        return "Portabello"
    elif WorldID == "1700":
        return "LEGO Club"
    elif WorldID == "1800":
        return "Crux Prime"
    elif WorldID == "1801":
        return "Nexus Tower Battlefield Crater"
    elif WorldID == "1900":
        return "Nexus Tower"
    elif WorldID == "2000":
        return "Ninjago Monastery"
    elif WorldID == "2001":
        return "Battle Against Frakjaw"
    else:
        return "Unknown"

def CheckNetworkConnection(IP: str, Port: int) -> None:
    try:
        r = requests.get("http://" + IP + ":" + str(Port) + "/")
        if r.status_code != 200:
            exit()
    except:
        print("Couldn't connect to master server")
        exit()

if __name__ == "__main__":
    if not len(sys.argv) >= 4:
        Help()
    else:
        IP: str = sys.argv[1]
        Port: int = int(sys.argv[2])
        CheckNetworkConnection(IP, Port)
        Subcommand: str = sys.argv[3]
        SubcommandArgs: list[str] = list()
        
        i: int = 0
        for x in range(len(sys.argv) - 4):
            SubcommandArgs.append(sys.argv[4 + i])
            i += 1

        if Subcommand not in CommandList: 
            Help()
            exit()

        if Subcommand == "list":
            r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
            json = json.loads(r.text)
            if json["Success"]:
                if len(json["Instances"]) >= 1:
                    print("Instances: (Name - GUID - Port)", end="\n\n")
                    for item in json["Instances"]:
                        Name: str
                        if item["Type"] == 0:
                            Name = "Authentication"
                        elif item["Type"] == 1:
                            Name = "Character"
                        else:
                            Name = GetWorldName(str(item["Zones"][0]))
                            
                        print(Name + " "*(30-len(Name)) + " - " + item["Id"] + " - " + str(item["Port"]))
                else:
                    print("No instances are open")
                    exit()
            else:
                print("List request failed")

        elif Subcommand == "shutdown":
            r = requests.get("http://" + IP + ":" + str(Port) + "/instance/list")
            jsonData = json.loads(r.text)
            if jsonData["Success"]:
                for item in jsonData["Instances"]:
                    if item["Type"] != 0 and item["Type"] != 1:
                        print("Shutting down " + GetWorldName(str(item["Zones"][0])))
                        r2 = requests.get("http://" + IP + ":" + str(Port) + "/instance/decommission?" + item["Id"])
                        if r.status_code != 200 or not json.loads(r2.text)["Success"]:
                            print("Failed to close " + GetWorldName(str(item["Zones"][0])))
            else:
                print("Listing all servers for shutdown failed")
            exit()

        elif Subcommand == "shutdown-world":
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
                                Name = GetWorldName(str(item["Zones"][0]))
                            r2 = requests.get("http://" + IP + ":" + str(Port) + "/instance/decommission?" + item["Id"])
                            if r.status_code != 200:
                                print("Failed to close " + "/" + str(SubcommandArgs[0]))
                            print("Closed " + Name + ":" + str(item["Port"]))
                            Found = True
                else:
                    print("Listing all servers for shutdown-world failed")
            else:
                Help()

            if not Found:
                Help()

            exit()
        elif Subcommand == "start":
            if len(SubcommandArgs) >= 1:
                r = requests.get("http://" + IP + ":" + str(Port) + "/instance/commission?" + SubcommandArgs[0])
                if r.status_code != 200:
                    print("Failed to start " + GetWorldName(str(SubcommandArgs[0])))
                else:
                    print("Started world " + GetWorldName(str(SubcommandArgs[0])))
            else:
                Help()

            exit()