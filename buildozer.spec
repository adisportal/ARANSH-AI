[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- ALL FEATURES ENABLED ---
# We use the core libraries. Buildozer 1.5.0 will handle 
# hostpython3 and sh automatically to save RAM.
requirements = python3,kivy==2.3.0,plyer,requests,certifi,openssl

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting Samsung M35 (Android 13+)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Focused on Samsung M35 (64-bit architecture)
android.archs = arm64-v8a

# Assistant trigger setup
android.manifest.intent_filters = intent_filters.xml

# Background Engine
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
log_level = 2
warn_on_root = 1
