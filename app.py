import os
import pathlib
import json
import argparse
import xml.etree.ElementTree as ET
from utils.display import print_message, Colors

def main():
    """
    The main context of the application.
    Purpose: Converts LoadRunner correlation rules to Blazemeter Correlation Recorder Plugin format
    @Input: LoadRunner Correlation file (*.cor)
    @Output: Blazemeter Correlation Recorder Rules Template (*.json)
    Author: NaveenKumar Namachivayam | QAInsights.com
    """
    try:
        parser = argparse.ArgumentParser(
            description='Convert LoadRunner Correlation Rules to JMeter'
        )
        required_named = parser.add_argument_group('mandatory arguments')
        required_named.add_argument(
            "-f",
            "--file",
            dest="corfile",
            help="Add Correlation file path"
        )
        args = parser.parse_args()
        cor = args.corfile

        # File Rename from *.cor to *.xml
        lr_cor_file = cor
        base = os.path.splitext(lr_cor_file)[0]
        lr_cor_file_renamed = base + ".xml"
        os.rename(lr_cor_file, lr_cor_file_renamed)

        # Get Inputs from user
        get_id = str(input("Enter id - [default: 1.0]: ") or "myrules")
        get_description = str(input("Enter description - [default: Inception version for my rules]: ") or "1.0")
        get_version = str(input("Enter the version - [default: 1.0]: ") or "1.0")
        get_components = str(input(
            "Enter the components - [default: com.blazemeter.jmeter.correlation.siebel.SiebelCounterCorrelationReplacement]:") 
            or "com.blazemeter.jmeter.correlation.siebel.SiebelCounterCorrelationReplacement"
            )
        get_response_filters =  str(input("Enter the version - [default: text/html]: ") or "text/html")

        # Root element of cor file
        root = ET.parse(lr_cor_file_renamed).getroot()
        
        # Iterate through each group
        # Loops only one time
        for group in root.iter('Group'):
            group_name = group.attrib['Name']
            break

        # Boiler Plate
        create_jmeter_rule(group_name,get_id, get_description, get_version, get_components, get_response_filters)
        # Create Rules
        fetch_rules(root, group_name,get_id, get_version)
        # Create Repository File
        create_repository(get_id, get_version, group_name)

        # Reverting the file name
        lr_cor_file = lr_cor_file_renamed 
        base = os.path.splitext(lr_cor_file)[0]
        lr_cor_file_renamed = base + ".cor"
        os.rename(lr_cor_file, lr_cor_file_renamed)

    except FileNotFoundError as e:
        print_message(e, message_color="red")

def create_repository(get_id, get_version, group_name):
    """
    Creating a repository for the rules
    """
    data = {
        get_id : {
            "versions": [
                get_version
            ]
        }
    }
    repository_file_name = group_name + '/' + get_id + '-repository.json'
    os.makedirs(os.path.dirname(repository_file_name), exist_ok=True)
    with open(repository_file_name,"w+") as f:
        json.dump(data, f)
    f.close()
    
    message = "Repository file has been created: " + repository_file_name
    print_message(message, message_color="green")
    #print_message(f"{message}","green")

def create_jmeter_rule(group_name,get_id, get_description, get_version, get_components, get_response_filters):
    """
    Create JSON file structure
    @param  group_name: the name of rules group
    @param  get_id: the id of the rules
    @param  get_description: the description of the rules
    @param  get_version: the version of the rules
    @param  get_components: the components of the rules
    @param  get_response_filters: the response filter for the rules
    @return json file structure
    """
    data = {
        'id': get_id,
        'description': get_description,
        'version': get_version,
        "components": get_components,
        "responseFilters": get_response_filters,
        "rules": [
        ], 
        "repositoryId": "local"
    }
    
    json_file_name = group_name + '/' + get_id + '-' + get_version + '-template' + '.json'
    os.makedirs(os.path.dirname(json_file_name))
    # Create JSON File
    with open(json_file_name,"w+") as f:
        json.dump(data, f)
    f.close()
    #print("Rules has been created: ", json_file_name)
    message = "Rules has been created: " + json_file_name
    print_message(message, message_color="green")
    
    return

def fetch_rules(root, group_name, get_id, get_version):
    """
    @param  root: the root element in cor file
    @param  group_name: the name of rules group
    @param  get_id: the id of the rules
    @param  get_version: the version of the rules
    @return each rule, left boundary, right boundary from the cor file
    """
    #print(f"Group name is  {group_name}")

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
        json_file_name = group_name + '/' + get_id + '-' + get_version + '-template' + '.json'
        # Adding each rule to the json
        add_rules_to_json(json_file_name, rule_name, full_regex)
        #print(full_regex)

    return

def add_rules_to_json(json_file_name, rule_name, full_regex):
    """
    @param  json_file_name: the json file name
    @param  rule_name: the rule name
    @param  full_regex: the full regex
    @retuen append rules to json
    """
    with open(json_file_name) as json_file:        
        data = json.load(json_file)
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
        temp = data['rules']
        temp.append(rules_data)
    # Appends each rule to the JSON
    write_json(data, json_file_name)

    return

def write_json(data, json_file_name): 
    """
    @param  data: boilerplate for the rules
    @param  json_file_name: json file name
    @return complete json file
    """
    with open(json_file_name,'w') as f: 
        json.dump(data, f, indent=4) 
    
if __name__ == "__main__":
    main()