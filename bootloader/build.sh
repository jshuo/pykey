make BOARD=pca10056 clean
make BOARD=pca10056 genhex
python3 hexmerge.py _build-pca10056/pca10056_bootloader-fa332bd-dirty-nosd.hex ./lib/softdevice/s140_nrf52_6.1.1/s140_nrf52_6.1.1_softdevice.hex -o pca10056_bootloader.hex