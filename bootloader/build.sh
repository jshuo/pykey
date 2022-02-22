make BOARD=pca10059 clean
make BOARD=pca10059 genhex
python3 hexmerge.py _build-pca10059/pca10059_bootloader-06388b7-dirty-nosd.hex ./lib/softdevice/s140_nrf52_6.1.1/s140_nrf52_6.1.1_softdevice.hex -o pca10059_bootloader.hex