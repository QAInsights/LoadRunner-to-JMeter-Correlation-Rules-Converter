import os
import pathlib
import json
import xml.etree.ElementTree as ET

def main():
    lr_cor_file = "./LR.cor"
    lr_cor_file_renamed = "./LR.xml"
    os.rename(lr_cor_file, lr_cor_file_renamed)

    root = ET.parse(lr_cor_file_renamed).getroot()

    for group in root.iter('Group'):
        group_name = group.attrib['Name']

    
    # Boiler Plate
    create_jmeter_rule(group_name)
    # Create Rules
    fetch_rules(root, group_name)
    # Create Repository File
    create_repository(group_name, version)
    # Reverting the file name
    lr_cor_file = "./LR.cor"
    lr_cor_file_renamed = "./LR.xml"
    os.rename(lr_cor_file_renamed, lr_cor_file)

def create_repository(group_name, version="1.0"):
    data = {
        group_name : {
            "versions": [
                version
            ]
        }
    }
    repository_file_name = group_name + '-repository.json'

    with open(repository_file_name,"w+") as f:
        json.dump(data, f)
    f.close()
    print("Repository file created", repository_file_name)

def create_jmeter_rule(group_name):
    '''
    Create JSON file structure
    '''
    data = {
        'id': 'ASP',
        'description': 'desc',
        'version': '1.0',
        "components": "com.blazemeter.jmeter.correlation.siebel.SiebelCounterCorrelationReplacement,\ncom.blazemeter.jmeter.correlation.siebel.SiebelRowCorrelationExtractor,\ncom.blazemeter.jmeter.correlation.siebel.SiebelRowIdCorrelationReplacement,\ncom.blazemeter.jmeter.correlation.siebel.SiebelRowParamsCorrelationReplacement",
        "responseFilters": "text/html",
        "rules": [

        ], 
        "repositoryId": "local"
    }
    
    json_file_name = group_name + '.json'
    
    # Create JSON File
    with open(json_file_name,"w+") as f:
        json.dump(data, f)
    f.close()
    print("File created", json_file_name)
    #print(pathlib.Path(json_file_name).parent.absolute())
    return

def fetch_rules(root, group_name):
    print(f"Group name is  {group_name}")

    for rule in root.iter('Rule'):
        # Rule Name
        rule_name = rule.attrib['Name']
        # Left Boundary
        corr_extractor_lb = rule.attrib['LeftBoundText']
        # Right Boundary
        corr_extractor_rb = rule.attrib['RightBoundText']
        # Constant Regex
        regex = "(.+?)"
        # Complete Regex
        full_regex = corr_extractor_lb + regex + corr_extractor_rb
        
        json_file_name = group_name + '.json'
        print(json_file_name)

        add_rules_to_json(json_file_name, rule_name,full_regex)
        print(full_regex)

    return

def add_rules_to_json(json_file_name, rule_name,full_regex):
    print("Add rules", json_file_name)
    with open(json_file_name) as json_file:        
        data = json.load(json_file)
        print(data['rules'])  
        # Adding Rules Ref names
        rules_data = {
            'referenceName': rule_name,
            'correlationExtractor' : {
                'type' : 'com.blazemeter.jmeter.correlation.core.extractors.RegexCorrelationExtractor',
                'regex' : full_regex,
                'matchNr': 1
            },
            'correlationReplacement' : {
                'type': 'com.blazemeter.jmeter.correlation.core.replacements.RegexCorrelationReplacement',
                'regex' : ''
            }
        }
        #print(rules_data)
        temp = data['rules']
        temp.append(rules_data)
       
    write_json(data, json_file_name)

    return

def write_json(data,json_file_name): 
    with open(json_file_name,'w') as f: 
        json.dump(data, f, indent=4) 

if __name__ == "__main__":
    main()