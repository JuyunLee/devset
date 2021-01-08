#!/usr/bin/python3
import sys
import urllib.request as urlreq
from multiprocessing import Process
import time

def work(id, url, verbose):
    msecs = time.time()*1000
    urlreq.urlopen(url)
    if verbose == 1:
        print(" Got response of id=" + str(i) + " [" + str(time.time()*1000 - msecs) + "ms]")

    return

verbose = 0

if len(sys.argv) == 4 and sys.argv[3] == "-v":
    verbose = 1
elif len(sys.argv) != 3:
    print("\n Usage : " + sys.argv[0] + " <url> <# of request(max 500)> [option]\n\n [options]\n  -v : verbose\n")
    exit(1)

if int(sys.argv[2]) > 500:
    print("\n Too many requests(max 500)")
    exit(1)

print("\n Send reqeusts to " + sys.argv[1] + " " + sys.argv[2] + " times.")
print(" Don't use this to attack somewhere without agreement\n")
confirm = input(" Start these requests? [y/N] ")
if confirm == "y":
    print()
    ps = [];
    for i in range(0, int(sys.argv[2])):
        if verbose == 1:
            print(" Send request id=" + str(i))
        ps.append(Process(target=work, args=(i, sys.argv[1], verbose)))
        ps[i].start()
    for i in range(0, int(sys.argv[2])):
        ps[i].join()
    print("\n complete")
else:
    print(" bye")
