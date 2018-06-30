
#initialize an empty list to store gamer dict
gamers = []
form_email = ('Dear {name},\nWelcome to the {game} night! This week\'s game night is {day_of_week}!\n Please RSVP your seats soon!')

# Add a gamer(dict ojt) into the list of gamers
def add_gamer(gamer, gamers_list):
    if 'name' in gamer and 'availability' in gamer:
        gamers_list.append(gamer)
        print (gamers_list)
    return gamers_list

#build an empty table(dict obj) of every night and attendee qty
def build_daily_frequency_table():
    days = {
        'Monday':0,
        'Tuesday':0,
        'Wednesday':0,
        'Thursday':0,
        'Friday':0,
        'Saturday':0,
        'Sunday':0
    }
    return days

#Update how many attendees are available for each night, return updated table (dict obj)
def calculate_availability(gamers, available_frequency):
    for gamer in gamers:
        for day in gamer['availability']:
            available_frequency[day] += 1
    return available_frequency

# find the night of max qty of attendees and return the night (str)
def find_best_night(availability_table):
    best_night = max (list (availability_table.values()))
    for night in availability_table:
        if availability_table[night] == best_night:
            return night

#find the attendees available for the game night, returns a list of attendee's names
def available_on_night(gamers_list, day):
    attendee=[]
    for gamer in gamers_list:
        if day in gamer['availability']:
            attendee.append(gamer['name'])
    return attendee

#create email context for each gamer
def send_email(gamers_who_can_attend, day, game):
    for name in gamers_who_can_attend:
        print(form_email.format(name = name, day_of_week = day, game = game))

#a test to add several test gamers into the called gamer list
def TEST_CASE_Add_in_test_gamers(gamers_list):
    add_gamer({'name':'Kimberly Warner',
    'availability':['Monday', 'Tuesday', 'Friday']}, gamers_list)
    add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers_list)
    add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers_list)
    add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers_list)
    add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers_list)
    add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers_list)
    add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers_list)
    add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers_list)
    add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers_list)
    add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers_list)
    return gamers_list

#a test case function to find the best game night by called gaer list, test on build_daily_frequency_table(), calculate_availability(gamers, available_frequency), find_best_night(availability_table) functions, available_on_night(gamers_list, day)
def TEST_CASE_Find_the_best_game_night(gamers_list):
    count_availability = build_daily_frequency_table
    count_availability = calculate_availability(gamers_list, count_availability)
    game_night = find_best_night(count_availability)
    attending_game_night = available_on_night(gamers_list, game_night)

    print('The best game


    night is {}!\n'.format(game_night))
    print('The possible attendees are {}\n'.format(attending_game_night))

#a test case on for_email statement and send_email function
def TEST_CASE_send_emails_to_gamers(attending_game_night, game_night, game = 'Abruptly Goblins!'):
    send_email(attending_game_night, game_night, game)
