from google import search
import optparse

def docExposed(site):
    doc_exposed = 'site:'+site+' ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'
    return search(doc_exposed, extra_params={'filter': '0'})
def dirListing(site):
    dir_listing = "site:"+site+" intitle:index.of"
    return search(dir_listing, extra_params={'filter': '0'})
def confExposed(site):
    conf_exposed = "site:"+site+" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"
    return search(conf_exposed, extra_params={'filter': '0'})
def dbExposed(site):
    db_exposed = "site:"+site+" ext:sql | ext:dbf | ext:mdb"
    return search(db_exposed, extra_params={'filter': '0'})
def logExposed(site):
    log_exposed = "site:"+site+" ext:log"
    return search(log_exposed, extra_params={'filter': '0'})
def bkExposed(site):
    bk_exposed = "site:"+site+" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
    return search(bk_exposed, extra_params={'filter': '0'})
def loginPage(site):
    login_page = "site:"+site+" inurl:login"
    return search(login_page, extra_params={'filter': '0'})
def sqlError(site):
    sql_error = 'site:'+site+' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'
    return search(sql_error, extra_params={'filter': '0'})
def phpInfo(site):
    php_info = 'site:'+site+' ext:php intitle:phpinfo "published by the PHP Group"'
    return search(php_info, extra_params={'filter': '0'})

def printList(list):
    for l in list:
        print l

def main():
    parser = optparse.OptionParser("usage%prog -u <site> -t <technique>")
    parser.add_option('-u', dest='target', type='string', help='Target site')
    parser.add_option('-t', dest='technique', type='int', help='Google hack techniques to use')
    (options, args) =parser.parse_args()
    if options.target == None:
        print parser.usage
        exit(0)
    else:
        site = options.target
        technique = 1

    if technique == 1:
        printList(docExposed(site))
    elif technique == 2:
        printList(dirListing(site))
        printList(confExposed(site))
        printList(dbExposed(site))
        printList(logExposed(site))
        printList(bkExposed(site))
        printList(loginPage(site))
        printList(sqlError(site))
        printList(phpInfo(site))
    elif technique == 3:
        printList(docExposed(site))
        printList(dirListing(site))
        printList(confExposed(site))
        printList(dbExposed(site))
        printList(logExposed(site))
        printList(bkExposed(site))
        printList(loginPage(site))
        printList(sqlError(site))
        printList(phpInfo(site))
    else:
        print '[-] Technique Type Error'
        print parser.usage
        exit(0)

if __name__ == "__main__":
    main()
