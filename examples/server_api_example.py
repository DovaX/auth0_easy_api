from auth0_easy_api import generate_flask_callback_app

domain="xxxxxxx.eu.auth0.com"
client_id="yrkFiXhdjkljkljkjklgwYPLRHH"
client_secret = "u074UGaOmZsfjkhkjahvlkjhdFVf4p08jjyjvwI3-gPEs0sXY52"
audience="https://xxxxxxx.eu.auth0.com/api/v2/"


def store_user_function(user):
    with open("user_data.txt","w+") as file:
        file.write(str(user))
        
app=generate_flask_callback_app(domain, client_id, client_secret, audience, store_user_function=store_user_function)
app.run()


