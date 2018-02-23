#!/usr/bin/env python2
import argparse, getpass, time, sys
from argparse import RawTextHelpFormatter

Version = 'v 1.02222018'

timestr = time.strftime("%Y%m%d-%H%M")

class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"
   lightblue = "\033[0;34m"

banner = (
    colors.lightblue + '\ndataScrape.py ' + Version + colors.normal +
    '\nDescription: Enumerates employee names from connect.data.com. Code stolen from LinkScrape ' +
    '\nLinkScrape lead Developers: Nick Sanzotta (@beamr) & Jacob Robles (@shellfail)' +
    '\nDataScrape lead thief: Kirk Hayes (@l0gan)' + '\n' +
    '*' * 95 +'\n')

def valid_range(pages):
    pages = pages.strip()
    if pages.isdigit():
        #use this as last page
        return
    elif '-' in pages:
        #may have a range
        pages = pages.split('-')
        if len(pages) != 2:
            print 'Invalid Range'
            sys.exit(1)
        else:
            first,last = pages[0].strip(),pages[1].strip()
            if first.isdigit() and last.isdigit() and int(first) >= 1 \
                and int(first) < int(last):
                #print int(first), int(last), 'Valid'
                pass
            else:
                print 'Invalid Range'
                sys.exit(1)
    else:
        #invalid range
        print 'Invalid Range'
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=\
        banner +
        "Usage: python dataScrape.py <OPTIONS> \n" +
        "Example[1]: python dataScrape.py -e connect.data.comUser@email.com -c 'acme' -m 7 -d acme.com\n" +
        "Example[2]: python dataScrape.py -e connect.data.comUser@email.com -c 'acme' -m 99 -d acme.com\n" +
        "Example[3]: python dataScrape.py -m 7 -i ~/Company/names.txt\n" +
        "Raw output saved to: data.com/dataScrape-data/Company_time.txt " +
        "Formatted output saved to: data.com/dataScrape-data/Company-mangle[x]_time.txt \n")

    auth_group = parser.add_argument_group(colors.lightblue + 'Login options' + colors.normal)
    auth_group.add_argument('-e', '--email',
        help="Your connect.data.com Email Address")
    auth_group.add_argument('-p', '--password',
        help="Your connect.data.com Password.\n" +
                "If -p is not defined, you'll be prompted")

    search_group = parser.add_argument_group(colors.lightblue + 'Search options' + colors.normal)
    search_group.add_argument('-c', '--company',
        help="Company you want to enumerate.\n" +
                "(Prepends to filename if used with -i)")

    mangle_help = ("1)FirstLast\n"
                "2)LastFirst\n"
                "3)First.Last\n"
                "4)Last.First\n"
                "5)First_Last\n"
                "6)Last_First\n"
                "7)FLast\n"
                "8)LFirst\n"
                "9)FirstL\n"
                "10)F.Last\n"
                "11)L.Firstname\n"
                "12)FirLa\n"
                "13)LastFir\n"
                "14)FLastnam\n"
                "15)LastF\n"
                "16)LasFi\n"
                "99)All              Mangle using all types")

    mangle_group = parser.add_argument_group(colors.lightblue + 'Mangle options' + colors.normal)
    mangle_group.add_argument('-m', '--mangle', type=int, choices=list(range(1,17)) + [99], default=7,
        help=mangle_help)
    mangle_group.add_argument('-d', '--domain',
        help='Append @domain.com to enumerater user list')
    mangle_group.add_argument('-i', '--input',
        help='Use local file instead of connect.data.com to perform name Mangle.')

    args = parser.parse_args()

    #Only ask for user/pass when doing LinkedIn search
    if not args.input:
        if not args.email:
            args.email = raw_input('Enter connect.data.com Email account[user@email.com]:')
            print('ENTERED: {0}\n'.format(args.email))
        if not args.password:
            args.password = getpass.getpass('Enter connect.data.com Password: ')
    while not args.company:
        args.company = raw_input('Enter Company[ex:acme]: ').strip()
        print('ENTERED: {0}\n'.format(args.company))
    if not args.domain:
        args.domain = raw_input('Enter Domain suffix[ex:acme.com]: ')
        print('ENTERED: {0}\n'.format(args.domain))

    return args

if __name__ == "__main__":
    args = parse_args()
    print args

