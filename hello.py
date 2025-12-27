import platform
import os

print("Привет из мира открытого кода!")
print(f"Ты работаешь на: {platform.system()} {platform.release()}")
print(f"Твой юзер: {os.getlogin()}")