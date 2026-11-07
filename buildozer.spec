
[app]

title = Salati
package.name = salati
package.domain = org.salati.app

source.dir = .
source.include_exts = py,png,jpg,kv,mp3,ttf

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,VIBRATE

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 0
