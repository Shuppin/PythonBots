# Credit to @TheUsaf and his team for the Kahoot! answer bot and KahootPY library

# WELCOME TO MY CULMINATION OF PYTHON BOTS WRAPPED INTO ONE PROGRAM
# Have fun! (Please don't heavily misuse this program)

__version__ = "1.1.5"

# Default Imports

import random # Obvious use cases
import time as t # Used to slow down the program a little for reading messages etc.. 
import os # Used to reload program
from importlib import reload, import_module

# 3rd Party Imports

try: # Try & Catch for 'KahootPY' import, the term 'catch' has the same meaning as 'except'
    import kahoot  # pip install KahootPY
except ImportError:
    print(" Please make sure KahootPY is installed before running this program")
    print(" This library can be found at https://pypi.org/project/KahootPY/")
    raise ImportError
    #exit() # Make sure the program isn't run without KahootPY installed, which would horribly break the program

try: # Try & Catch for 'selenium' import
    import selenium  # pip install selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
except ImportError: 
    print(" Please make sure you have Selenium installed before running this program")
    print(" Help can be found at https://selenium-python.readthedocs.io/installation.html")
    raise ImportError
    #exit() # Make sure the program isn't run without selenium installed, which would horribly break the program

try:
    import colorama # pip install colorama
    from colorama import Fore as c, Back, Style
except ImportError:
    print(" Please make sure you have Colorama installed before running this program")
    print(" This library can be found at https://pypi.org/project/KahootPY/")
    raise ImportError
    #exit()

# Read devkey from file 'password.txt'

key = open(os.path.join(os.path.dirname(__file__), "password.txt") , 'r')
devkey = key.read()

# Colorama initialisation

colorama.init(autoreset=True)

def test():
    print("test")

def Console(console=None): # A cool little console which adds certain features for monitoring the program during runtime

    consoleSyntaxOne = c.BLUE + " bots@main"
    consoleSyntaxTwo = c.WHITE + ":"
    consoleSyntaxThree = c.CYAN + "~"
    consoleSyntaxFour = c.WHITE + "$ "
    consoleSyntaxInput = consoleSyntaxOne + consoleSyntaxTwo + consoleSyntaxThree + consoleSyntaxFour

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(c.RED + """                      
                       ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''
    """)

    print("")

    print(c.BLUE + " [---]" + c.CYAN + "               The Bot Library              " + c.BLUE + "[---]")
    print(c.BLUE + " [---]" + c.CYAN + "             Created By: " + c.RED + "Shuppin            " + c.BLUE + "[---]")

    print(c.CYAN + "                     Version: " + c.RED + __version__)
    print(c.CYAN + "                   Codename: '" + c.YELLOW + "Mercury" + c.CYAN + "'")

    print(c.BLUE + " [---]    " + c.YELLOW + "https://github.com/Shuppin/PythonBots" + c.BLUE + "   [---]")
    print(c.BLUE + " [---]" + c.CYAN + "       Credit to @TheUsaf for KahootPY      " + c.BLUE + "[---]")

    print("")

    print(c.MAGENTA + "               Welcome to The Bot Library")
    print(c.MAGENTA + "   Your All-In-One Library for all your botting needs")

    print("")
    print("")

    print(" Type 'help' to get started")

    while True: # Loop for whole function

        if console == None: # Ask for the user to input a command if one was not given when the funciton was called

            while True: # Try & Catch for 'console' input
                print("")
                try:
                    print(consoleSyntaxInput, end = '')
                    console = input()
                    if console == "" or console == None:
                        print(c.RED + " Please enter a command!")
                    else:
                        break
                except ValueError:
                    print(c.RED + f" The command '{console}' is not a recognised command")

            passedCommand = False # Just to ensure 'passedCommand' gets defined

        else:
            passedCommand = True # Boolean which tells the function if the command passed was from inside the function or if it was passed when the funciton was called

        if console is not None:
            tempConsole = console.replace(")", " ) ")
            tempConsole = tempConsole.replace("(", " ( ")
            command = tempConsole.split() # Splits the command passed up into words in an array, this is for handling multiple arguments
            arguments = tempConsole.split(",") # Splits the command based on commas

        if command[0].lower() == "help": # Checking if the command passed starts with [.startswith()] 'help' in lower case [.lower()]
            if len(command) == 1: # Checking if the command passed if only 1 word long, e.g. just 'help' instead of 'help exit'
                print("") 
                print(" | Command | Usage              | Example             |")
                print(" |---------|--------------------|---------------------|")
                print(" | help    | help <command>     | help status         |")
                print(" | status  | status <process>   | status KahootBot()  | (Not Implemented)")
                print(" | exit    | exit               | exit                |")
                print(" | escape  | escape             | escape              |")
                print(" | execute | execute <function> | execute KahootBot() |")
                print(" |---------|--------------------|---------------------|")

            elif len(command) > 1: # Checking if the command passed has 1 or more arguments

                if command[1].lower() == "status": # Checking if the command has the argument 'status', same for all of the below
                    print(" Displays status of specified function/process")

                elif command[1].lower() == "help":
                    if len(command) >= 3:
                   
                        print(" add me") # IMPLEMT THIS
                    print(" Displays the help page")

                elif command[1].lower() == "exit" or command[1].lower() == "escape" or command[1].lower() == "stop": # 'or' statement just checks two arguments in one as they are the same
                    print(" Exits the console and returns to main program")

                elif command[1].lower() == "execute":
                    if len(command) >= 3:
                        if command[2].lower() == "kahootbot() ":
                            print(" Usage: execute kahootbot(<pin>, <username>, <quizname>)")
                        else:
                            print(" Runs a specified function")
                            print(" Usage: execute <process> OR execute [pid:<process id>]")
                            while True:
                                try:
                                    print(" Would you like to see the currently available proceses? (Y/N)")
                                    #print(consoleSyntaxInput, end = '')
                                    tempIn = input(" >> ")
                                    break
                                except ValueError:
                                    print(c.RED + " Not a valid response!")
                    else:
                        print("")
                        print(" Runs a specified function")
                        print(" Usage: execute <process> OR execute [pid:<process id>]")
                        print(" Example: execute pid:1")
                        print("")

                        while True:
                            try:
                                print(" Would you like to see the currently available proceses? (Y/N)")
                                #print(consoleSyntaxInput, end = '')
                                tempIn = input(" >> ")
                                break
                            except ValueError:
                                print(" Not a valid response!")
                                         
                    if tempIn.lower().startswith("y"):
                        print("")
                        print(" | Process     | PID |")
                        print(" |-------------|-----|")
                        print(" | KahootBot() |  1  |")
                        print(" |-------------|-----|")
                    
                else:
                    print(" That command does not exist")

        elif command[0].lower() == "exit" or command[0].lower() == "escape" or command[0].lower() == "stop": # Stops this function's loop, which is what this command does
            break

        elif command[0].lower() == "execute": # Checking if the command passed was 'execute', using the same method as before
            
            if len(command) == 1: # Checks if an argument was actually passed
                print(" Please specify a program to execute")
            
            elif len(command) > 1:

                if len(command) >= 3:
                    if command[1].lower().startswith("kahootbot") and command[2] == "(" and command[len(command) - 1] == ")":

                        if command[3] != ")": # If command has args
                            arguments = [''.join(command[3:(len(command) - 1)])]
                            tempstr = arguments[0]
                            tempstr = tempstr.replace('"', '')
                            tempstr = tempstr.replace("'", "")
                            arguments = tempstr.split(",")

                            if len(arguments) == 1:
                                consoleExec = KahootBot(int(arguments[0]))
                                consoleExec()
                            elif len(arguments) == 2:
                                consoleExec = KahootBot(int(arguments[0]), arguments[1])
                                consoleExec()
                            elif len(arguments) == 3:
                                consoleExec = KahootBot(int(arguments[0]), arguments[1], arguments[2])
                                consoleExec()
                            else:
                                print(c.RED + " Too many arguments passed!")
                        else:
                            consoleExec = KahootBot()
                            consoleExec()

                if command[1].lower().startswith("pid:"): # Checks if the user entered 'execute pid:<process id>'

                    if command[1] == "pid:1":
                        consoleExec = KahootBot()
                        consoleExec()
                        
                    else:
                        print(" That function does not exist!")

                else:
                    print(c.RED + " That function does not exist!")
                  
        elif command[0].lower() == "status":
            print(c.YELLOW + " Not implemented")

        else: # If the command passed doesn't fit any of the identifiers above, run this
            print(c.RED + f" The command '{console}' is not a recognised command")


        if passedCommand == True: # Stops this function's loop if command was passed when the function was called, the purpose of this is so you can execute just a single a console command by just calling the function
            break

        elif passedCommand == False: # What happens if above is not true
            console = None # Sets 'console' back to 'None' so the function will run 'if console == none:'


class KahootBot: # KahootBot class in all its glory

    # Assigning Global Varibles
    driver = None
    autoName = None

    def __init__(self, pin=None, user=None, quiz_name=None): # __init__ gets called as soon as the class get execute/assigned, string 'pin' is the kahoot game pin which you desire to connect to, strinf 'user' is the user name you would like to have for your bot, string 'quiz_name' is the name of the quiz you are playing, used for the answer bot.

        # Declaring inputed varibles and making sure they are at least set to 'None'
                
        self.pin = pin if pin is not None else None
        self.user = user if user is not None else None
        self.quiz_name = quiz_name if quiz_name is not None else None

        print("")
        print(" _____________________________________________") # Seperator to show your on the next section
        print("")
        
        print(" Initiating KahootBot()")
        t.sleep(random.uniform(0.5, 0.8))
        print(f" KahootBot() initiated with the arguments: {self.pin}, \"{self.user}\", \"{self.quiz_name}\"")

    def __call__(self):

        self.exec() # Starts the rest of the class

        #driver.close()

        print("")

        print(c.GREEN + " Achievment Unlocked!")
        print(c.GREEN + " Ultimate Finale - Finish executing KahootBot()")

        print("")

    def exec(self): # This function loads all of the items nessecary for the class, assigns essential variables and asks what you want to actually do in the class

        # Saying 'autoName' and 'driver' are global as we want to change them in this function
        
        global autoName
        global driver

        # Section A - Loading webdrivers

        print("")
        print(" Loading Selenium Web Drivers...")
        print(" Please be patient (Chrome will minimise itself)")
        t.sleep(0.5) # Give the user time to read the message above

        print(" ", end = '')
        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe') # Load the chrome webdriver, used for interacting with Google Chrome, the double backslash represents one '\', but in python backslash is an escape character so you need two of them to cancel one out
        driver.minimize_window() # Minimises the chrome window once it has loaded 

        t.sleep(1) # Give selenium time to minimise the chrome window as it can take upto a second a slow device.
        print("")
        print(" Load complete! ") # Tell the user the load is complete
        print("")
        t.sleep(0.3)
        print("")
        print("")
        print(" _____________________________________________") # Seperator to show your on the next section
        print("")

        t.sleep(0.5)

        driver.minimize_window() # Minimise the window again in case the user thinks it should have been open.ArithmeticError

        # Section B - Disclaimer

        print("")
        print(c.RED + " DISCLAIMER:")
        print(c.RED + " Kahoot! and the K! logo are trademarks of Kahoot! AS")
        print(c.RED + " More info can be found at https://kahoot-win.herokuapp.com/privacy")
        print("")

        t.sleep(3)

        # Section C -Variable Assignment

        print(" Initialising bot...")

        print("")
       
        # Welcome message 

        print(" ------------------------------------")
        print(" Welcome to Kahoot API meets python ;)")
        print(" Caution, this can get you banned from kahoot")
        print(" Proceed at your own risk")
        print(" ------------------------------------")

        print("")

        t.sleep(2.5) # Give time to let the user catch up

        if self.pin==None: # Checks if 'self.pin' was assigned when the variable was passed when KahootBot() was called
            while True: # Loop for this whole section

                while True: # Try & Catch for game pin input
                    try:
                        print(" Please enter your game pin: ")
                        pinIn = int(input(" > "))
                        break
                    except ValueError:
                        print(c.RED + " That is not a valid pin!")
                        print("")

                while True: # Try & Catch for correct pin check
                    try:
                        print(" Are you sure this is the right pin (Y/N)? ")
                        pinCorrect = input(" > ")
                        break
                    except ValueError:
                        print(c.RED + " Not a valid response!")
                        print("")

                print(" (This API is not designed for python, so i cannot test if your pin is correct or not)") # Small Notice
                t.sleep(1) # Give time to allow the user to read message
                print("")

                if pinCorrect.lower().startswith("y"): # If the user responds with anything begining with 'y', e.g. 'yes' to allow for minor mistakes
                    self.pin = pinIn # Assign the variable
                    break # Stops the loop from running again
                elif pinCorrect.lower().startswith("n"): # If the user responds with anything begining with 'n', e.g. 'no'
                    print(c.RED + " Trying again...")
                    print("") 
                    # Notice the lack of 'break' which makes the loop go round again to allow the user to input their new desired pin
                else: # Make sure any input is accounted for
                    print(c.RED + " Not a valid response!")
                    print(c.RED + " Trying again...")
                    print("")

        if self.user == None or self.user == "": # Checks if 'self.user' was assigned when the variable was passed when KahootBot() was called

            while True: # Try & Catch for Bot name type choice
                try:
                    print(" ------------------------------------")
                    print(" | Set bot name to:                 |")
                    print(" | 1) Kahoot Auto-generated         |")
                    print(" | 2) Custom                        |")
                    print(" ------------------------------------")
                    nameMultiChoice = input(" > ")

                    if nameMultiChoice == "1": # Checks if the inputted choice from above was 1
                        self.user = "gay" # This name is typically blocked, so kahoot will replace it with an autogenerated one
                        autoName = True # This is later used when displaying the name of the bot, as we don't actually know what name kahoot chose, it replaces the name with '<auto>'
                        break

                    elif nameMultiChoice  == "2": # Checks if the inputted choice from above was 2
                        while True: # Try & Catch for bot name input
                            try:
                                print(" Enter the name of your bot")
                                self.user = input(" > ")
                                break
                            except ValueError:
                                print(c.RED + " Not a valid response!")
                                print("")
                        autoName = False # Ensures 'autoName' gets assigned
                        break

                    else:
                        print(c.RED + "Please choose a valid option!")
                        print("")

                except ValueError:
                    print(c.RED + " Not a valid response!")
                    print("")
            
        else:
            autoName = False # Ensures 'autoName' gets assigned

        print(" Initialisation complete!") # Lets the user know the program is done initialising
        print("")

        while True: # Loop for action choice

            # Menu to show which actions are available

            print(" ------------------------------------")
            print(" | What would you like to do?       |")
            print(" | 1) Flood bots                    |")
            print(" | 2) Answer bot                    |")
            print(" | 3) Custom - not implemented      |")
            print(" ------------------------------------")

            while True: # Try & Catch for action choice input
                try:
                    execChoice = input(" > ")
                    break
                except ValueError:
                    print(c.RED + " Not a valid response!")
                    print("")

            if execChoice == "1": # You know waht this does by now
                self.flood() # Executes the function flood()
                break # Stops the loop (in other words, breaks out of the loop)
            elif execChoice == "2":
                self.fullBot() # Executes the function fullBot()
                break # Stops the loop (in other words, breaks out of the loop)
            elif execChoice == "3":
                print(c.YELLOW + " Not implemented") # Reiterates to the user that this feature is not implmented
            else:
                print(c.RED + " Not a valid response!")

    def flood(self): # This function uses the KahootPY Library to simulate a client trying to connect to kahoot, and then this function itterates that

        # Welcome message

        print("")
        print(" Flood bot loaded!")
        print("")
        print("")
        print(c.BLUE + " ||_________________________________||")
        print(c.BLUE + " ||_________________________________||")
        print(c.BLUE + " ||        " + c.CYAN + "Kahoot Bot Flooder" + c.BLUE + "       ||")
        print(c.BLUE + " ||              " + c.CYAN + "v1.5" + c.BLUE + "               ||")
        print(c.BLUE + " ||_________________________________||")
        print(c.BLUE + " ||_________________________________||")
        print(c.BLUE + " ||                                 ||")
        print("")

        t.sleep(2) # Allow time for the user to take in this outstanding jaw dropping exquisite masterpiece of ascii art

        while True: # Try & Catch for 'botsAmount' input, warning: lots of nested try's here, so be careful if modifying
            try:
                print(" How many bots would you like to flood?")
                botsAmount = int(input(" > "))
                if botsAmount < 101: # Makes sure the amount is a reasonable amount (less than 100)
                    break
                elif botsAmount > 100:
                    print(c.YELLOW + " That value is too high! Defaulting to 100")

                    # Override system for devlopment purposes

                    while True: # Loop for override 
                        while True: # Try & Catch for override input
                            try:
                                print(" Do you wish to override? (Y/N)")
                                override = input(" > ")
                                break
                            except ValueError:
                                print(c.RED + " Not a valid response!")

                        if override.lower().startswith("y"):
                            while True: # Try & Catch for devkeyInput
                                try:
                                    devkeyInput = input("Please enter dev key: ")
                                    break
                                except ValueError:
                                    print(c.RED + " Override Failed")
                                    botsAmount = 100 # Sets the bots amount back down to the max amoubtn of 100
                                    break
                            if devkeyInput == devkey:
                                print(c.GREEN + " Override Successful") # Leaves 'botsAmount' as it is
                            else:
                                print(c.RED + " Override Failed")
                                botsAmount = 100 # Sets the bots amount back down to the max amoubtn of 100
                            break

                        elif override.lower().startswith("n"):
                            print(" Proceeding as normal..")
                            break

                        else:
                            print(c.RED + " Not a valid response!")
                            print("")

                    print("")
                        
                    break

            except ValueError:
                print(c.RED + " Not a valid response!")
                print("")

        while True: # Try & Catch for 'delayChoice' input
            try:
                print(" -- Delay interval for bot (Seconds) --")
                print("    1) Random Interval (Small)")
                print("    2) Random Interval (Large)")
                print("    3) Set Interval")
                delayChoice = float(input(" > "))
                break
            except ValueError:
                print(c.RED + " Not a valid response!")
                print("")

        print("")

        if delayChoice == 3: # Set interval section for option 3
            while True: # Try & Catch for delay input
                try:
                    print(" What would you like you interval to be? (Seconds)")
                    delay = int(input(" > "))
                    break
                except ValueError:
                    print(c.RED + " Not a valid response!")
                    print("")

        print("")
        print(" Inititating Flood...")  # Let the user know the flood is starting
        print("")

        # Flood section

        terms = [] # Declaring the array 'terms'
        for i in range(botsAmount): # Repeat for the amount of times set in the input above
            
            if delayChoice == 1: # Random intervals of time (Small)
                delay = random.uniform(0.4,1.3) # random.uniform() is the same as random.randint() but for floats
            elif delayChoice == 2: # Random intervals of time (Large)
                delay = random.randint(3,10)
            
            t.sleep(delay) # Wait the amount of time the float/int 'delay' is set to
            
            terms.append(f"client{i}") # Appends(adds to the end) the string 'client' followed by the Nth(i) itteration, the f at the start is 'format' which allows the use of {} inside the quotation mark
            terms[i] = kahoot.client() # Set the Nth item in the list 'terms' to kahoot.client(), the thing which connects to kahoot
            
            terms[i].join(self.pin, str(self.user) + " " + str(i + 1)) # This is the line which actually connects to the kahoot service, syntax is <client>.join(<pin>, <username>). The extra [+ ' ' + str(i + 1)] on the end adds the number of the bot onto the end of the username
            
            if autoName == False: # Checks if the name set earlier was an automatic name set by kahoot or set by the user
                print(f" Bot ({self.user} {i + 1}) Planted")
            else:
                print(f" Bot (<auto> {i + 1}) Planted")
            

        print("")
        print(" Flood complete!") # Tells the user the flood is complete

    def fullBot(self):

        driver.minimize_window() # Minimises Google Chrome if it is open

        print("")
        print(" Answer Bot Loaded!")
        print("")
        print("")

        # Welcome Message

        print(" ||_________________________________||")
        print(" ||_________________________________||")
        print(" ||        Kahoot Answer Bot        ||")
        print(" ||             v2.4.1              ||")
        print(" ||        Hooks By @TheUsaf        ||")
        print(" ||_________________________________||")
        print(" ||_________________________________||")
        print(" ||                                 ||")

        t.sleep(0.5) # More ascii art uwu

        while True: # Try & Catch for Anwser bot type
            try:
                print("")

                print(" -----------------------------------------")
                print(" | Would you like:                       |")
                print(" | 1) One Answer Bot                     |")
                print(" | 2) Multiple Answer Bots               |")
                print(" | 3) 5 Answer Bots (Leaderboard filler) |")
                print(" -----------------------------------------")

                fullBotChoice = int(input(" > "))

                break
            
            except ValueError:
                print(c.RED + " Not a valid response!")
                print("")
        
        if self.quiz_name == None: # Checks if 'self.quiz_name' was set when the class was called

            while True: # Try & Catch for quiz name input
                try:
                    
                    print(" Please enter the quiz name")
                    print(" (Enter 'none' if you don't have the name)")
                    quizNameInput = input(" > ")

                    #rawQuizNameInput = r"{}".format(quizNameInput)  |  This line of code assigns 'rawQuizNameInput' to the same as 'quizNameInput', but it is a raw string, which basically means it will ignore all special characters such '\','{}' and '#' to name a few 
                    
                    if quizNameInput == "none": # Allows the user to set the name value to nothing 
                        print(c.RED + " The bot will not work wihtout a quiz name")
                        print(c.RED + " There are other options which can be found in the settings tab on the website")

                        self.quiz_name = None # Actually sets the name value to none
                    
                    else:

                        self.quiz_name = quizNameInput # Sets the name to whatever the user inputted

                    break

                except ValueError:
                    print(c.RED + " Not a valid response!")

        if fullBotChoice == 1: # Checks if the user chose option one (One Answer Bot)

            print(" Connecting...")

            driver.minimize_window() # Closes the window first, so this page loads without the user knowing
            driver.get('https://kahoot-win.herokuapp.com/') # Gets the whole website which is used for the basis of this program 

            print("")

            # This whole section gives time for the webpage to load, there is a correct way to do this,which is not implemented yet

            print(" Connection established")
            t.sleep(0.5)
            print(" Loading webpage")
            t.sleep(0.5)

            print("")

            print(" Loading.")
            t.sleep(1.5)
            print(" Loading..")
            t.sleep(1.5)
            print(" Loading...")
            t.sleep(4)

            print("")

            driver.maximize_window() # Once the first webpage is loaded, it waits for it to load, then it opens a new window with the same link, the second webpage won't show any popups as the page has previously been loaded
            driver.get('https://kahoot-win.herokuapp.com/') # Opens a new webpage popup free
            
            while True: # Try & Catch for element location
                try:
                    login = driver.find_element_by_id("loginInput") # Find an element in the raw HTML with the id 'loginInput'
                    submit = driver.find_element_by_id("loginButton") # Same but with 'loginButton'
                    
                    login.send_keys(self.pin) # Types the game pin into the login input box on the website
                    

                    break

                except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                    t.sleep(2) # This sleep gives time for the element to load before trying to execut ecode on it

            while True: # Try & Catch for submit button
                try:
                    submit.click() # Clue is in the name, it clicks the button

                    break

                except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.  

                    while True:
                        # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                        try:
                            okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                            okButton.click() # Proceeds to click the button
                            t.sleep(0.3)

                            break
                        except selenium.common.exceptions.NoSuchElementException:
                            t.sleep(2)

            print(" Waiting for page to load, please allow upto 5 seconds")
            t.sleep(5)

            # This section makes sure the element xpath~"/html/body/div[4]/div[3]/div/button[1]" exists, if it does exist then that mean the next page has loaded

            while True:
                try:            
                    tempElement = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/button[1]")
                    break
                except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                    t.sleep(1)

            while True: # Try & Catch for element location
                try:

                    # Exact same as before, but with slightly different names

                    name = driver.find_element_by_id("loginInput") 
                    nameSubmit = driver.find_element_by_id("loginButton")
                    
                    name.send_keys(self.user)
                    

                    break

                except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                    t.sleep(2)
                    
            while True: # Try & Catch for submit button
                try:
                    nameSubmit.click() # Clue is in the name, it clicks the button

                    break

                except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.

                    while True:
                        # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                        try:
                            okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                            okButton.click() # Proceeds to click the button
                            t.sleep(0.3)

                            break
                        except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                            t.sleep(2)

            print("")

            print(" Waiting for page to load, please allow upto 5 seconds")
            t.sleep(5)

            if self.quiz_name is not None:

                while True: # Try & Catch for element location
                    try:
                        quizName = driver.find_element_by_id("nameInput") # Find the element with the id 'nameInput' and assigns it to the variable 'quizName'

                        quizName.send_keys(self.quiz_name) # Types the quiz_name into the box, unless it is equal to None
                        
                        break

                    except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                        t.sleep(2)

                    except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.

                        while True:
                            # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                            try:
                                okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                                okButton.click() # Proceeds to click the button
                                t.sleep(0.3)

                                break
                            except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                                t.sleep(2)
            else:
                print(f" self.quiz_name has been identified as none, {self.quiz_name}")

        elif fullBotChoice == 2: # Checks if the user chose option two (Multi Answer Bot)

            while True: # Try & Catch for amount of bots input
                try:
                    print("")

                    print(" How many bots would you like to have?")
                    multiAnswerBotAmount = int(input(" > "))

                    if 100 > multiAnswerBotAmount > 25: # Checks that the inputted value is a reasonable amount
                        while True: # Nested Try & Catch for max tabs warning input
                            try:
                                print("")
                                print(c.YELLOW + " WARNING")
                                print(c.YELLOW + " Opening more than 25 tabs might **severely** effect system perfomance")
                                print(c.YELLOW + " Do you wish to proceed? (Y/N)")
                                multiAnswerBotWarning1 = input(" > ")

                                break

                            except ValueError:
                                print(c.RED + " Not a valid response!")
                                print("")
                        
                        print("")

                        if multiAnswerBotWarning1.lower().startswith("y"): # Checks if the user responded with anything begining with 'y'
                            print(" Okay, good luck...")
                            print("")
                            t.sleep(1)
                            print(" 3")
                            t.sleep(1)
                            print(" 2")
                            t.sleep(1)
                            print(" 1")
                            t.sleep(1)
                            print(" Commencing...")
                            print(f" Opening {multiAnswerBotAmount} tab(s)")
                            print("")
                            break
                        elif multiAnswerBotWarning1.lower().startswith("n"):
                            print(" Wise choice..")
                    
                    elif multiAnswerBotAmount > 99:
                        print("")
                        print(" You are officially a mad man/woman for even trying to open that many tabs")
                        print(" For your own computer's sake, i wont let you do that")
                        print("")

                    elif 26 > multiAnswerBotAmount > 0:
                        print(f" Opening {multiAnswerBotAmount} tab(s)")
                        break

                    elif multiAnswerBotAmount < 1:
                        print(c.RED + " Please make sure your answer is above 0")

                except ValueError:
                    print(" Not a valid response!")
                    print("")

            driver.get('https://kahoot-win.herokuapp.com/')

            t.sleep(3)        
            
            for i in range(multiAnswerBotAmount):

                print(f" Opening tab {i+1}")

                driver.maximize_window()

                driver.execute_script('''window.open("https://kahoot-win.herokuapp.com/","_blank");''')


                # Here (1)

                while True: # Try & Catch for element location
                    try:
                        login = driver.find_element_by_id("loginInput") # Find an element in the raw HTML with the id 'loginInput'
                        submit = driver.find_element_by_id("loginButton") # Same but with 'loginButton'
                        
                        login.send_keys(self.pin) # Types the game pin into the login input box on the website
                        

                        break

                    except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                        t.sleep(2) # This sleep gives time for the element to load before trying to execut ecode on it

                while True: # Try & Catch for submit button
                    try:
                        submit.click() # Clue is in the name, it clicks the button

                        break

                    except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.  

                        while True:
                            # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                            try:
                                okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                                okButton.click() # Proceeds to click the button
                                t.sleep(0.3)

                                break
                            except selenium.common.exceptions.NoSuchElementException:
                                t.sleep(2)

                print(" Waiting for page to load, please allow upto 5 seconds")
                t.sleep(5)

                # This section makes sure the element xpath~"/html/body/div[4]/div[3]/div/button[1]" exists, if it does exist then that mean the next page has loaded

                while True:
                    try:            
                        tempElement = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/button[1]")
                        break
                    except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                        t.sleep(1)

                while True: # Try & Catch for element location
                    try:

                        # Exact same as before, but with slightly different names

                        name = driver.find_element_by_id("loginInput") 
                        nameSubmit = driver.find_element_by_id("loginButton")
                        
                        name.send_keys(self.user)
                        

                        break

                    except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                        t.sleep(2)
                        
                while True: # Try & Catch for submit button
                    try:
                        nameSubmit.click() # Clue is in the name, it clicks the button

                        break

                    except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.

                        while True:
                            # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                            try:
                                okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                                okButton.click() # Proceeds to click the button
                                t.sleep(0.3)

                                break
                            except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                                t.sleep(2)

                print("")

                print(" Waiting for page to load, please allow upto 5 seconds")
                t.sleep(5)

                if self.quiz_name is not None:

                    while True: # Try & Catch for element location
                        try:
                            quizName = driver.find_element_by_id("nameInput") # Find the element with the id 'nameInput' and assigns it to the variable 'quizName'

                            quizName.send_keys(self.quiz_name) # Types the quiz_name into the box, unless it is equal to None
                            
                            break

                        except selenium.common.exceptions.StaleElementReferenceException: # This error occurs when the element cannot be found or it is not in a valid state e.g. it is not fully loaded yet
                            t.sleep(2)

                        except selenium.common.exceptions.ElementClickInterceptedException: # This error occurs when there is a popup over the button, or the button is hidden.

                            while True:
                                # This bit of code locates and clicks the 'ok' button on the popup responsible for creating this error
                                try:
                                    okButton = driver.find_element_by_xpath("/html/body/div[6]/button") # The direct path to the element we are looking for, as the element cannot be identified by a single id
                                    okButton.click() # Proceeds to click the button
                                    t.sleep(0.3)

                                    break
                                except selenium.common.exceptions.NoSuchElementException: # This error occurs when the element specified does not exists in the webpage
                                    t.sleep(2)
                else:
                    print(c.YELLOW + f" self.quiz_name has been identified as none, {self.quiz_name}")

if __name__ == "__main__":
    Console("help")

