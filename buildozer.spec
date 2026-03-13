[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# Added 'android' and 'requests' which you might need for searching
requirements = python3,kivy,plyer,android,requests

# Permissions for Earbuds and Mic
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN

# Targeting modern Samsung devices
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# --- THE MAGIC LINK ---
# This injects your earbud-trigger code into the App Manifest
android.manifest.intent_filters = intent_filters.xml

# Ensure the app doesn't close immediately in the background
android.services = AranshService:service.py

[buildozer]
log_level = 2
warn_on_root = 1
