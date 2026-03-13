[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# Added 'android' and 'requests' for assistant functionality
requirements = python3,kivy,plyer,android,requests

# Permissions for Earbuds, Mic, and Foreground Services
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE

android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a

# --- THE ASSISTANT TRIGGER ---
android.manifest.intent_filters = intent_filters.xml

# --- THE BACKGROUND SERVICE ---
# Format: Name:File:Foreground:Sticky
# 'foreground' keeps it alive, 'sticky' restarts it if it crashes.
android.services = AranshService:service.py:foreground:sticky

orientation = portrait
android.private_storage = True

[buildozer]
log_level = 1
warn_on_root = 1
