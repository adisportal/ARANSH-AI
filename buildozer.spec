[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- ALL FEATURES ENABLED ---
# Requirements optimized for Ubuntu 22.04 stability.
# Openssl and Certifi remain for secure AI/HTTPS web calls.
requirements = python3,kivy==2.3.0,plyer,requests,certifi,openssl

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+ / M35)
android.api = 33
android.minapi = 21
# Locked to 25b as per your successful path logs
android.ndk = 25b
android.accept_sdk_license = True

# Focused on Samsung M35 (64-bit)
android.archs = arm64-v8a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh alive in the background
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Level 2 ensures we see any hidden C-compilation errors
log_level = 2
warn_on_root = 1
