"""
prac 7 project_management
expected time: 60 minutes
8:32
Expected 60 minutes, was actually ()
"""

import datetime
from prac_07.project import Project


def main():
    filename = "projects.txt"
    projects = load_file(filename)
    print(projects)


def load_file(filename):
    projects = []
    in_file = open(filename)
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        # print(parts)
        # start_time = [parts[1][:2], parts[1][3:5], parts[1][-4:]]
        # print(start_time)
        projects.append(Project(*parts))
    in_file.close()
    return projects


main()
