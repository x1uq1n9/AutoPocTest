import shodan

api = shodan.Shodan('EEFr2PmVoBV33oRnLuoXs4fmqeWafcJV')
# query = '''header="Falcon Web Server"'''
query = "131.111.15.240"
# host = api.host('131.111.15.240')
cursor = api.search_cursor(query)
for info in cursor:
    info = info
    print(info)
# vulns = info['vulns']
# for cve in vulns.keys():
#     print(cve)