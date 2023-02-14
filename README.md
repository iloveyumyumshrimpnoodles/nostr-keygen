# nostr-keygen
A Python3 script to generate Nostr npub/nsec keypairs from a given seed. <br>
Uses HKDF to derive 32 bytes, which are then used to generate a SECP256k1 keypair

# usage
```console
user@hostname:~$ python3 seed.py your passphrase
```

# license
```
This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
```