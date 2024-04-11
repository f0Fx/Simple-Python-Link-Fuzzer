import sys
from modules import engine

try:
    URL = sys.argv[1]
except:
    print("Please provide a URL as an argument")
    sys.exit(1)

engine.FuzzLink(URL)