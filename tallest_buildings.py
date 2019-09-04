'''
Created on Aug 30, 2019

@author: Mahsum
'''

tallest_buildings_table_header = ["Rank","Building","City","Country","Height","Floors","Built"]

tallest_buildings_table_content = [
    ["1","Burj Khalifa",                "Dubai",            "United Arab Emirates", "828 m",    "163",  "2010"],
    ["2","Shanghai Tower",              "Shanghai",         "China",                "632 m",    "128",  "2015"],
    ["3","Abraj Al-Bait Clock Tower",   "Mecca",            "Saudi Arabia",         "601 m",    "120",  "2012"],
    ["4","Ping An Finance Centre",      "Shenzhen",         "China",                "599 m",    "115",  "2017"],
    ["5","Lotte World Tower",           "Seoul",            "South Korea",          "554.5 m",  "123",  "2016"],
    ["6","One World Trade Center",      "New York City",    "United States",        "541.3 m",  "104",  "2014"],
    ["7","Guangzhou CTF Finance Centre","Guangzhou",        "China",                "530 m",    "111",  "2016"],
    ["8","Tianjin CTF Finance Centre",  "Tianjin",          "China",                "530 m",    "98",   "2018"],
    ["9","China Zun",                   "Beijing",          "China",                "528 m",    "108",  "2018"],
    ["10","Taipei 101",                 "Taipei",           "Taiwan",               "508 m",    "101",  "2004"]
    ]

print("******************** Before Sorting **************************")

print(tallest_buildings_table_header)
for row in tallest_buildings_table_content:
    for elem in row:
        print(elem, end=' ')
    print()
    
print("******************** Answer 1: Sort by any columns **************************")

tallest_buildings_table_content.sort(key=lambda x:x[4], reverse=True) #sort by column number. 4 is Height. Default order is ascending(False)

for row in tallest_buildings_table_content:
    for elem in row:
        print(elem, end=' ') #format by space
    print() #new line

print("******************** Answer 2: Returns the oldest building **************************")

tallest_buildings_table_content.sort(key=lambda x:x[6])
print(tallest_buildings_table_content[0][1])

print("******************** Answer 3: Returns the country that have biggest number of tall buildings **************************")
country_list=[]
country_dict = {}

for line in tallest_buildings_table_content:
    country_list.append(line[3])
    
for a in country_list:
    country_dict[a] = country_list.count(a)

print(sorted(country_dict.items(), key=lambda x: x[1], reverse=True)[0][0]) #Country that has more number of tall buildings
