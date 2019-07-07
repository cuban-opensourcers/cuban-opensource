#!/usr/bin/python3

import json

def parse_category(c, level=2):
    category_name = c['name']

    lines = ["#"*level + " " + category_name + '\n']

    if 'data' in c:
        for sc in c['data']:
            lines += parse_category(sc, level+1)
            
    
    if 'projects' in c:
        for p in c['projects']:
            lines.append(parse_project(p))
        lines.append('\n')


    return lines


def parse_project(p):
    return "- [{name}]({url}): {description}".format(name=p["name"], url=p["url"], description=p["description"])

with open("data.json") as json_file:
    text = json_file.read()
    json_data = json.loads(text)
    
    lines = [
    "# Cuban Open Source Projects\n",
    "![Cuban Open Source Projects](https://repository-images.githubusercontent.com/192082154/31c31d80-8f7f-11e9-95d0-3cd6467c8181)\n",
    "Awesome list of Cuban open source projects. Just to know what is being openly developed in Cuba...\n"
    ]

    for c in json_data['data']:
        lines += (parse_category(c))
    
    with open('README.md', 'w') as output_file:
        output_file.write("\n".join(lines))

