"""
Implements the specialized (derived) class for a Project Lead
"""
from swDeveloper import SwDeveloper

class ProjectLead(SwDeveloper):
    # Update the class definition as per the instructions in the PDF
    def __init__(self, developerId, name, email, hourlyRate, weeklyHours, projectCount):
        super().__init__(developerId, name, email, hourlyRate, weeklyHours)
        self.projectCount = projectCount
        
    def __str__(self):
        return super().__str__ + f"\nProject Count: {self.projectCount}"
    
    def weeklyEarnings(self):
        base_earnings = super().weeklyEarnings()
        regular_earnings = base_earnings * self.projectCount
        project_compensation = 0.3 * regular_earnings
        return base_earnings + project_compensation