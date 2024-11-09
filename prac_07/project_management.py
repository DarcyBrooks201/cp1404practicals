"""
prac 7 project_management
expected time: 60 minutes
8:32 - 9:27
9:50 - 10:07
10:24 -
Expected 60 minutes, was actually ()
"""

import datetime
from prac_07.project import Project


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
            projects.sort(key=lambda project: project.priority)
            print("Incomplete projects:")
            for project in projects:
                if project["completion_percentage"] != 100:
                    print(project)
            print("Complete projects:")
            for project in projects:
                if project["completion_percentage"] == 100:
                    print(project)
            display_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "F":
            min_start_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            min_start_date = datetime.datetime.strptime(min_start_date_string, "%d/%m/%Y").date()
            projects.sort(key=lambda project: project.start_date)
            for project in projects:
                start_date = project["start_date"]
                if start_date >= min_start_date:
                    print(project)
            display_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "A":
            add_project(projects)
            display_menu()
            menu_choice = input(">>> ").upper()
        elif menu_choice == "U":
            update_project(projects)
            display_menu()
            menu_choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {filename}? ").upper()
    if save_choice == "Y":
        save_file(filename, projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    """Update a project's priority and completion percentage, can be left blank to not change"""
    project_number = 0
    for project in projects:
        print(f"{project_number} {project}")
        project_number += 1
    project_choice = int(input("Project choice: "))
    while project_choice < 0 or project_choice > (len(projects) - 1):
        print("Invalid project choice")
        project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage_string = input("new completion percentage: ")
    if new_percentage_string != "":
        new_percentage = int(new_percentage_string)
        projects[project_choice]["completion_percentage"] = new_percentage
    new_priority_string = input("new priority: ")
    if new_priority_string != "":
        new_priority = int(new_priority_string)
        projects[project_choice]["priority"] = new_priority


def add_project(projects):
    """Add a new project to list of projects"""
    name = input("name: ")
    start_date = input("start date (dd/mm/yyyy): ")
    priority = int(input("priority: "))
    cost_estimate = float(input("cost estimate: "))
    completion_percentage = int(input("completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def display_menu():
    """Display menu options"""
    print(
        "(L)oad projects, (S)ave projects, (D)isplay projects, (F)ilter projects by date, (A)dd new project, (U)pdate project, (Q)uit")


def load_file(filename):
    """Get project information from a file"""
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
    """Save project information to a file"""
    out_file = open(filename, "w")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        print(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=out_file)
    out_file.close()
    print(f"Successfully saved {len(projects)} projects to {filename}")


main()
