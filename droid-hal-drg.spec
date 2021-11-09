# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device DRG
%define vendor nokia

%define rpm_device drg
%define rpm_vendor nokia

%define vendor_pretty Nokia
%define device_pretty 6.1 Plus

%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/bt_firmware\
/bugreports\
/cache\
/d\
/dsp\
/firmware\
/persist\
/product\
/sdcard\
/system_ext\
/verity_key\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

