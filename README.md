# Codes_Py_CSharp
A few python codes and a C# Web App that can perform basic CRUD on student data using JSON(no database)


Environment:
Python: 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]

Visual Studio: 
Microsoft Visual Studio Community 2019
Version 16.10.3
Microsoft.AspNetCore.App\3.1.16


data.json is the storage file for the Web App in C#
Live data located in Codes_Py_CSharp\WebApplication2\WebApplication2\wwwroot\data


About the Web Application:
- Built using C# Asp.net Core
- Read data from data.json
- Display as table(check home.png screenshot in Web app screenshots folder)
- Form to add new student
- Same addition form updates the student data if roll number already exists in json
- All fields are mandatory
- Basic error handling implemented
- Search searches using Roll number or substring of name
- if both are entered, first output the row with entered Roll number, followed by the list of rows with name having the searched substring
- If 0 results, show error
- Delete will delete the item with given roll number.
- If roll number doesnt exist in data, delete shows an error message
- Json file being read before each operation to make sure data is live
- Using bootstrap 4.1.3 via cdn
- Any questions, please get back




