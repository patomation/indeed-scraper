from pprint import pprint
from os import system
import sys
import re


# My Modules
from modules import html, queryString, excel

def scrape(props):
    search = props['search']
    # Clear Screen
    _ = system('clear')

    # Display Obligitory Branding Message
    print "==========================================================================="
    print " "
    print " Googel Search SCRAPER tm"
    print " "
    print "==========================================================================="
    print " "
    print " "

    # Abstracts checking if element exists to prevent erors
    def textScrub (element):
        string = ''
        if element != 'None':
            if hasattr(element, 'text'):
                # encodes string
                string = element.text.encode("utf-8")
                # regex for cleaning characters out
                regex = re.compile('[^a-zA-Z.://]')
                # cleans string
                string = regex.sub('', string)
        return string


    url='https://www.google.com/search?q='+search
    page = html.parse(url)

    results = []

    rank = 1
    for result in page.findAll('div', { 'class':'g'}):
        name = textScrub( result.find('h3') )
        link = textScrub( result.find('cite') )
        print '----'
        print name
        print link

        results.append({
            'rank' : rank,
            'name' : name,
            'link' : link
        })
        rank += 1


    print '-----------------------------------------------------------------'
    print 'Finished Scraping'
    print '-----------------------------------------------------------------'
    print results
    # print '...Processing Output Files....'
    excel.write({
        'columns':{
            'A' : {'label':'rank'   ,'width':  5},
            'B' : {'label':'name'   ,'width': 30},
            'C' : {'label':'link'   ,'width': 30}
        },
        'items':results,
        'fileName': './google-rank_'+search.replace(' ', '-')+'.xlsx'
    })
