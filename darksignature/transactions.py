import subprocess

def save_output_to_file(output):
    with open("SignatureRSZ.txt", "a") as file:
        file.write(output)

# Number of signatures in a Bitcoin transaction
for i in range(32):
    process = subprocess.run(
        ["./darksignature", "-pubkey",
         "0f71d4a196a52ae7a02f146eb5373a2d5a59fd9e2cadd1c86ad9fb74f403169a",
         "c7199eab2b040586b9adb32aa052acdb916bee6f6c90e41ba655669b5e7352fb"],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    output = f"|ECDSA Signature R,S,Z values from Bitcoin №{i+1}:\n{process.stdout}\n"
    print(output)
    save_output_to_file(output)
