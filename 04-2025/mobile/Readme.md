1) Your goal was to analyze and modify an Android application to manipulate the in-game coin value and extract the flag

2) You could have used tool like ApkEasyTool: https://github.com/mkcs121/APK-Easy-Tool/releases
	Note: You should use latest version of the apktool: https://sourceforge.net/projects/apktool.mirror/files/v2.10.0/
	
3)   Launch the apkeasytool.exe provided with APK Easy Tool.
     Load the given .apk file by selecting it via the GUI.
     Use the "Decompile" option to break apart the APK contents.
     
4) you'd find a DLL file: Assembly-CSharp.dll
   This file holds the majority of the game's logic and is built with Unity.

5) You could open this DLL with tools such as dnSpy or ILSpy.

6) you should explore the folder with all DLLs:
   mytaxi\assets\bin\Data\Managed\
	Resources.ExternalUsage
	└── FlagShower
	<img src="./photo_1.png">
	
   Within FlagShower, there’s a check involving a coin threshold:

	```if (Bank.Coins == -10000L)```
	
7) Next, you should have navigated through the namespaces: 
	Assembly-CSharp.dll
	└── Client.Game
    	    └── CoinDisplaySystem
    	   
   Within CoinDisplaySystem, you would encounter variables and methods responsible for the coin balance. You could either inspect the methods modifying the coin value or directly alter the class to return a required value.
   ''photo_2''
   
8) After applying the necessary edits:
      Go back to APK Easy Tool.
      Use the "Compile" option to rebuild the modified APK and "Sign APK" to sign the application.
      Install and run the APK on an emulator or a test device.

9) In the main menu the button for revealing the flag would appear. 
   Copy the given string. 
   ''photo_3''

10) Lastly, you could use tool like CyberShef to convert the hex value into the flag
    ''photo_4''
