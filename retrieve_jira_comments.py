# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 23:58:10 2018

@author: nkanak
"""

import json
from jira import JIRA

jira = JIRA('https://issues.apache.org/jira')

# Save HADOOP issues to JSON file.
with open('hadoop_issues.json') as f:
    issues = json.load(f)['issues']

comments = dict((issue['key'], [comment.raw for comment in jira.comments(issue['key'])]) for issue in issues)

with open('hadoop_issues_comments.json', 'w') as f:
    json.dump(comments, f, indent=2)
