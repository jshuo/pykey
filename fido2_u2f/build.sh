#!/bin/bash

mkdir -p build/
for py in *.py; do
  if [ $py == "main.py" ] || [ $py == "boot.py" ]; then
    continue
  fi
  ../adapted-circuitpython/mpy-cross/mpy-cross $py
done

python3 utils/make_cheader.py *.mpy main.py boot.py attestation.der

cp fido-drive.h /home/secux/workspace/pykey/adapted-circuitpython/supervisor/shared