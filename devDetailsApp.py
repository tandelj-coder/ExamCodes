"""
Implements interaction with the end user and drives the application logic
"""
import csv
from swDeveloper import SwDeveloper
from projectLead import ProjectLead

class DevDetailsApp:
    def __init__(self):
        self.developers = []

    def addSoftwareDeveloper(self):
        developerId = input("Enter Developer ID: ")
        name = input("Enter name: ")
        email = input("Enter Email: ")
        hourlyRate = float(input("Enter Hourly Rate: "))
        weeklyHours = int(input("Enter Weekly Hours: "))
        developer = SwDeveloper(developerId, name, email, hourlyRate, weeklyHours)
        self.developers.append(developer)

    def addProjectLead(self):
        developerId = input("Enter Developer ID: ")
        name = input("Enter name: ")
        email = input("Enter Email: ")
        hourlyRate = float(input("Enter Hourly Rate: "))
        weeklyHours = int(input("Enter Weekly Hours: "))
        projectCount = int(input("Enter the Project Count: "))
        project_lead = ProjectLead(developerId, name, email, hourlyRate, weeklyHours, projectCount)
        self.developers.append(project_lead)

    def showWeeklyEarnings(self):
        developerId = input("Enter Developer ID: ")
        found = False
        for developer in self.developers:
            if developer.get_developer_id() == developerId:
                found = True
                print(developer)
                print(f"Weekly Earnings: {developer.weeklyEarnings()}")
                break
            if not found:
                print("No matching Developer ID found")
    
    def saveToCSV(self):
        with open('developers.csv', 'w', newline='') as csvfile:
            fieldnames = ['Developer ID', 'Name', 'Email', 'Hourly Rate', 'Weekly Hours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for developer in self.developers:
                writer.writerow({
                    'Developer ID': developer.get_developer_id(),
                    'Name': developer.name,
                    'Email': developer.email,
                    'Hourly Rate': developer.hourlyRate,
                    'Weekly Hours': developer.weeklyHours
                })

    def addLanguageToDeveloper(self):
        developerId = input("Enter Developer ID: ")
        language = input("Enter new language: ")

        found = False
        for developer in self.developers:
            if developer.get_developer_id() == developerId:
                found = True
                try:
                    developer.addLanguage(language)
                    print("Language added successfully")
                except ValueError as e:
                    print(f"Error: {e}")
                break

        if not found:
            print("No matching Developer ID found.")
    
    def main(self):
        # Update the class definition as per the instructions in the Print Document
        print("Employee Details Manager: Jigar Tandel")
        while True:
            print("\nMain Menu:")
            print("a. Add Software Developer")
            print("b. Add Project Lead")
            print("c. Show Weekly Earnings")
            print("d. Exit")

            choice = input("Enter your choice: ")
            
            try:
                if choice == 'a':
                    self.addSoftwareDeveloper()
                elif choice == 'b':
                    self.addProjectLead()
                elif choice == 'c':
                    self.showWeeklyEarnings()
                elif choice == 'd':
                    break
                else:
                    print("Invalid choice. Please select a, b, c or d")
            except ValueError as e:
                print(f"Error: {e} Please try again.")

                self.saveToCSV()
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    # call the main method
    app = DevDetailsApp.main()
    app.main()
