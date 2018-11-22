from flask import Flask, render_template, request
import requests
app = Flask("MyApp")

def send_simple_message(email): ##API mailing
    return requests.post(
        "https://api.mailgun.net/v3/sandbox193ed7f036fb471ba1c573815b69fa46.mailgun.org/messages", ##link to API
        auth=("api", "ce8a6a1a50fb81f573661d3a1be5e4bd-9525e19d-2fb4b8ed"),
        data={"from": "Excited User <mailgun@sandbox193ed7f036fb471ba1c573815b69fa46.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

#@app.route("/email")
#def email():
   # send_simple_message()
   # return "Email sent"

@app.route("/") ##land a hello page, no need to type anything after / to run
def hello():
    return "Hello World"

@app.route("/<name>") ##gets details after /, usable if there are loads of pages
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"]) ##decorator starts with @, it is a path or route to somewhere
def sign_up():
    form_data = request.form
    email = form_data["email"]
    send_simple_message(email)
    return "Email sent to: {}".format(email)

app.run(debug=True) ##make sure Flask runs and tells if there is any errors
