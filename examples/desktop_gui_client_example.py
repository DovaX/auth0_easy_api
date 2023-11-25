from auth0_easy_api.auth0_easy_api import open_authentication_page
import dogui.dogui_core as dg #Simple gui library

domain="xxxxxxx.eu.auth0.com"
client_id="yrkFiXhdjkljkljkjklgwYPLRHH"
client_secret = "u074UGaOmZsfjkhkjahvlkjhdFVf4p08jjyjvwI3-gPEs0sXY52"
audience="https://xxxxxxx.eu.auth0.com/api/v2/"


def authenticate():    
    open_authentication_page(domain, client_id, audience)


gui=dg.GUI()
button=dg.Button(gui.window, "Authenticate", authenticate, 1, 1)
gui.build_gui()



