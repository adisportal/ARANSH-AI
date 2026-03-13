[app]
title = Aransh AI
package.name = aranshai
package.domain = org.aransh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# These are the engine parts of your app
requirements = python3,kivy,plyer,android,requests,pyjnius

# Permissions for Earbuds, Mic, and the Background Service
android.permissions = RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, INTERNET, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, FOREGROUND_SERVICE

# Settings for modern Samsung phones
android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# Link to your assistant trigger file
android.manifest.intent_filters = intent_filters.xml

# THE SERVICE: This tells Android Aransh is always on duty
android.services = AranshService:service.py:foreground

orientation = portrait
android.private_storage = True

[buildozer]
log_level = 1
warn_on_root = 1
