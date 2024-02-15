# Ask the user for a data sentence (fourth of july 2023), convert the sentence
# to YYYY-MM-DD
def convert_date_sentence(sentence):

    months = {
        'january':'01', 'february': '02', 'march':'03',
        'april':'04', 'may':'05', 'june': '06', 'july':'07',
        'august':'08', 'september':'09', 'october': '10',
        'november':'11', 'december': '12'
    }

    days = {
        'first':'01', 'second':'02','third':'03', 'fourth':'04', 'fifth':'05'
    }

    parts=sentence.split(" ")
    return f"{parts[-1]}-{months[parts[-2].lower()]}-{days[parts[0].lower()]}" # Return the date iun YYYY-MM-DD format

while True:
    date_sentence=input("Enter the date sentence in format(day of month year):")
    try:
        print(convert_date_sentence(date_sentence))
    except:
        print("There is something wrong with you date sentence.")