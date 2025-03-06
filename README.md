# instagram-unfollower
```
Usage: python unflow.py [username]
[username]  -  Your instagram username

NOTE: Your account/ip might get banned using this script, use it at your own risk
```
This script does not store your credentials! It just needs your username for some functionality (like detecting user login).
After running, you are presented with the login page. You need to login yourself, then everything is automated and script closes the browser and prints on the console.

There are some constant sleep timers that waits for the element to load, you can adjust accordingly.

Although there's a requirements.txt, here's the requirements:
- python 3+
- selenium
- Google chrome and ChromeDriver that you can download them [here](https://developer.chrome.com/docs/chromedriver/get-started). Just make sure they're on your $PATH
