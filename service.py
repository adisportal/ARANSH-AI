from time import sleep
from jnius import autoclass

# This helps the service restart if Android tries to close it
PythonService = autoclass('org.kivy.android.PythonService')
if hasattr(PythonService, 'mService'):
    PythonService.mService.setAutoRestartService(True)

while True:
    # This is where your earbud-listening logic will go
    print("Aransh Service is active...")
    sleep(10) 
