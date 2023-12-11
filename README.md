# python-module--tolu-mohawk

# Text Encryption/Decryption

## Project Overview
This Python script provides a command line interface for encrypting and decrypting messages using the Python cryptography module. Users can supply a message and a key value for encryption, and the encrypted message will be written to a file of their choice. Additionally, the script can read text from a specified file and decrypt a message using a supplied key value.

## Installation Instructions
 Clone this repository to your local machine.
   ```
   git clone https://github.com/your-username/text-encryption-decryption.git
   cd text-encryption-decryption
   ```

## Install the required dependencies.
```
pip install cryptography
```

# Usage Guide

## Encryption
Encrypt a message and write it to a file.
```python encrypt.py --message "your message here" --key "your_key" --output "path/to/output_file.txt"
```

## Decryption
Decrypt a message from a file using a key.
```python decrypt.py --input "path/to/output_file.txt" --key "your_key"
```

Make sure to replace "your_key" with the actual key and provide the correct file paths. Use double quotes (" ") around the message and key if they contain spaces or specfial characters.

