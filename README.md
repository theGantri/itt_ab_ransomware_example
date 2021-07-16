# ITT_ab Ransomware Code Example

simple short ransomware example in 50 lines of python code that was written for a school presentation

## Execution
---
### Encryption
encrypts all the files in folder and generates a key file (used for decryption) for each.
```
python app.py encrypt PATH_TO_FOLDER
```
#### Example:
```sh
python app.py encrypt "test"
```

### Decryption
decrypts all the files in folder with using the proper key files. Deletes the key files after decription.
```
python app.py decrypt PATH_TO_FOLDER
```
#### Example:
```sh
python app.py decrypt "test"
```
