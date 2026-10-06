'''
#BMI Scenario->Link with Exception handling with usage of while
while <condition>:
    statement(S)....
    .........


while True:
        #Now we are gonna link BMI case to it with exception handling
    try:
       weight = int(input("enter the weight in kgs:"))
       height = float(input("enter the height in meters:"))
       if weight > 0 and height > 0:
               # print(weight,height)
          break
       else:
             print("value must be postive")
    except Exception as e:
            print(e)
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Category: Underweight -> Eat well")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Category: Healthy -> Keep consistent")
elif bmi >= 25 and bmi <= 29.9:
    print("Category: Overweight -> Start exercising")
elif bmi >30:
    print("you are in obese category and bmi is {bmi}")

-----------------
user_details = {}
user_details = {'weight':[],
                'height':[]}
for i in range(10):
    while true:
        try:
            weight = int(input("enter the weight in kgs:"))
            height = float(input("enter the height in meters:"))
            if weight > 0 and height > 0:
                 user_details = ['weight'].append(weight)
                 user_details = ['height'].append(height)
            
            else:
                print("value must be postive")
        except Exception as e:
              print(e)


bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Category: Underweight -> Eat well")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Category: Healthy -> Keep consistent")
elif bmi >= 25 and bmi <= 29.9:
    print("Category: Overweight -> Start exercising")
elif bmi >30:
    print("you are in obese category and bmi is {bmi}")
print(user_details)    

#File handling ->create files,make some changes over files
    #we will use open(),with()->.txt files
    #we have different modes -> 'r','w','a','r+'
#first we will create a.txt file and write some content to it --->'r'
#file =open('second.txt','r')
#print(file)
#NOW to read content from the file
#print(file.read())
#print(file.readline())#read a single line from the line
#print(file.readlines())#read list of lines
#'w' mode -> it automatically creates a new line and if same file is existing
#it overides
file = open('meenakeshi.txt','w')
print(file)
#print(file.read()) #it is not readable
file.write('vishalakshi,swapna and kick are friends')
file.close()#Once the file is closed then only tha data is written to file


#we can use with keyword
with open('second.txt','w') as file:
    #print(file)# in this case we already second.txt file the content is overide
    file.write('I am good')
    file.write('I love ampolu')
    file.write('\n But she so beautiful')#no need for usage of close() content will be directly written

data = ['codegnan','python','vizag','pfs']
data.append('\n Agentic AI')
#with open('qw.txt','w') as file:
    #file.write(data) in this case write() fails as it needs only str
   # for text in data:
        #file.write(text)

with open('asdf.txt','w') as file:
    file.writelines(data)#this can directly insert the data from the list

#'a'--> will create a new file,if file is already existing content will
#be added instead of over rideing
with open('asdf.txt','a') as f:
    f.write('\n hello')

#'r'-->perform both read  and write operations
with open('asdf.txt','r+') as f:
    print(f.read())
    f.write()
    f.write('\n webinar is very imporatant')
user_details = {}
user_details = {'weight':[],
                'height':[]}
for i in range(10):
    while True:
        try:
            weight = int(input("enter the weight in kgs:"))
            height = float(input("enter the height in meters:"))
            if weight > 0 and height > 0:
                 user_details = ['weight'].append(weight)
                 user_details = ['height'].append(height)
        except Exception as e:
              print(e)

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Category: Underweight -> Eat well")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Category: Healthy -> Keep consistent")
elif bmi >= 25 and bmi <= 29.9:
    print("Category: Overweight -> Start exercising")
elif bmi >30:
    print("you are in obese category and bmi is {bmi}")
    
else:
    print("value must be postive")
       
print(user_details)
'''


dict_ = {'name' : [],
         'weight' : [],
         'height' : [],
         'unit' : [],
         'bmi' : [],
         'category' : []
}
n_ = int(input("Enter number of users: "))
for i in range(n_):
    name = input("Enter the user name: ")
    dict_["name"].append(name)
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))

            if weight > 0:
                dict_["weight"].append(weight)
                break
            else:
                print("Weight must be positive")

        except ValueError:
            print("Please enter a valid number")


    while True:
        try:
            unit = input("Enter height unit (feet/cm/inches/meters): ").lower()
            height = float(input("Enter your height: "))

            if height > 0:

                if unit == "feet" or unit == "feets":
                    height_m = height * 0.3048

                elif unit == "cm":
                    height_m = height / 100

                elif unit == "inches":
                    height_m = height * 0.0254

                elif unit == "meters":
                    height_m = height

                else:
                    print("Invalid height unit")
                    continue
                dict_["height"].append(height)
                dict_["unit"].append(unit)
                break

            else:
                print("Height must be positive")

        except ValueError:
            print("Please enter a valid number")


    bmi = weight / (height_m ** 2)

    dict_["bmi"].append(round(bmi, 2))
    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal weight"

    elif bmi < 30:
        category = "Overweight"

    else:
        print("Obesity")
    dict_['category'].append(category)
print(dict_)




