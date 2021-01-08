#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import argparse
import urllib.request as urlreq
import progressbar
import requests
import os
import sys


pbar = None

def progress_bar(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


def is_a_clink(tag):
    return tag.name == 'a' and \
           tag.has_attr('class') and \
           tag.get('class') == ['c-link']


def downloadable_entry(tag):
    return is_a_clink(tag) and tag.has_attr('download')


def book_entry(tag):
    return is_a_clink(tag) and \
        tag.has_attr('data-category') and tag.get('data-category') == 'book'


magazines = {
    'hackspace' : 'HackSpace',
    'helloworld' : 'HelloWorld',
    'magpi' : 'MagPi',
    'wireframe' : 'Wireframe',
}

parser = argparse.ArgumentParser(description="""
Download Raspberry Pi Press issues.

Freely available magazines are: HackSpace, HelloWorld, MagPi and Wireframe.

By default `rpipress-downloader` downloads only the latest issue of each
magazine. However you can download all issues, all books for all or some magazines.

Issues and books are saved respectively in
- `~/rpipress/{magazine}`
- `~/rpipress/{magazine}/Books`

or, using the snap, in
- `~/snap/rpipress-downloader/current/rpipress/{magazine}`,
- `~/snap/rpipress-downloader/current/rpipress/{magazine}/Books`.
""", formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument("-m", "--magazines", help="Choose which magazine(s) to download. Defaults to all",
                    type=str.lower, action='append', nargs='+',
                    choices=list(magazines.keys()))
parser.add_argument("-a", "--all", help="Download all issues",
                    action="store_true")
parser.add_argument("-b", "--books", help="Download the magazine books",
                    action="store_true")
parser.add_argument("-q", "--quiet", action="store_true", help="No prints")
args = parser.parse_args()

filtered_magazines = dict()
if args.magazines:
    # Retrieve all requested magazines in flatten list
    requested_magazines = [item for sublist in args.magazines for item in sublist]

    # Remove duplicates
    requested_magazines = list(dict.fromkeys(requested_magazines))

    # Get subset
    filtered_magazines = {m: magazines[m] for m in requested_magazines}
else:
    # If none specified, get them all
    filtered_magazines = magazines

# Creating the download folder
output_base_path = os.getenv('SNAP_USER_DATA')
if not output_base_path: output_base_path = os.path.expanduser('~')

download = False
for magazine, Magazine in filtered_magazines.items():

    output_path = os.path.join(output_base_path, 'rpipress', Magazine)

    if not os.path.exists(output_path): os.makedirs(output_path)

    base_url = 'https://' + magazine + '.raspberrypi.org'

    issues_url = base_url + '/issues'

    # Find latest review number
    try:
        r = requests.get(issues_url)
        data = r.text
        soup = BeautifulSoup(data,"lxml")
        last_issue = soup.find('section', class_="c-latest-issue").findChild("a")['href'].split('/')[-1]
    except():
        raise Exception('Could not find latest ' + Magazine + ' issue number')
    else:
        if not args.quiet: print('Latest ' + Magazine + ' issue is N°' + last_issue)

    start_issue = 1 if args.all else int(last_issue)

    # Download issues
    for issue in range(start_issue, int(last_issue) + 1):
        try:
            issue_path = os.path.join(output_path, Magazine + '{:02d}.pdf'.format(issue))
            if not os.path.exists(issue_path):
                r = requests.get(issues_url + '/{:02d}/pdf'.format(issue))
                data = r.text
                soup = BeautifulSoup(data, "lxml")
                tag = soup.find(downloadable_entry)
                if not tag:
                    r = requests.get(issues_url + '/{:02d}/pdf/download'.format(issue))
                    data = r.text
                    soup = BeautifulSoup(data, "lxml")
                    tag = soup.find(is_a_clink, string='click here to get your free PDF')
                    tag['href'] = base_url + tag['href']
                show_progress = progress_bar if not args.quiet else None
                urlreq.urlretrieve(tag['href'], issue_path, show_progress)
                download = True
            else:
                continue
        except():
            if not args.quiet: print('ERROR: There was an error downloading ' + Magazine + ' N°{:02d}'.format(issue))
        else:
            if not args.quiet: print(Magazine + ' N°{:02d} downloaded!'.format(issue))

    if args.books:

        books = {}

        # Find all books
        try:
            r = requests.get(base_url + '/books')
            data = r.text
            soup = BeautifulSoup(data, "lxml")
            tags = soup.find_all(book_entry)
        except():
            if not args.quiet: print('ERROR: There was an error retrieving the book list')
        else:
            for tag in tags:
                books[tag['data-label']] = tag['href']

            if books:
                output_path = os.path.join(output_path, 'Books')
                if not os.path.exists(output_path): os.makedirs(output_path)

                # Download each book if not already there
                for book_name, book_href in books.items():
                    try:
                        book_path = os.path.join(output_path, book_name + '.pdf')
                        if not os.path.exists(book_path):
                            r = requests.get(base_url + book_href + '/pdf')
                            data = r.text
                            soup = BeautifulSoup(data, "lxml")
                            tag = soup.find(downloadable_entry)
                            if not tag:
                                r = requests.get(base_url + book_href + '/pdf/download')
                                data = r.text
                                soup = BeautifulSoup(data, "lxml")
                                tag = soup.find(is_a_clink, string='click here to get your free PDF')
                                tag['href'] = base_url + tag['href']
                            show_progress = progress_bar if not args.quiet else None
                            urlreq.urlretrieve(tag['href'], book_path, show_progress)
                            download = True
                        else:
                            continue
                    except():
                        if not args.quiet: print('ERROR: There was an error downloading ' + Magazine + ' book ' + book_name)
                    else:
                        if not args.quiet: print(Magazine + ' book \'' + book_name + '\' downloaded!')

if not args.quiet:
    if not download: print('You are up to date')
    print('Your favorite magazines are waiting for you in ' +
        'file://' + os.path.join(output_base_path, 'rpipress'))
