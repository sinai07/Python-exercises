# A function that prints hello world
def hello_world():
    print("hello_world")

# This line calls (runs) the function
hello_world()

# To translate
# First, we need to tell python to use the boto3 package we installed 

import boto3 

#we need to tell python which specific service we want to use within the boto3 package
client = boto3.client("translate") 

# declare the function using def, name, braces for parameters and a colon 

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='es' 
)
#### Add the new text below this line ####

    print(response)
#this code is inside the function and will print the contents of the variable 'response' 

translate_text()


#Create a new file called lab_2_intro_to_boto3.py and add the following code:
