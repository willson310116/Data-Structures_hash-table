# Password-check-by-hash-table

## Abstract
It's an extension of a programming assignment of course Data Structures Fall 2020.


## Usage
```python
python3 password_generator.py num 
python3 create_hash_value.py
python3 search.py
```
*num is the number of pseudo password you want to create*
- `password_generator.py` will create passwords with 6 uppercase letters, and write into file `pseudo_password.txt`
- `create_hash_value.py` will create a file `hash_value.txt` which contains hash values of passwords in file `password.txt`.
    - with salt `000~999` added in front of the ascii code of each password; then use `Hash function` to derive the hash value of the ascii code with salt
- **Hash function = (243 × left) + right) mod 85767489**, where left is the left 8 digits of the ascii code, and right is the rest 7 digits of the ascii code.
- `search.py` allows users to input arbitrary hash value, and returns the corresponding password and salt value if it exists.
___


***There are 3 source code files, follow the usage instruction, and it will work nicely～***

