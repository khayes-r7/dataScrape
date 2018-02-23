#!/usr/bin/env python2
import os.path

def write(companyName, timestr, newname, first_name, last_name, filename):
    with open(filename, 'a') as f:
        f.write(newname+"\n")

    msfpath = 'dataScrape-data/'+companyName+'-'+timestr+'-msfpro.csv'
    if not os.path.isfile(msfpath):
        with open(msfpath, 'a') as f:
            f.write('email_address,first_name,last_name\n')
    with open(msfpath, 'a') as f:
        f.write(newname+','+first_name.title()+','+last_name.title()+'\n')

def mangleOne(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname=first_name + last_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleTwo(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name + first_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleThree(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name + "." + last_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames


def mangleFour(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name + "." + first_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleFive(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name + "_" + last_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleSix(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name + "_" + first_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames


def mangleSeven(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name[0] + last_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleEight(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name[0] + first_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleNine(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name + last_name[0]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames


def mangleTen(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name[0] + "." + last_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleEleven(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name[0] + "." + first_name
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleTwelve(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name[0:3] + first_name[0:2]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames


def mangleThirteen(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name[0:4] + first_name[0:3]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleFourteen(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = first_name[0] + last_name[0:7]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleFifteen(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name + first_name[0]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleSixteen(names, companyName, timestr, domain, filename):
    newnames = []
    for name in names:
        first_name = name[0]
        last_name = name[1]
        newname = last_name[0:3] + first_name[0:2]
        if domain != '':
            newname = newname+"@"+domain
            write(companyName, timestr, newname, first_name, last_name, filename)
        else:
            write(companyName, timestr, newname, first_name, last_name, filename)
        newnames.append(newname)
    return newnames

def mangleAll(names, companyName, timestr, domain, filename):
    newnames = []
    newname = mangleOne(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleTwo(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleThree(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleFour(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleFive(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleSix(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleSeven(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleEight(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleNine(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleTen(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleEleven(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleTwelve(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleThirteen(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleFourteen(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleFifteen(names, companyName, timestr, domain, filename)
    print(newname)
    newname = mangleSixteen(names, companyName, timestr, domain, filename)
    print(newname)

if __name__ == '__main__':
    pass

