# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:27:41 2018

@author: nkanak
"""

import json
from jira import JIRA

jira = JIRA('https://issues.apache.org/jira')

# Get all projects.
projects = jira.projects()

# Get HADOOP project details.
hadoop = jira.project('HADOOP')

# Save HADOOP project details.
with open('hadoop_data.json', 'w') as f:
    json.dump({'hadoop': hadoop.raw}, f, indent=2)

# Get all HADOOP issues.
hadoop_issues = jira.search_issues('project=HADOOP', maxResults=10000, json_result=True)

# Save HADOOP issues to JSON file.
with open('hadoop_issues.json', 'w') as f:
    json.dump({'issues': hadoop_issues['issues']}, f, indent=2)