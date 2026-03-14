[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- FIXED REQUIREMENTS ---
# Removed 'android' and 'pyjnius' to prevent the toolchain conflict
# Added 'certifi' for secure SSL/HTTPS connections
requirements = python3,kivy==2.3.0,plyer,requests,certifi,openssl,sh

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+)
android.api = 33
android.minapi = 21
# Matches the recommended version from your log
android.ndk = 25b
android.accept_sdk_license = True
# Builds for both 64-bit and 32-bit Samsung processors
android.archs = arm64-v8a, armeabi-v7a

# Link to your earbud trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh alive in the background
# 'sticky' ensures it restarts if Android kills it for RAM
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Kept at 2 so we can see the exact line if a compilation error occurs
log_level = 2
warn_on_root = 1
