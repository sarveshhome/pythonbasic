# import xml.etree.ElementTree as ET
# data = '''
# <person>
# <name>Chuck</name>
# <phone type="intl">
# +1 734 303 4456
# </phone>
# <email hide="yes" />
# </person>'''
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))


#

import json
data = '''
[
{ "id" : "001",
"x" : "2",
"name" : "Chuck"
} ,
{ "id" : "009",
"x" : "7",
"name" : "Brent"
}
]'''
info = json.loads(data)
print(info)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])