[app]

# (String) Title of your application
title = برنامه ساده من

# (String) Package name
package.name = myapp

# (String) Package domain (needed for android)
package.domain = ir.hamid

# (String) Source code where the main.py live
source.dir = .

# (List) Source files to include
source.include_exts = py,png,jpg,kv,atlas,txt,html

# (List) Requirements
requirements = python3,kivy

# (String) Version of your application
version = 1.0.0

# (List) Permissions
android.permissions = INTERNET

# (String) Android API level
android.api = 33

# (String) Android minimum API
android.minapi = 21

# (String) Android NDK version
android.ndk = 25c

# (String) Android SDK version
android.sdk = 33

# (Boolean) If True, then enable internet permission
android.allow_backup = False

# (String) Orientation (portrait, landscape or sensor)
orientation = portrait

# (Boolean) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (String) Path to build artifact storage
warn_on_root = 1
