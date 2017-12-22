# Wifi Killer Mac
## (or Linux)

A **Simple** but **Effective** WiFi Killer for **Mac**!
When I say **simple** I mean **simple**.

To be installed on a computer and then run from it. The script
denies WiFi access in a loop.

Piss off your friend or block someone's internet conection.

## Getting Started

The install is very easy: clone https://github.com/marti157/wifi-kill-mac.git and
copy the WifiKillMac.py script to a computer.

## Prerequisites

You need python installed to use this script. Python comes preinstalled on
OSX computers.

## Setting it up

Open the WifiKillMac.py script with any text editor and edit the password line with
the victim's computer's sudo password. Make sure the user is a sudoer.

```python
while True:
	"sudo ifconfig en0 down"
	"YourSudoPassword"
	time.sleep(10)
```
The only thing you have to change is the "YourSudoPassword".

### On Linux

You can do this on linux but you have to change the network node to the correct one.

Here it's "en0", but it's usually "wlan0" on Linux.

## Running

Once you have the script on the victim's computer, navigate to the directory where it
is located and run using this command:

```
sudo python WifiKillMac.py &
```
The "&" at the end makes the script run in the background.

## Persistance

The script stops running when the computer is restarted, but there is a way to get round
this. You can use Automator to run a script that executes the script when the computer boots up. Look at [this](https://developer.apple.com/library/content/documentation/AppleApplications/Conceptual/AutomatorConcepts/Articles/ShellScriptActions.html) for more information.

## Contributing

If you want to contribute create a pull request on whatever you want to modify and i will
get back as soon as i can.

## License

This project is licensed under the [LICENSE.md](https://github.com/marti157/scripts/LICENSE) Apache 2 License - see in the general scripts folder.

By Marti157
