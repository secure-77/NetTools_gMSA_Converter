# NetTools_gMSA_Converter
 Tool to convert gMSA passwords from HEX to MD4 / NT hashes
 
 
 
### gMSA Passwords

This approach is an alternative way to https://github.com/micahvandeusen/gMSADumper for getting gMSA passwords 

1. Following this instructions from NetTools (https://nettools.net/howto-retrieving-gmsa-password-details/) to retrieve the password from an account

2. Copy the string form the current password, make sure you only copy the part until the previous password part and delete the tailing 0000, the final string should look like this

```plaintext
A19E 5B5D 2BDC 3A2A E61F 415B B806 1002 5CD3 619B 74FB 75B7 09A7 D89E 53E4 67C6 3828 C8FE ADED 29C5 9EC7 1178 DC83 AFC1 F26F D643 B7B7 AF6C AE7F 1A7C E7A9 0766 AEE3 5949 3E83 8567 86FF 42F7 2D7B 33A3 D3DD D510 F444 BB4C C604 6C6F 9D8B 3ADF A78F 7CD6 233E 5CD5 F72C 9FED 6212 164A 4ED3 8FA7 A9ED 5CF7 EEE3 3D65 541E E9BE D0A9 1FE0 93A4 690F F155 D020 7051 5CAC F044 3BE7 A1F6 92C7 1590 3B15 8CCE EF92 7613 7B11 6E9F BD73 2BCB 2454 CDCA EC47 EA53 4D3F E0EF 94B2 A79C C5B6 8690 1160 EF0C 4209 C20E 9B97 834A 6DF4 65BA B642 3BF5 EE8F C111 06A1 F6C1 9A02 D9CC F153 A67B 3ADD 983C 7A20 9123 A7B6 17C0 CD83 782F AFE5 9A0A 7992 2DE2 1C27 2A8A 26AC
````

3. Pass the hex to the converter to retrieve the MD4 / NT Hash.

```bash
python3 md4.py -i 'A19E 5B5D 2BDC 3A2A E61F 415B B806 1002 5CD3 619B 74FB 75B7 09A7 D89E 53E4 67C6 3828 C8FE ADED 29C5 9EC7 1178 DC83 AFC1 F26F D643 B7B7 AF6C AE7F 1A7C E7A9 0766 AEE3 5949 3E83 8567 86FF 42F7 2D7B 33A3 D3DD D510 F444 BB4C C604 6C6F 9D8B 3ADF A78F 7CD6 233E 5CD5 F72C 9FED 6212 164A 4ED3 8FA7 A9ED 5CF7 EEE3 3D65 541E E9BE D0A9 1FE0 93A4 690F F155 D020 7051 5CAC F044 3BE7 A1F6 92C7 1590 3B15 8CCE EF92 7613 7B11 6E9F BD73 2BCB 2454 CDCA EC47 EA53 4D3F E0EF 94B2 A79C C5B6 8690 1160 EF0C 4209 C20E 9B97 834A 6DF4 65BA B642 3BF5 EE8F C111 06A1 F6C1 9A02 D9CC F153 A67B 3ADD 983C 7A20 9123 A7B6 17C0 CD83 782F AFE5 9A0A 7992 2DE2 1C27 2A8A 26AC'

md4 / NT Hash:
47e89a6afd68e3872ef1acaf91d0b2f7
```


further information: https://secure77.de/gmsa-passwords/








