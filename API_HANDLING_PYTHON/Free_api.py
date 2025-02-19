import requests 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_user', methods=['GET', 'POST'])
def get_random_user():
    # If the request method is POST, proceed to fetch the random user
    if request.method == "POST":
        url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
        response = requests.get(url)
        data = response.json()
        if data.get("success") and "data" in data:
            user_data = data["data"]
            user_name = user_data["login"]["username"]
            user_country = user_data["location"]["country"]
            return f"{user_name} is from {user_country}"
        else:
            return "Failed to fetch data", 500
    # If the request is GET, you could redirect or inform the user to use the form.
    return "Please submit the form to get a random user."

if __name__ == "__main__":
    app.run(debug=True)
