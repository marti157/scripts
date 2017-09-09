# HOT MOTD
Easy script for a nice motd

## Setup
Open /etc/profile and add this line at the bottom:
```
/directory/to/script/HotMotd.sh
```
You should also remove everything in the /etc/motd file.
When you have done that, open /etc/ssh/sshd_config and change
```
PrintLastLog yes
PrintMotd yes
```
with
```
PrintLastLog no
PrintMotd no
```
Modify /etc/pam.d/login and comment this line:
```
#session    optional   pam_motd.so
```
Then restart SSH with
```
sudo service ssh restart
```
You are mostly done now.

Favourite if you used the script!

Also leave feedback if you liked it and I will make this into a repo, with
more options.
