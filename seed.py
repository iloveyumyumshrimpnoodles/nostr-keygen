"""
This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
"""

import sys

from nostr.key import PrivateKey

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

if len(sys.argv) == 1:
    sys.exit(f"usage: python3 {sys.argv[0]} your seed")

seed = " ".join(sys.argv[1:])

hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=None,
)

raw_bytes = hkdf.derive(seed.encode())

privkey = PrivateKey(raw_bytes)
pubkey = privkey.public_key

print(f"Seed: {seed}")

print("\n---- Private Key ----")
print(f"Bech32: {privkey.bech32()}")
print(f"Hex: {privkey.hex()}")

print("\n---- Public Key ----")
print(f"Bech32: {pubkey.bech32()}")
print(f"Hex: {pubkey.hex()}")