from cryptography.fernet import Fernet
import argparse
import base64

def encrypt(message, key, output_file):
    # Create a Fernet cipher suite with the provided key
    cipher_suite = Fernet(base64.urlsafe_b64encode(key))

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(message.encode())

    # Write the encrypted message to the specified output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_message)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Encrypt a message and write it to a file.")
    parser.add_argument("--message", required=True, help="The message to encrypt")
    parser.add_argument("--key", required=True, help="The encryption key")
    parser.add_argument("--output", required=True, help="The output file path")
    args = parser.parse_args()

    # Ensure the key is 32 bytes long
    key = base64.urlsafe_b64encode(args.key.encode())
    key = key.ljust(32, b'=')

    # Call the encryption function
    encrypt(args.message, key, args.output)

if __name__ == "__main__":
    main()

