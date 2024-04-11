import requests
import threading

def GetRoutes():
    with open("modules/to_fuzz.txt", "r") as f:
        return f.readlines()
    
def CheckLink(url:str, route:str):
    r = requests.get(url + f"/{route}")
    if r.status_code == 200:
        return print(f"\033[0;32m{route} exists\033[0m")
    print(f"\033[0;31m{route} does not exist\033[0m")

def FuzzLink(url:str):
    # Fuzzing the link
    for route in GetRoutes():
        route = route.strip()
        threading.Thread(target=CheckLink, args=(url, route)).start()
        