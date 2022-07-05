#!/bin/bash

# # Copyright (c) 2018 makerdiary
# # All rights reserved.
# # 
# # Redistribution and use in source and binary forms, with or without
# # modification, are permitted provided that the following conditions are
# # met:
# #
# # * Redistributions of source code must retain the above copyright
# #   notice, this list of conditions and the following disclaimer.
# #
# # * Redistributions in binary form must reproduce the above
# #   copyright notice, this list of conditions and the following
# #   disclaimer in the documentation and/or other materials provided
# #   with the distribution.

# # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# # "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# # LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# # A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# # OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# # SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# # LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# # DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# # THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# # OF THIS SOFTWARE, EVEN IF ADVISED OFgenerate-certs.sh THE POSSIBILITY OF SUCH DAMAGE.



# set -e
# set -o pipefail

# # Check prerequisites
# for command in openssl python; do
#   if ! which "$command" >/dev/null 2>&1; then
#     echo "Not find command: $command" >&2
#     echo "Please install the corresponding package." >&2
#     exit 1
#   fi
# done
# for openssl_subcommand in ecparam req x509; do
#   openssl help &> /tmp/.generate_certs
#   if ! grep -q $openssl_subcommand /tmp/.generate_certs; then
#     echo "OpenSSL does not support the \"$openssl_subcommand\" command." >&2
#     echo "Please compile a full-featured version of OpenSSL." >&2
#     rm -f /tmp/.generate_certs
#     exit 1
#   fi
# done

# # Change to certs directory
# workdir="../rsa-keys"
# cd "$workdir"

# # # Generate CA key and certificate
# # openssl genrsa -out rsa-priv.key 2048 
# # # openssl genrsa 2048 -out rsa-priv.pem
# # openssl rsa -in rsa-priv.key -outform PEM -pubout -out public.pem
# # openssl rsa -in rsa-priv.key -out pub.der -outform DER -pubout
# # openssl rsa -pubin -in public.pem -text -noout
# openssl genrsa -out image_sign.pem 2048
# openssl rsa -in image_sign.pem -pubout -out image_sign_pub.der -outform DER -RSAPublicKey_out

# python ../tools/rsa2array.py image_sign.pem image_sign_pub.der 
from Crypto.PublicKey import RSA
keyPair = RSA.generate(2048)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

msg = b'A message for signing'
from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)