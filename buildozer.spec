[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- ALL FEATURES ENABLED ---
# hostpython3: Fixes memory crashes on GitHub runners
# sh & openssl: Essential for background tasks and secure AI API calls
# kivy, plyer, requests, certifi: The core engine
requirements = python3,kivy,plyer,requests,certifi,hostpython3,sh,openssl

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+ / M35)
android.api = 33
android.minapi = 21
# Locked to the version confirmed by your logs
android.ndk = 25b
android.accept_sdk_license = True

# --- ARCHITECTURE ---
# arm64-v8a is the modern standard for Samsung M-series. 
# Keeping it to one architecture ensures the build finishes successfully.
android.archs = arm64-v8a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh active in the background
# 'sticky' tells Android to restart the service if the phone runs low on RAM
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Level 2 is enabled so we can see the full compilation log
log_level = 2
warn_on_root = 1
