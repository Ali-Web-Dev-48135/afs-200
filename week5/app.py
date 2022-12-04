import authorizedUsers
import requests


try:
    response = requests.get('https://randomuser.me/api/?results=10&nat=us')
    
    response_to_json = response.json()

    
    for retrieved_user_from_api in response_to_json["results"]:
        authorizedUsers.AuthorizedUsers(retrieved_user_from_api["name"]["first"], retrieved_user_from_api["name"]["last"], retrieved_user_from_api["email"])

except requests.exceptions.HTTPError as httperror:
    print(f"HttpError Has Occured {httperror}")
except requests.exceptions.ConnectionError as connectionError:
    print(f"A connection error has occured {connectionError}")
except requests.exceptions.Timeout as timeoutError:
    print(f"Timeout error occured {timeoutError}")
except requests.exceptions.RequestException as requestError:
    print(f"Request error occured {requestError}")

for saved_user in authorizedUsers.AuthorizedUsers.print_authorized_users():
    print(f"{saved_user['fName']} {saved_user['lName']} ({saved_user['email']})")
