#data will be written to the output.json file(not appended)
#A new file will be created each time
#expecting logs.log to contain data in the provided correct format
#no error handling for simplicity
#also printing out the resultant list for reference
#if file reading faails, an error message will be displayed
import json
logs = []
try:
    with open('logs.log', 'r') as file:
        for line in file.readlines():
            if len(line.split(' - ')) >= 4:
                d = dict()
                if "error" in line.split(' - ')[2].lower() or "warning" in line.split(' - ')[2].lower():
                    d['Date'] = line.split(' - ')[0]
                    d['Type'] = line.split(' - ')[2]
                    d['Message'] = line.split(' - ')[3]
                    logs.append(d)
    print("The following data will be appended to output.json file\n\n")
    for x in logs:
        for y,z in x.items():
            print(y," : ",z)
    with open('output.json', 'w+', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=4)
except:
    print("something went wrong")


"""
Output:
The following data will be appended to output.json file


Date  :  2015-05-22 16:48:48,180
Type  :  ERROR
Message  :  Failed: Waiting for files the Files from Cloud Storage: gs://folder/folder/

Date  :  2015-05-22 16:48:48,180
Type  :  WARNING
Message  :  Starting: Attempt 2 Checking for New Files from gs://folder/folder/

"""

