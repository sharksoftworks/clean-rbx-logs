import os
import time
import pyperclip

from pystyle import Colors, Colorate

print(Colorate.Horizontal(Colors.blue_to_cyan, "Rbx-Logs Remover", True))
print(Colorate.Horizontal(Colors.blue_to_cyan, "Discord link set to clipboard.", True))
pyperclip.copy("https://discord.gg/426GMS6SMv")
time.sleep(1.5)
os.system("cls")

user = os.getlogin()
storage = f"C:/Users/{user}/Appdata/Local/Roblox/logs"
file = os.listdir(storage)

print(Colorate.Horizontal(Colors.blue_to_cyan, "[shark-rbx] Getting log files...", True))
print(Colorate.Horizontal(Colors.blue_to_cyan, "[shark-rbx] Removing log files...", True))
for files in file:
    try:
        os.remove(file + "/" + files)
    except Exception as e:
        var = e
print(Colorate.Horizontal(Colors.blue_to_cyan, "[shark-rbx] Removed log files...", True))
input(Colorate.Horizontal(Colors.blue_to_cyan, "[shark-rbx] Press any key to exit...", True))
#thx for using this
