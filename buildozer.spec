[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- LIGHTWEIGHT REQUIREMENTS ---
# Removed 'sh' and 'openssl' as they often cause the 'Broken pipe' error on GitHub
# Buildozer includes 'android' and 'pyjnius' automatically, so we keep it clean
requirements = python3,kivy==2.3.0,plyer,requests,certifi

# Permissions for Earbuds, Mic, and Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

# Targeting modern Samsung (Android 13+)
android.api = 33
android.minapi = 21
# Matches the recommended version from your previous successful log steps
android.ndk = 25b
android.accept_sdk_license = True

# --- FOCUS ON YOUR PHONE ---
# Building ONLY for arm64-v8a (Samsung M35) makes the build 2x faster and much more stable
android.archs = arm64-v8a

# Link to your earbud trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: Keeps Aransh alive in the background
# 'sticky' ensures it restarts if Android kills it for RAM
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
# Level 2 is required to see the real error hidden behind the 'Broken pipe'
log_level = 2
warn_on_root = 1
