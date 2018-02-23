#!/usr/bin/env python2
# Description: Enumerates employee names from connect.data.com based off company search results.

import os, sys, getopt, getpass, json, re, requests, time
import argparse
from argparse import RawTextHelpFormatter
from sys import argv
from bs4 import BeautifulSoup
from pprint import pprint
from dataArguments import *
from dataMangle import *

curr_time = time.time()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def login(client, email, password):
    homepage = 'https://connect.data.com/login?source=HPTopNav'
    login_page = 'https://connect.data.com/loginProcess'

    html = client.get(homepage).content
    soup = BeautifulSoup(html,'lxml')
    csrf = soup.find(id="CSRF_TOKEN")['value']
    login_information = {
        'j_username': email,
        'j_password': password,
        'CSRF_TOKEN': csrf,
        }

    login_response = client.post(login_page, data=login_information)
    # Validate Login.
    loginError = "Your email address and/or password could not be found."
    if loginError in login_response.text:
        print(" Invalid Password.")
        print(" Exiting...")
        sys.exit(2)

#close the session created by the script
def logout():
    pass

#search for possible companies
def company_search(client,companyName):
    # need to get DWRSESSIONID
    search_data = {
        'callCount': '1',
        'c0-scriptName': '__System',
        'c0-methodName': 'generateId',
        'c0-id': '0',
        'batchId': '0',
        'instanceId': '0',
        'page': '%2Fhome',
        'scriptSessionId': ''
    }
    response = client.post('https://connect.data.com/dwr/call/plaincall/__System.generateId.dwr', data=search_data)
    dwrsessionid = re.findall('"(.*?)"', response.text, re.DOTALL)
    dwrsessionid = dwrsessionid[2]
    # now we can pull names of employees
    search_data = {
        'callCount': '1',
        'nextReverseAjaxIndex': '0',
        'c0-scriptName': 'SearchDWR',
        'c0-methodName': 'findContacts',
        'c0-id': '0',
        'c0-param0': 'string:%7B%22filters%22%3A%7B%22companies%22%3A%5B%22' + companyName + '%22%5D%7D%2C%22actionsOnColumns%22%3A%7B%22companyName%22%3A%7B%22sort%22%3A%22asc%22%7D%7D%2C%22totalRecordsOnPage%22%3A5000%7D',
        'batchId': '0',
        'instanceId': '0',
        'page': '%2Fsearch',
        'scriptSessionId': dwrsessionid + '/03*PU7m-9oc9Nj9ug'
    }
    # need to figure out how to get the DWRSESSIONID cookie (set to null during login) and use in cookies and set the sessionId pre / to that value
    response = client.post('https://connect.data.com/dwr/call/plaincall/SearchDWR.singleBoxSearch.dwr', data=search_data, cookies={'DWRSESSIONID':dwrsessionid})
    response_string = response.text
    # My hacky code. I'm sure there is a better way...
    split1 = response_string.split('resultList:[')
    split2 = split1[1].split("},{")
    employee_names = re.findall('name:"(.*?)"', str(split2), re.DOTALL)
    companyCount = len(employee_names)
    return companyCount,employee_names

#search employees based on company
def employee_search():
    pass

def connection(email, password, companyName):
    client = requests.Session()
    login(client, email, password)
    companyCount,employee_names = company_search(client,companyName)

    print('\n Company Name: '+companyName+
            '\n Employees: ' + str(companyCount))

    output = 'dataScrape-data/' + companyName + '_' + timestr + '.txt'
    outputTitle = 'dataScrape-data/'+companyName+'_employee-title_'+timestr+'.txt'#

    print(' Formatting userlist...\n')
    for name in employee_names:
        firstName = name.split(', ')[1]
        lastName = name.split(', ')[0]
        employee = firstName + ' ' + lastName
        with open(output, 'a') as f:
            f.write(employee + '\n')
        #with open(outputTitle, 'a') as f:
        #        f.write(employee + ' : ' + userlocation + ' : ' + occupation + '\n')

    if not os.path.isfile(output):
        print(" No employees parsed...")
        print(" Exiting...")
        sys.exit(2)#

    print(" [*]Raw Employee list Saved to: " + output)
#    print(" [*]Employee w/ Title list Saved to: " + outputTitle)#

    return companyName,output

def name(companyName, output, formatValue, domain):
    filename = "dataScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"

    if not os.path.isfile(output):
        print(" File not found...")
        print(" Exiting...")
        sys.exit(2)

    names = []
    #generate a list of first and last name, then call mangle
    for line in open(output, 'r'):
        full_name = ''.join([c for c in line if  c == " " or  c.isalpha()])
        full_name = full_name.lower().split()
        names.append([full_name[0], full_name[-1]])

    if formatValue == 1:
        newname = mangleOne(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 2:
        newname = mangleTwo(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 3:
        newname = mangleThree(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 4:
        newname = mangleFour(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 5:
        newname = mangleFive(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 6:
        newname = mangleSix(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 7:
        newname = mangleSeven(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 8:
        newname = mangleEight(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 9:
        newname = mangleNine(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 10:
        newname = mangleTen(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 11:
        newname = mangleEleven(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 12:
        newname = mangleTwelve(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 13:
        newname = mangleThirteen(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 14:
        newname = mangleFourteen(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 15:
        newname = mangleFifteen(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 16:
        newname = mangleSixteen(names, companyName, timestr, domain, filename)
        # print(newname)
    elif formatValue == 99:
        mangleAll(names, companyName, timestr, domain, filename)
    else:
        sys.exit(2)

    print(' [*]Mangled option chosen: '+ str(formatValue))
    print(' [*]Mangled list Saved to: '+filename)

if __name__ == "__main__":
    print(banner)
    args = parse_args()
    cls()
    print(banner)

    if not os.path.exists("dataScrape-data/"):
        os.mkdir("dataScrape-data/")
    if args.input:
        name(args.company, args.input, args.mangle, args.domain)
    else:
        company,output = connection(args.email, args.password, args.company)
        name(company, output, args.mangle, args.domain)
        print "\n Completed in: %.1fs\n" % (time.time() - curr_time)

