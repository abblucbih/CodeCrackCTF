from Crypto.Cipher import AES
import os

# Function to remove padding from decrypted data
def unpad(data):
    return data.rstrip(b"\0")

# Function to decrypt a file
def decrypt_file(encrypted_file, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data)
    return unpadded_data

# Main function
def main():
    key = b'5910200000000000'  # 16 bytes key
    encrypted_file = "flag.txt.enc"
    if not os.path.exists(encrypted_file):
        print("Error: Encrypted file '{}' not found.".format(encrypted_file))
        return
    decrypted_data = decrypt_file(encrypted_file, key)
    with open("decrypted_flag.txt", 'wb') as f:
        f.write(decrypted_data)
    print("File decrypted successfully. Decrypted data saved as 'decrypted_flag.txt'.")

if __name__ == "__main__":
    main()
