To run challange:
```sh
sudo docker-compose up
```
<img src="Pasted image 20250412210217.png">
app was using the weak secret to sign the JWT keys:
<img src="Pasted image 20250412210542.png">

brute force it with 
JWT tool https://github.com/ticarpi/jwt_tool
or `hashcat` 
```sh
hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list
```
with Seclists jwt wordlist
https://github.com/danielmiessler/SecLists/blob/master/Passwords/scraped-JWT-secrets.txt


