from time import time, gmtime
currenttime = gmtime(time())
print(f"Today is {currenttime[0]}-{currenttime[1]}-{currenttime[2]} and it is {currenttime[3]}:{currenttime[4]}:{currenttime[5]}.")
