# dataScrape ![Supported Python versions](https://img.shields.io/badge/python-2.7-blue.svg)
      dataScrape.py v 1.02222018
      Description: Enumerates employee names from connect.data.com
      Created by: Kirk Hayes / @l0gan
      Inspired by (and code stolen from) LinkScrape by: Nick Sanzotta / @beamr  &  Jacob Robles / @shellfail

      ***********************************************************************************************

***
Installation:

    git clone https://github.com/MooseDojo/reponamehere.git
    cd reponamehere/OSINT/dataScrape
    python dataScrape.py --help

    3rd Party Python libraries may be required:
    pip install beautifulsoup4
    pip install bs4
    pip install lxml

***
Caveats

    Does not utilize connect.data.com API.(This is a pure Web Scraper)
    connect.data.com Account may be flagged or banned.
    Script still has some minor bugs when scraping some character sets.
***

***
Default Values:

    If a parameter is not defined it's default value will be chosen.
    Default values listed below.

    Mangle Option = 7  ex: FLast

***
Usage(CLI):

    Usage: python dataScrape.py <OPTIONS>
    Example[1]: python dataScrape.py -e connect.data.comUser@email.com -c 'acme.com' -m 7 -d acme.com
    Example[2]: python dataScrape.py -e connect.data.comUser@email.com -c 'acme.com' -m 99 -d acme.com
    Example[3]: python dataScrape.py -m 7 -i ~/Company/names.txt\n"
    Formatted output saved to: dataScrape-data/Company-mangle[x]_time.txt

    Login options:
    -e <email> Your connect.data.com Email Address.
    -p <pass>  Your connect.data.com Password. (If -p parameter is not defined, you'll be prompt to enter a password)

    Search options:
    -c <company> Company domain name you want to enumerate.(Prepends to filename if used with -i)
  ***
Mangle Options:

    -m <mangle>
        1)FirstLast        
        2)LastFirst        
        3)First.Last       
        4)Last.First       
        5)First_Last       
        6)Last_First       
        7)FLast            
        8)LFirst           
        9)FirstL           
        10)F.Last          
        11)L.Firstname     
        12)FirLa           
        13)Lastfir
        14)FirstLastnam             
        15)LastF
        16)LasFi
        99)All              Mangle using all types


    -d <domain> Append @domain.com to enumerated user list."
    -i <input>  Use local file instead of connect.data.com to perform name Mangle."
    Misc:

    -h <help>  Prints this help menu.



***
Usage(Wizard):

      ENTERED: "acme.com"


       Mangle options:

             -m <mangle>		
                                       1)FirstLast        
                                       2)LastFirst        
                                       3)First.Last       
                                       4)Last.First       
                                       5)First_Last       
                                       6)Last_First       
                                       7)FLast            
                                       8)LFirst           
                                       9)FirstL           
                                      10)F.Last           
                                      11)L.Firstname      
                                      12)FirLa            
                                      13)Lastfir
                                      14)FirstLastnam
                                      15)LastF
                                      16)LasFi
                                      99)All              Mangle using all types

      Enter name Managle choice[ex:7]:
      ENTERED: "7"

      [*]TIP: This value will be added to the end of each mangled result[ex:jsmith@acme.com].
      Enter Domain suffix[ex:acme.com]: acme.com
      ENTERED: "acme.com"

