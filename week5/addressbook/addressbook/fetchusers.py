import requests

class FetchUsers():
    def __init__(self):
        self.fetched_users_list = []


    #Handles http request to fetch the 25 users.
    def fetch_users_from_api(self):
        try:
            response = requests.get('https://randomuser.me/api/?results=5&nat=us')
            
            
            response.raise_for_status()

            response_to_json = response.json()  
            return response_to_json["results"]

        except requests.exceptions.HTTPError as httperror:
            print(f"HttpError Has Occured {httperror}")
        except requests.exceptions.ConnectionError as connectionError:
            print(f"A connection error has occured {connectionError}")
        except requests.exceptions.Timeout as timeoutError:
            print(f"Timeout error occured {timeoutError}")
        except requests.exceptions.RequestException as requestError:
            print(f"Request error occured {requestError}")

    #Populates the fetched_users_list with the 25 retrieved users from above method.
    def populate_fetched_users_list(self, fetched_list):
        for user in fetched_list:
            self.fetched_users_list.append(user)
        return self.fetched_users_list
