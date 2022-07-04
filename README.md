# TOTP-Generator

Simple Desktop app on PyQt with TOTP-Generator.
The application accepts a 32-digit secret key and generates one-time password based on it, which is updated every 30 seconds

## Application protection
The main method of protecting the application is a permanent password, which, if absent, is generated automatically when the secret key is entered for the first time but the user can also set his password for protection and change it at any time. The keyring library was used as a tool for secure storage of the secret key. The basic principle of operation is based on the fact that each OS user has its own encrypted storage, access to which is possible only after the user logs in, so other users and their software will not have access to the local keystore. By storing the secret key in the OS credential storage in encrypted form and decrypting it in the application using the password key, we complicate its theft.
## Tip
If you forgot your secret key or password you can find them with:
```
print(cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos1), cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key)))
```
```
print(cryptocode.decrypt(keyring.get_password(credentials.service_id, credentials.pos2), credentials.secret_key))
```