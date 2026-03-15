[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- STABLE FEATURES ---
# Added 'android' to requirements; it's often needed for background services.
requirements = python3,kivy==2.3.0,openssl,requests,certifi,plyer,android

android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Assistant trigger setup
android.manifest.intent_filters = intent_filters.xml

# Background Engine
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Level 2 is required to see the exact C-compilation failures
log_level = 2
warn_on_root = 1
