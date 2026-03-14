[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- NEW FEATURES ---
# Added 'sh' for better shell commands and 'openssl' for secure internet (SSL/HTTPS)
# Added 'kivy==2.3.0' to ensure stability on modern Android
requirements = python3,kivy==2.3.0,plyer,android,requests,pyjnius,sh,openssl

# Permissions for Earbuds, Mic, and the Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Settings for modern Samsung phones
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
# Building for both 64-bit (modern) and 32-bit (older) ensures it works on all Samsung M-series
android.archs = arm64-v8a, armeabi-v7a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# --- IMPROVED SERVICE ---
# Added 'sticky' so Android restarts the service automatically if it ever runs out of RAM
android.services = AranshService:service.py:foreground:sticky

# Visuals
orientation = portrait
android.private_storage = True
# Ensures the screen doesn't flicker during start
android.presplash_color = #FFFFFF 

[buildozer]
# Raised to 2 so we can see exactly what is happening if a crash occurs
log_level = 2
warn_on_root = 1
