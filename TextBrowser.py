import requests
import sys
import os
from bs4 import BeautifulSoup
from colorama import Fore

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''




def old():
    global list_old
    user_input = list_old.pop(len(list_old) - 2)

    file_path = os.path.join(args, user_input)
    with open(file_path, 'r') as f:
        print(f.read())



def get_request(url):

    if url.__contains__("https://"):
        return requests.get(url)
    else:
        url = 'https://' + url
        return requests.get(url)




# write your code here
def check_url():
     while True:
        user_input = input().strip()
        if user_input == 'exit':
            sys.exit()
        elif user_input == 'back':
            old()

        elif user_input.count('.') > 0:

            req = get_request(user_input)

            soup = BeautifulSoup(req.content, 'html.parser')
            p = soup.find_all(['p','a','ul','ol','li'])
            for i in p:
                if i.name == 'a':
                        print(Fore.BLUE + i.get_text())
                print(i.text)

            file_name = user_input
            file_path = os.path.join(args, file_name)
            with open(file_path, 'a+') as f:
                for i in p:
                    f.write(i.text)

        else:
            key = user_input.split()
            if len(key) == 1:
                if key[0] in os.listdir(args):
                    file_name = key[0]
                    list_old.append(file_name)
                    file_path = os.path.join(args, file_name)
                    with open(file_path, 'r') as f:
                        print(f.read())
                else:
                    print('Error: Incorrect URL')
            else:
                print('Error: Incorrect URL')



list_old = []

args = sys.argv[1]
if os.path.exists(args):
    pass
else:
    os.mkdir(str(os.getcwd()).join({args}))

check_url()
