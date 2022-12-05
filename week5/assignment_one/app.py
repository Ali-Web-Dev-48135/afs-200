import authorizedUsers
import users
import requests


try:
    response = requests.get('https://randomuser.me/api/?results=10&nat=us')
    
    response.raise_for_status()

    response_to_json = response.json()

    
    for retrieved_user_from_api in response_to_json["results"]:
        newUser = users.User(retrieved_user_from_api['name']['first'], retrieved_user_from_api['name']['last'],retrieved_user_from_api['email']) 
        new_authorized_user = authorizedUsers.AuthorizedUsers()
        new_authorized_user.addUser(newUser)
        newUser.__str__()


except requests.exceptions.HTTPError as httperror:
    print(f"HttpError Has Occured {httperror}")
except requests.exceptions.ConnectionError as connectionError:
    print(f"A connection error has occured {connectionError}")
except requests.exceptions.Timeout as timeoutError:
    print(f"Timeout error occured {timeoutError}")
except requests.exceptions.RequestException as requestError:
    print(f"Request error occured {requestError}")

