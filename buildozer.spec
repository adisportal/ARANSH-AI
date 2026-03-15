[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- ALL FEATURES ENABLED (FIXED) ---
# Added sh, openssl, and hostpython3 as promised.
# This allows for secure AI calls and background shell commands.
requirements = python3,kivy,plyer,requests,certifi,hostpython3,sh,openssl

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+ / M35)
android.api = 33
android.minapi = 21
# Locked to 25b as per your build logs
android.ndk = 25b
android.accept_sdk_license = True

# --- ARCHITECTURE ---
# arm64-v8a is for your Samsung M35. 
# Keeping it to one arch prevents the "Broken Pipe" crash.
android.archs = arm64-v8a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh alive in the background
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
log_level = 2
warn_on_root = 1
