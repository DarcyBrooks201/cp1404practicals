"""prac 7, project class"""
import datetime

class Project:
    def __init__(self, name="", start_date="31/12/2000", priority=0, cost_estimate=0.0, completion_percentage=0.0):
        """Construct project object from Name, Start Date, Priority, Cost Estimate, and Completion Percentage"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """String version of project object"""
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __getitem__(self, key):
        """Return part of the object"""
        if key == "name":
            return self.name
        elif key == "start_date":
            return self.start_date
        elif key == "priority":
            return self.priority
        elif key == "cost_estimate":
            return self.cost_estimate
        elif key == "completion_percentage":
            return self.completion_percentage

    def __setitem__(self, key, value):
        """Change part of the object"""
        if key == "name":
            self.name = value
        elif key == "start_date":
            self.start_date = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        elif key == "priority":
            self.priority = value
        elif key == "cost_estimate":
            self.cost_estimate = value
        elif key == "completion_percentage":
            self.completion_percentage = value

    def project_original_string(self):
        """Original string version of project"""
        return f"{self.name}    {self.start_date}   {self.priority} {self.cost_estimate}    {self.completion_percentage}"
