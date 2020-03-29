import os, sys, zipfile
from argparse import ArgumentParser
from threading import Thread
from colors import Normal as n, Bold as b, Symbols as s

"""
Old Zipfile Password Cracker from long ago...
"""

def extract(zip, passwd):
    try:
        # Try to extract the zip archive with password
        zip.extractall(pwd=passwd)
        # Print status
        print s.plus + n.ws + "Found password: \"" + n.ys + str(passwd) + n.ws + "\"" + n.ce + "\n"
        pass
    except Exception as e:
        print "\n" + s.error + n.ws + str(e) + n.ce + "\n"
        sys.exit(1)

def main():
    # Initialize parser module
    parse = ArgumentParser(usage="zipcrack.py -F <ZIPFILE> -D <DICTIONARY_FILE> | -h, --help", conflict_handler="resolve")
    parse.add_argument('-F', '--zip', type=str, dest="opc_ziparch", metavar='', default=None, help="Specify a locked zip file.")
    parse.add_argument('-D', '--dict', type=str, dest="opc_dictfile", metavar='', default=None, help="Specify a dictionary file.")
    parse.add_argument('-T', '--thread-it', action="store_true", dest="opc_thread", help="Initialize multiple decrypt "
                                                                                         "instances using threading.")

    args = parse.parse_args()

    if args.opc_ziparch is None and args.opc_dictfile is None:
        print n.ws + parse.usage + n.ce
        exit(1)
    else:
        zip = zipfile.ZipFile(args.opc_ziparch)
        pf = open(args.opc_dictfile)

        for string in pf.readline():
            pwd = string.strip('\n')

            if args.opc_thread:
                t = Thread(target=extract, args=(zip, pwd))
                # Start the thread
                t.start()
            else:
                extract(zip, pwd)
                pass

if __name__ == '__main__':
    main()
