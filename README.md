# rpipress-downloader

[![Snap Status](https://build.snapcraft.io/badge/artivis/rpipress-downloader.svg)](https://build.snapcraft.io/user/artivis/rpipress-downloader)

Download Raspberry Pi Press issues.

Freely available magazines are:
[HackSpace](https://hackspace.raspberrypi.org/),
[HelloWorld](https://helloworld.raspberrypi.org/),
[MagPi](https://magpi.raspberrypi.org/) and
[Wireframe](https://wireframe.raspberrypi.org/).

By default `rpipress-downloader` downloads only the latest issue of each
magazine.
However you can download all issues, all books for all or some magazines.

Issues and books are saved respectively in
- `~/rpipress/{magazine}`
- `~/rpipress/{magazine}/Books`

or, using the snap, in
- `~/snap/rpipress-downloader/current/rpipress/{magazine}`,
- `~/snap/rpipress-downloader/current/rpipress/{magazine}/Books`.

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

By default, invoking `rpipress-downloader` will download only the latest issue
for each magazine if they are not already available locally.

You can:
- download issues only for one (or several) magazine(s),
```bash
$ rpipress-downloader --magazines magpi hackspace
```

- download all issue of each magazine,
```bash
$ rpipress-downloader --all
```

- download all books,
```bash
$ rpipress-downloader --books
```

- combine options,
```bash
$ rpipress-downloader -a -m magpi -b
```
will download all MagPi issues and books.

## Options

```bash
$ rpipress-downloader -h
usage: rpipress-downloader [-h]
                           [-m {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...]]
                           [-a] [-b] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -m {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...], --magazines {hackspace,helloworld,magpi,wireframe} [{hackspace,helloworld,magpi,wireframe} ...]
                        Choose which magazine(s) to download. Defaults to all
  -a, --all             Download all issues
  -b, --books           Download the magazine books
  -q, --quiet           No prints
```
