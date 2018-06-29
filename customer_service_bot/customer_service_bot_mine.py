
# coding: utf-8

# In[3]:


def cs_service_bot():
   # Replace `pass` with your code
   print ("\n Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?"+'\n'+"[1] New Customer"+'\n'+"[2] Existing Customer")
   response = int(input ("Please enter the number corresponding to your choice: "))
   if response == 1:
       new_customer()
   elif response == 2:
       existing_customer()
   else:
       print ("Sorry, we didn't understand your selection.")
       cs_service_bot()


# In[5]:


def existing_customer():
    print ("\n[1] Television Support \n[2] Internet Support \n[3] Speak to a support representative. ")
    response = int (input("\nWhat kind of support do you need?: "))
    if response == 1:
        television_support()
    elif response == 2:
        internet_support()
    elif response == 3:
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        existing_customer()


# In[ ]:


def new_customer():
    print ("\n[1] Sign up for service. \n[2] Schedule a home visit. \n[3] Speak to a sales representative. ")
    response = int (input("We're excited to have you join the DNS family, how can we help you?: "))
    if response == 1:
        sign_up()
    elif response == 2:
        home_visit()
    elif response == 3:
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
        new_customer()


# In[ ]:


def television_support():
    print ("\n[1] I can't access certain channels.\n[2] My picture is blurry.\n[3] I keep losing service.\n[4] Other issues.")
    response = int (input("What is the nature of your problem?: "))
    if response == 1:
        print ("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif response == 2:
        print ("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == 3:
        print ("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif response == 4:
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


# In[ ]:


def internet_support():
    print ("[1] I can't connect to the internet.\n[2] My connection is very slow.\n[3] I can't access certain sites.\n[4] Other issues.")
    response = int (input("What is the nature of your problem?: "))
    if response == 1:
        print ("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == 2:
        print ("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    elif response == 3:
        print ("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == 4:
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


# In[ ]:


def did_that_help():
    response = str (input("Was the problem solved? (Yes or No): ")).upper()
    if response == "YES":
        print ("Thanks for contacting us!")
    elif response == "NO":
        print ("[1] Talk to a live representative\n[2] Schedule a home visit")
        choice = int(input("Please choose your further support option: "))
        if choice == 1:
            live_rep("support")
        elif choice == 2:
            home_visit ("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()
    else:
        print("Sorry, we didn't understand your selection.")
        did_that_help()


# In[ ]:


def sign_up():
    print ("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.")
    print ("[1] Bundle Deal (Internet + Cable)\n[2] Internet\n[3] Cable")
    response = int(input (": "))
    if response == 1:
        print ("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif response == 2:
        print ("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif response == 3:
        print ("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()


# In[ ]:


def home_visit(purpose="none"):
    if purpose == "none":
        print ("[1] New service installation.\n[2] Exisitng service repair.\n[3] Location scouting for unserviced region.")
        response = int(input ("Please choose which service is required: "))
        if response == 1:
            home_visit("new install")
        elif response == 2:
            home_visit("support")
        elif response == 3:
            home_visit ("scout")
        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    else:
        visit_date = str(input("lease enter a date(mm/dd format) below when you are available for a technician to come to your home and {}".format(purpose)))
        print ("Wonderful! A technical will come visit you on {}. Please be available between the hours of 1:00 am and 11:00 pm.".format(visit_date))
        return visit_date


# In[ ]:


def live_rep(help_type):
    if help_type == "sales":
        print ("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    elif help_type == "support":
        print ("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")


# In[ ]:


cs_service_bot()
