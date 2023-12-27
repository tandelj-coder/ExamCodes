"""
Implements the general (base) class for a software developer
"""


class SwDeveloper:
    def __init__(self, developerId, name, email, hourlyRate, weeklyHours):
        if not developerId.strip():
            raise ValueError("Developer ID cannot be Blank")
        self._developerId = developerId # unique identification number
        self._name = name # The name of the developer
        self._email = email # Developer's email
        self._hourlyRate = hourlyRate # Per hour earnings of the developer
        self._weeklyHours = weeklyHours # Weekly work hours of the developer
        self.language_known = set()

    def addLanguage(self, new_language):
        if not new_language.strip():
            raise ValueError("Language anme cannot be blank.")
        if new_language in self.language_known:
            raise ValueError("Language already known")
        
        self.language_known.add(new_language)

    # Update the class definition as per the instructions in the print document
    def get_developer_id(self):
        return self._developerId
    
    def set_email(self, new_email):
        if "@" in new_email and not new_email.startswith("@"):
            self._email = new_email
        else:
            raise ValueError("Invalid email format. Must contain '@ and not start with '@'")
    
    def __str__(self):
        return f"Developer ID: {self._developerId} \nDeveloper Name: {self._name} \nDeveloper Email: {self._email} \nHourly Rate: {self._hourlyRate} \nWeekly Hours: {self._weeklyHours}"

    def weeklyEarnings(self):
        return self._hourlyRate * self._weeklyHours