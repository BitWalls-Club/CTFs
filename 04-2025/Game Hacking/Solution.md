1. Open the game here https://bitwalls-club.github.io/CTFs/04-2025/game/ , chromium based browsers recommended (google chrome , brave , chromium etc)
2. In the task you should have manipulate the game score (coins):

- Because the score was stored in the client side memory
- You should search a tool(memory debugger) that helps you to search that memory address where the score is saved and manipulate it
- I recommend "CheatEngine"  https://www.cheatengine.org/downloads.php

3. After the game launched open the browser task bar (Shift+Esc):
<img src="https://i.imgur.com/LwPUYsH.png">

4. Note the PID of the task that 30276 in my case 
Browsers convert PID to HEX format in computer memory
*The hexadecimal representation of the decimal number 30276 is **7606***
5. Attach that process to the CheatEngine <img src="https://i.imgur.com/RpZtbJZ.png">

6. Scan for the amount of coins you have with "New Scan"
<img src="https://i.imgur.com/59dWZNC.png">

7. Update the game coins that search that coins value with "Next Scan"
<img src="https://i.imgur.com/TtQ5JHR.png">

8. Continue the same process until you have only 1 result left
<img src="https://i.imgur.com/8qiaN5S.png">

9. Double Click the remaining value and change it to whatever value you want (e.g. 1337)
<img src="https://i.imgur.com/KwIGkbz.png>

10. Collect another coin to changes take affect and you have 1338 coins
<img src="https://i.imgur.com/eZU53rA.png">

11. Go to the game finish and you should get the flag
<img src="https://i.imgur.com/O6aerce.png">

Still dont get it? , watch the tutorial here https://www.youtube.com/watch?v=jfhzY7WnwbU 

Tag me in our community https://t.me/root_0t4j0n,  if you need any clarification


