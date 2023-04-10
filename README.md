# rpipress-downloader

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/rpipress-downloader)

Download Raspberry Pi Press issues.

Freely available magazines are:
<!-- [Custom PC](https://custompc.raspberrypi.org/), -->
[HackSpace](https://hackspace.raspberrypi.org/),
[HelloWorld](https://helloworld.raspberrypi.org/) and
[MagPi](https://magpi.raspberrypi.org/)
<!-- [Wireframe](https://wireframe.raspberrypi.org/). -->

Remember that you can find these resources for free only thanks to people
around the world supporting them.
You too can support their work either by buying physical copies or
by making a contribution of any size.

By default `rpipress-downloader` downloads only the latest issue of each
magazine.
However you can download all issues, all books for all or some magazines.

Issues and books are saved respectively in

- `~/rpipress/{magazine}`
- `~/rpipress/{magazine}/Books`

or, using the snap, in

- `~/snap/rpipress-downloader/current/rpipress/{magazine}`,
- `~/snap/rpipress-downloader/current/rpipress/{magazine}/Books`.

## Installation

### From source

```bash
git clone https://github.com/artivis/rpipress-downloader.git
cd rpipress-downloader
python3 -m pip install -U .
```

### Snap

```bash
sudo snap install rpipress-downloader
```

## Use

By default, invoking `rpipress-downloader` will download only the latest issue
for each magazine if they are not already available locally.

You can:

- download issues only for one (or several) magazine(s),

  ```bash
  rpipress-downloader --magazines magpi hackspace
  ```

- download all issue of each magazine,

  ```bash
  rpipress-downloader --all
  ```

- download all books,

  ```bash
  rpipress-downloader --books
  ```

- download to a specific base path,

  ```bash
  rpipress-downloader --path /home/ubuntu/Documents
  ```

- combine options,

  ```bash
  rpipress-downloader -a -m magpi -b -p /home/ubuntu/Documents
  ```

will download all MagPi issues and books in `/home/ubuntu/Documents/rpipress/MagPi`.

## Options

```bash
$ rpipress-downloader -h
usage: rpipress-downloader [-h] [-a] [-b] [-m {hackspace,helloworld,magpi} [{hackspace,helloworld,magpi} ...]] [-p PATH] [-q]

Download Raspberry Pi Press issues.

Freely available magazines are: HackSpace, HelloWorld, MagPi.

By default `rpipress-downloader` downloads only the latest issue of each
magazine. However you can download all issues, all books for all or some magazines.

By default, issues and books are saved respectively in
- `~/rpipress/{magazine}`
- `~/rpipress/{magazine}/Books`

or, using the snap, in
- `~/snap/rpipress-downloader/current/rpipress/{magazine}`,
- `~/snap/rpipress-downloader/current/rpipress/{magazine}/Books`.

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Download all issues
  -b, --books           Download the magazine books
  -m {hackspace,helloworld,magpi} [{hackspace,helloworld,magpi} ...], --magazines {hackspace,helloworld,magpi} [{hackspace,helloworld,magpi} ...]
                        Choose which magazine(s) to download. Defaults to all.
  -p PATH, --path PATH  Set the download path. Defaults to ~/rpipress or ~/snap/rpipress-downloader/current/rpipress.
  -q, --quiet           No prints
```
