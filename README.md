<h1 align="center">
  <img src="https://github.com/aurora-0025/i3-autosplit/blob/master/images/thumbnail.png?raw=true" width=50%/><br/>
</h1>
<h5 align="center">To dynamically change the split direction in I3/Sway so as to split new windows automatically based on the width and height of the focused window</h3>

<p align="center"><a href="https://github.com/olemartinorg/i3-alternating-layout">Inspired By</a></p>

---

# Quick start

## Ubuntu

```bash
  $ sudo apt install python3-pip
  $ pip3 install i3ipc
  $ git clone https://github.com/aurora-0025/i3-autosplit 
```
Adding to your i3-autosplit to autostart of i3 config

> Edit your i3 config file `~/.config/i3/config` add this line

```bash
    exec --no-startup-id python /path/to/i3-autosplit.py
```

## Arch

```bash
  $ sudo pacman -S python-pip 
  $ pip3 install i3ipc
  $ git clone https://github.com/aurora-0025/i3-autosplit
```
Adding to your i3-autosplit to autostart of i3 config

> Edit your i3 config file `~/.config/i3/config` add this line

```bash
    exec --no-startup-id python /path/to/i3-autosplit.py
```
# PREVIEW
<h1 align="center">
  <img src="./images/preview.gif"/><br/>
</h1>






