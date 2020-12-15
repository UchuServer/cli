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