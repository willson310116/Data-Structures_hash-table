# Data Structure HW_Hash table

## usage
```python
python3 create_hash_value.py
python3 search.py
```
- `create_hash_value.py` will create a file `hash_value.txt` which contains hash values of passwords in file `password.txt`.
    - with $salt$ `000~999` added in front of the ascii code of each password, using $Hash function =$ $(243 × left) + right)$ $mod$ $85767489$, where left is the left 8 digits of the ascii code, and right is the rest 7 digits of the ascii code.
- `search.py` allows users to input arbitrary hash value, and returns the corresponding password and salt value if it exists.
___


***There are 2 source code files, follow the usage instruction, and it will work nicely.***

