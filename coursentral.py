#INFORMATION ABOUT ALL OF THE COURSES#######################################################################################################
courses = [
{
    "name" : "CS50's Introduction to Computer Science",
    'partner' : 'Harvard University',
    'partner type' : 'University',
    'subject' : 'Computer Science',
    'level' : 'Beginner',
    'languag' : 'English',
    'price' : 'Free',
    'certificate' : True,
    'duration' : '12 weeks 6 to 18 hours per week',
    'pacing' : 'Self-paced',
    'availability' : True
},
{
    "name" : 'Application Development - Python',
    'partner' : 'Google',
    'partner type' : 'Organization',
    'subject' : 'Python',
    'level' : 'Intermediate',
    'language' : 'English',
    'price' : 'Free',
    'certificate' : True,
    'duration' : '6 hours worth of material',
    'pacing' : 'Self-paced',
    'availability' : True 
},
{
    "name" : 'Python: aprender a programar',
    'partner' : 'Universitat Politecnica de Valencia',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : 'Spanish',
    'price' : 'Free',
    'certificate' : True,
    'duration' : '8 weeks long, 3-4 hours a week',
    'pacing' : '6th Jun,2023',
    'availability' : True
},
{
    "name" : 'Python for Everybody',
    'partner' : 'University of Michigan',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 150,
    'certificate' : True,
    'duration' : '35 weeks long, 3 hours a week',
    'pacing' : 'Self-Paced',
    'availability' : True
},
{
    "name" : 'Computing in Python I: Fundamentals and Procedural Programming',
    'partner' : 'Georgia Institute of Technology',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '5 weeks long, 9-10 hours a week',
    'pacing' : '1st Jan,2024',
    'availability' : False 
},
{
    "name" : 'Introduction to Computer Science and Programming Using Python',
    'partner' : 'Massachusetts Institute of Technology',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '9 weeks long, 14-16 hours a week',
    'pacing' : '30th Aug,2023',
    'availability' : False
},
{
    "name" : "CS50's Introduction to Artificial Intelligence with Python",
    'partner' : 'Harvard University',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '7 weeks long, 10-30 hours a week',
    'pacing' : '1st Apr,2020',
    'availability' : True
},
{
    "name" : 'Python Data Structures',
    'partner' : 'University of Michigan',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '7 weeks long, 2-4 hours a week',
    'pacing' : '13th Jul,2023',
    'availability' : True
},
{
    "name" : 'Python Data Visualization',
    'partner' : 'Rice University',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '4 weeks long, 8-9 hours worth of material',
    'pacing' : '31st Jul,2023',
    'availability' : True
},
{
    "name" : "Python for Data Science",
    'partner' : 'University of California, San Diego',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : False,
    'duration' : '10 weeks long, 8-10 hours a week',
    'pacing' : 'Self-Paced',
    'availability' : True 
},
{
    "name" : "CS50's Introduction to Programming with Python",
    'partner' : 'Harvard University',
    'partner type' : 'University',
    'subject' : 'Python',
    'level' : 'Beginner',
    'language' : "English",
    'price' : 'Free',
    'certificate' : True,
    'duration' : '10 weeks long, 3-9 hours a week',
    'pacing' : '1st Apr,2022',
    'availability' : True
}
]


#MAIN QUESTION FILTERING FUNCTION ###################################################################################################################
def filtering_function():
        for course in courses:
            if course['subject'] == subject.capitalize() and course["level"] == level.capitalize() and course['language'] == language.capitalize():
                filtered_courses.append(course)


#OPTIONAL QUESTION FILTERING FUNCTIONS########################################################################################################
def filtering_function2():
    for filtered_course in filtered_courses:
        if price == 'yes':
            if filtered_course['price'] != 'Free':
                filtered_courses.remove(filtered_course)
        if cer == 'yes':
            if filtered_course['certificate'] != True:
                filtered_courses.remove(filtered_course)
        if pacing == 'yes':
            if filtered_course['pacing'] != 'Self-Paced':
                filtered_courses.remove(filtered_course)


#CHOSEN COURSE FUNCTIONS####################################################################################################################
def choosing():
        global chosen_course
        chosen_course = input('')

def returner():   
        if any(dictionary.get("name") == chosen_course
               for dictionary in filtered_courses
               ):
                print('''
                          

Here is the information about your course!
                              ''')
                for key, value in filtered_course.items():
                    print(key, ':', value)
                signin() 
        else:
            print('''
Sorry the name you entered is not valid!
                  
kindly re-enter the name of the course of your choice.
 ''')    
            choosing() 
            returner() 


#LOGIN FUNCTIONS###########################################################################################################################
def email_entry():
    global email
    email = input('Email: ')

def password_entry():
    global password
    password = input('Password: ')

def email_validation():
    if substring and substring2 in email and len(email) >= 13:
            print('valid email')
    else:
        print('Invalid email, kindly re-type it')
        email_entry()
        email_validation()

def password_validation():
    if len(password) >= 8:
        print('valid password')
    else:
        print('Invalid password, kindly re-type it')
        password_entry()
        password_validation()

def signin():
    global signup
    signup = input('Would you like to sign up for the course? ')
    if signup.capitalize() == 'Yes':
        email_entry()
        global substring
        global substring2
        substring = '@'
        substring2 = '.com'
        email_validation()
        password_entry()
        password_validation()
        print('''
                         
YOU ARE ENROLLED! HAPPY LEARNING.
                          ''')
    else:
        print('No worries!')


#QUESTIONS#########################################################################################################################
print('''
      
WELCOME TO COURSENTRAL!
      
You will be asked a few mandatory questions so we can find the perfect courses for you.
      

''')
ready = input('Ready to start? ')

if ready.capitalize() == 'No':
    print('''
          
Visit us when your ready, Enjoy the rest of your day!
          
          ''')
else:
    subject = input('''(Python-Computer Science-Swift-Java-C++)
What subject/skill are you looking for? ''')
    level = input('''(Beginner-Intermediate-Advanced)
What is your skill level? ''')
    language = input('''(English-Arabic-Spanish-Chinese)
Choose your language: ''')
    print('''
          
Now here are a few optional questions.
    
If you have a prefrance to the question asked kindly type yes.
          
    ''')

    price = input('Free? ')
    cer = input('With certificate? ')
    pacing = input('Self-Paced? ')

    filtered_courses = []
    filtering_function()
    filtering_function2()

    for filtered_course in filtered_courses:
        print("_________________________________________________________________________")
        for key, value in filtered_course.items():
            print(key, ':', value)
    print('''       
Here are the courses we have filtered out for you!


    
Kindly copy-paste the name of the course you would like to enroll into!
          ''')

    choosing()
    returner()
