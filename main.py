#INSTALL ALL THE REQUIREMENTS

# pip install requests
# pip install bs4

# STEP 1:- IMPORT MODULES
import requests   # "REQUEST" MODULE DEFINES FUNCTIONS AND CLASSES WHICH HELP IN OPENING URL'S.
import bs4        # HERE "BEAUTIFUL SOUP" MODULE DEFINES FUNCTIONS AND CLASSES WHICH HELP TO PARSE THE HTML TEXT IN A PROPER READABLE FORMAT.

# STEP 2:- INPUT THE URL
url = input("enter your url ")
response = requests.get(url) # WHEN OUR REQUEST GETS APPROVED AND WE WILL GET RESPONSE FROM THE SERVER OF THE GIVEN URL 

print(type(response))
# print(response.text)  # HERE WE PRINTED THE RESPONSE TEXT FROM THE SERVER.

# STEP 3:- PARSE THE HTML
filename = "temp.html"   # HERE WE CREATED TEMPORARY HTML FILE TO SAVE THE REQUESTED CONTENT FROM THE URL.
bs = bs4.BeautifulSoup(response.text,"html.parser") # HERE WE CREATED "bs4" OBJECT TO PARSE THE HTML TEXT IN A READABLE FORMAT 

formatted_text = bs.prettify() # HERE prettify() METHOD WILL TURN A BEAUTIFUL SOUP PARSE TREE INTO A NICELY FORMATTED UNICODE STRING, WITH A SEPERATE LINE FOR EACH TAG AND EACH STRING.
print(formatted_text)

with open(filename, "w+") as f:  # HERE "with" KEYWORD IS USED FOR AUTOMATICALLY OPENS THE FILE USING "open() FUNCTION AS A WRITEABLE MODE.
    f.write(formatted_text)

# STEP 4:- FIND THE TAGS.
list_imgs = bs.find_all('img')  # HERE WE USED find_all() function TO FIND ALL THE "IMG" TAGS IN A FORMATTED HTML TEXT 
print(list_imgs)

no_of_imgs = len(list_imgs) # HERE WE PRINTED LENGTH OF THE IMG TAGS

list_as = bs.find_all('a') # HERE WE USED find_all() function TO FIND ALL THE "ANCHOR" TAGS IN A FORMATTED HTML TEXT 
no_of_as = len(list_as)

print("no of img tags", no_of_imgs)
print("no of anchor tags", no_of_as)
