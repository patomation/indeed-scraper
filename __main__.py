import argparse
import os
from modules import scraper

def main():
    parser = argparse.ArgumentParser(description='Query Google Search')
    parser.add_argument('-q',
                    help='Search Term Query')


    args = parser.parse_args()

    if args.q == None:
        print "Must include search term with: -q 'google search term'"
        exit

    if( args.q != None ):
        scraper.scrape({
            'search': args.q
        })

if __name__ == "__main__":
    main()
