"""prac 7, project class"""


class Project:
    def __init__(self, name="", start_date="31/12/2000", priority=0, cost_estimate=0.0, completion_percentage=0.0):
        """Construct project object from Name, Start Date, Priority, Cost Estimate, and Completion Percentage"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """String version of project object"""
        return f"({self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage})"
