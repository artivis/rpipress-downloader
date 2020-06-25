# rpipress-downloader

[![Snap Status](https://build.snapcraft.io/badge/artivis/rpipress-downloader.svg)](https://build.snapcraft.io/user/artivis/rpipress-downloader)

Download Raspberry Pi Press issues.

Freely available magazines are: Hackspace, HelloWorld, MagPi and Wireframe.
You can choose to download all issues or only the latest one(s)
for all or some magazines.

Issues are saved in `~/snap/rpipress-downloader/current/rpipress/{magazine}`.

## Install

### From source

```bash
$ git clone https://github.com/artivis/rpipress-downloader.git
$ cd rpipress-downloader/scripts
```
Use with,
```bash
python3 rpipress-downloader
```

### Snap

```bash
sudo snap install rpipress-downloader
```
Use with,
```bash
rpipress-downloader
```

## Use

By default, invoking `rpipress-downloader` will download all issues
for each magazine if they are not already available locally.

You can choose to download issues only for one (or some) magazine(s),
```bash
$ rpipress-downloader --magazines magpi hackspace
```
You can also download only the latest issue of each magazine,
```bash
$ rpipress-downloader --latest
```
You can also combine options,
```bash
$ rpipress-downloader -l -m magpi
```
will download only the latest MagPi issue.

## Options

```bash
$ rpipress-downloader -h
usage: rpipress-downloader [-h]
                           [-m {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...]]
                           [-l] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -m {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...], --magazines {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...]
                        Choose which magazine(s) to download. Defaults to all
  -l, --latest          Download only the latest issue
  -q, --quiet           No prints
```
