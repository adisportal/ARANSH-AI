[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- STABILITY UPDATES ---
# 1. Added hostpython3: This is the 'magic' fix for memory crashes on GitHub.
# 2. Removed version lock on Kivy: Lets Buildozer pick the most compatible local version.
requirements = python3,kivy,plyer,requests,certifi,hostpython3

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+)
android.api = 33
android.minapi = 21
# Matches the recommended version from your log
android.ndk = 25b
android.accept_sdk_license = True

# --- ARCHITECTURE ---
# Building only for arm64-v8a (Samsung M35) to save 50% build time and RAM.
android.archs = arm64-v8a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh alive in the background
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Level 2 is vital so we can see the exact line if a C-compilation fails.
log_level = 2
warn_on_root = 1
