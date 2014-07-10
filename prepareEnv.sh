#!/bin/bash
cd ./tests/functional/WPA-EAP
adb push ./gogogo.crt /storage/sdcard0/
adb push ./cacert.crt /storage/sdcard0/
