# pip install ecdsa 

from ecdsa import VerifyingKey, SECP256k1 
import binascii 

def get_coordinates_from_pubkey(pubkey_hex): 
    # Convert HEX to bytes 
    pubkey_bytes = binascii.unhexlify(pubkey_hex) 
    
    # Create a VerifyingKey object from the public key 
    vk = VerifyingKey.from_string(pubkey_bytes, curve=SECP256k1) 
    
    # Get the Gx and Gy coordinates 
    Gx = vk.pubkey.point.x() 
    Gy = vk.pubkey.point.y() 
    
    # Convert the coordinates to HEX format 
    Gx_hex = format(Gx, 'x').zfill(64) # Fill with zeros up to 64 characters 
    Gy_hex = format(Gy, 'x').zfill(64) # Fill with zeros up to 64 characters 
    
    return Gx_hex, Gy_hex 

pubkeyhex = "030f71d4a196a52ae7a02f146eb5373a2d5a59fd9e2cadd1c86ad9fb74f403169a" 

Gx, Gy = get_coordinates_from_pubkey(pubkeyhex) 

print(f"pubkey: {pubkeyhex}") 
print(f"") 
print(f"(Gx, Gy) = {Gx} {Gy}")
