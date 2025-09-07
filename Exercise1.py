import requests

api_url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

data = {
    "UCID": input("Enter your UCID: "),
    "first_name": input("Enter your first name: "),
    "last_name": input("Enter your last name: "),
    "github_username": input("Enter your github username: "),
    "discord_username": input("Enter your discord username: "),
    "favorite_cartoon": input("Enter your favorite cartoon: "),
    "favorite_language": input("Enter you favorite programming language: "),
    "movie_or_game_or_book": input("Enter favorite movie, game, or book: "),
    "section": input("Enter your section number: ")
}

params = {"UCID": data["UCID"], "section": data["section"]}
response = requests.get(api_url, params=params)
if(response.status_code == 200 and response.json()):
    print("Cannot add duplicate results")
else:
    response = requests.post(api_url, json=data)

    if(response.status_code == 200):
        print("Data submitted")
    else:
        print('Error occured: ', response.text)
