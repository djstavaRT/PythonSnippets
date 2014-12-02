__author__ = 'djstava'

#!/usr/bin/env python
#coding=utf-8

import json

#Function:Analyze json script
#Json is a script can descript data structure as xml,
#for detail, please refer to "http://json.org/json-zh.html".

#Note:
#1.Also, if you write json script from python,
#you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}
#f = file("temp.json");
#s = json.load(f)
#print s
#f.close

#json string:
s = json.loads('{"name":"djstava", "type":{"name":"djstavaRT", "parameter":["sex", "age"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]

