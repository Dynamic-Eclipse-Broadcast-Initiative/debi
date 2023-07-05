#!/usr/bin/env python

# hdrsnap [args] <watchdir> <destdir>
#
# hdrsnap monitors <watchdir> for workfiles consisting
# of the form snap*.txt

# It will attempt to process the file.
# If it succeeds it will delete the file,
# If it fails, it will rename it to bad*.txt

# The job:
# a workfile consists of a list of filenames, one per line to combine into
# an HDR image to be placed in <destdir> (Maybe this becomes
# uploading eventually).  Naming conventions can be refined by
# additional args.
#

import argparse
import glob
import logging
import os.path
import sys
import time
from typing import Text

import watchdog.observers
import watchdog.events

from . import merge_fits

loglevel = logging.INFO

def process_workfile(workfile: Text, destfile: Text) -> bool:
    image_files = []
    with open(workfile, 'r') as fd:
        logging.debug(f'Processing workfile {workfile}')
        for line in fd:
            fn = line.strip()
            if not os.access(fn, os.R_OK):
                logging.error("Cannot open image: " + fn)
                return False
            image_files.append(fn)
    try:
        print(image_files)
        if '.fits' in image_files[0]:
            merge_fits.merge_fits(image_files, destfile)
        elif '.tif' in image_files[0]:
            merge_fits.merge_tifs(image_files, destfile)
        else:
            raise(ValueError(f'Unknown image format'))

    except Exception as e:
        logging.error(e)
        raise(e)
        return False
    return True

def create_dest_and_fail_paths(workfile: Text, destdir: Text):
    """Returns (destfile, failedfile) a workfile."""
    dirname, basename = os.path.split(workfile)
    return os.path.join(destdir, basename[:-4] + '.jpg'), os.path.join(dirname, 'bad' + basename[4:])

def process_dir(watchdir, destdir):
    for workfile in glob.glob(os.path.join(watchdir, 'snap*.txt')):
        destfile, failedfile  = create_dest_and_fail_paths(workfile, destdir)
        logging.info(f'Processing {workfile} to make {destfile}')
        if process_workfile(workfile, destfile):
            os.remove(workfile)
        else:
            os.rename(workfile, failedfile)

class HdrHandler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(
                self, patterns=['snap.*.txt'], ignore_directories=True,
                case_sensitive=False)
        def on_closed(self, event):
            print(events.src_path, "closed")

# Watch a directory for work files, and call a worker function if it finds any.
def watch_dir(watchdir: Text, destdir: Text):

    """
    TODO: use watchdog
    event_handler = HdrHandler()

    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, watchdir)
    observer.start()
    """
    logging.info("Hello!")

    workfunc = lambda: process_dir(watchdir, destdir)

    try:
        while True:
            time.sleep(1)
            workfunc()
    finally:
        pass
    """
        observer.stop()
        observer.join()
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='hdrsnap',
            description='watch and generate hdr snaps')
    parser.add_argument('watchdir', help='directory to monitor for workfiles')
    parser.add_argument('destdir', help='destination directory for results')
    parser.add_argument('--once', action='store_true', help='run worker once')
    parser.add_argument('--debug', action='store_true', help='run worker once')

    args = parser.parse_args()

    if args.debug:
        loglevel = logging.DEBUG

    logging.basicConfig(level=loglevel)

    if args.once:
        process_dir(args.watchdir, args.destdir)
        sys.exit()

    watch_dir(args.watchdir, args.destdir)
