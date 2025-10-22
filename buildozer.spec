[app]
title = Quantum Mobile OS
package.name = quantumos
package.domain = com.quantum

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
