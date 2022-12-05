#Flask Imports
from flask import Flask, render_template
import json
from flask import request

#Class Imports
import fetchusers
import addresslisting

app = Flask(__name__)


addressbookObject = addresslisting.AddressBook()
fetchedUserObject = fetchusers.FetchUsers()


for userFetched in fetchedUserObject.populate_fetched_users_list(fetchedUserObject.fetch_users_from_api()):
    contactObject = addresslisting.Contact(userFetched['name']['first'],userFetched['name']['last'],userFetched['email'],userFetched['phone'],userFetched['picture']['medium'])
    
    #Populates the addrressbook with the created contact objects.
    addressbookObject.addAddress(contactObject)

@app.route("/home")
@app.route("/")
def get_all():
        return render_template('index.html', users=addressbookObject.getAllAddresses())


@app.route("/search", methods=['POST'])
def find_user():
    user_value = request.form.get('user_name')
    return render_template('index.html', users=addressbookObject.findAllMatching(user_value))