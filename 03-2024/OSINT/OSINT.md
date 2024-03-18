## OSINT
```sh
"OSINT"
Problem: find a flag going step by step
```
Solution:
```
Step 1:
find metadata of the picture using exiftool:
```
![alt text](image.png)
where you'll find the link to Telegram Channel
```
Step 2:
```
some messages from user:
![alt text](image-1.png)
```
Step 3:
```
latitude and longitude checking:
![alt text](image-2.png)
lets see reviews of our university:))
![alt text](image-3.png)
Step 4:
twitter profile:
![alt text](image-4.png)
use google dorks to see location of the place from the picture:
![alt text](image-5.png)
we have checked reviews of New Uzbekistan University, lets see reviews of Cesar:
![alt text](image-6.png) 
Step 5:
from github we found:
![alt text](image-7.png)
lets use Caesar Cipher decoder to decode xee_pvkq{d@5d4_m@35@b}
![alt text](image-8.png)
```
Finally here is the answer:
nuu_flag{t@5t4_c@35@r}
```