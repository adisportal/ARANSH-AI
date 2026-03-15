[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# --- STABLE REQUIREMENTS ---
# We removed 'hostpython3' and 'sh' from the list.
# Buildozer's engine (p4a) will add them as hidden dependencies.
# This prevents the memory overload that causes "Broken Pipe".
requirements = python3,kivy==2.3.0,plyer,requests,certifi,openssl

android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE, WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Focused on Samsung M35
android.archs = arm64-v8a

android.manifest.intent_filters = intent_filters.xml
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True
android.presplash_color = #FFFFFF 

[buildozer]
log_level = 2
warn_on_root = 1
