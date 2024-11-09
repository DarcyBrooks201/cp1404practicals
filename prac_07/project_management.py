"""
prac 7 project_management
expected time: 60 minutes
8:32 - 9:27
9:50 - 10:07
10:24 -
Expected 60 minutes, was actually ()
"""

import datetime
from turtledemo.penrose import start

from prac_07.project import Project


# TODO Add docstrings to functions

def main():
    filename = "projects.txt"
    projects = load_file(filename)
    display_menu()
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Filename: ")
            projects = load_file(filename)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "S":
            filename = input("Filename: ")
            save_file(filename, projects)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "D":
            # TODO add sorting
            # projects.sort(project[2])
            print("Incomplete projects:")
            for project in projects:
                if project["completion_percentage"] != 100:
                    print(project)
            print("Complete projects:")
            for project in projects:
                if project["completion_percentage"] == 100:
                    print(project)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "F":
            #TODO complete
            pass
            menu_choice = input(">>> ").upper()
        elif menu_choice == "A":
            add_project(projects)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "U":
            update_project(projects)
            menu_choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {filename}?").upper()
    if save_choice == "Y":
        save_file(filename, projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    project_number = 0
    for project in projects:
        print(f"{project_number} {project}")
        project_number += 1
    project_choice = int(input("Project choice"))
    while project_choice < 0 or project_choice > len(projects):
        print("Invalid project choice")
        project_choice = int(input("Project choice"))
    print(projects[project_choice])
    new_percentage = int(input("new percentage: "))
    if new_percentage != "":
        projects[project_choice][4] = new_percentage
    new_priority = int(input("new priority: "))
    if new_priority != "":
        projects[project_choice][2] = new_priority


def add_project(projects):
    name = input("name: ")
    start_date = input("start date: ")
    priority = int(input("priority: "))
    cost_estimate = float(input("cost estimate: "))
    completion_percentage = int(input("completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def display_menu():
    print(
        "(L)oad projects, (S)ave projects, (D)isplay projects, (F)ilter projects by date, (A)dd new project, (U)pdate project, (Q)uit")


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
    print(f"Successfully loaded {len(projects)} projects from {filename}")
    return projects


def save_file(filename, projects):
    out_file = open(filename, "w")
    print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
    for project in projects:
        #TODO fix output
        print(Project.project_original_string(project), file=out_file)
    out_file.close()
    print(f"Successfully saved {len(projects)} projects to {filename}")


main()
