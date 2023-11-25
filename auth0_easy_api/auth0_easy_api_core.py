

import webbrowser
import requests
import json
import jwt

from flask import Flask, request, render_template



##### CLIENT SIDE #####
def open_authentication_page(domain, client_id, audience):
    url="https://"+domain+"/authorize?response_type=code&prompt=login&audience="+audience+"&client_id="+client_id+"&redirect_uri=http://localhost:5000/api/auth/callback" #https://dev.forloop.ai/api/auth/callback




    webbrowser.open(url)



#open_authentication_page(domain, client_id, audience)


##### SERVER SIDE #####

def get_all_users(management_token):
    url = "https://forloop-cloud-dev.eu.auth0.com/api/v2/users"
    payload = {}
    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer '+management_token
    }
    print(headers)
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.content)
    
    return(result)
    

def get_management_token(domain, client_id, client_secret, audience):
        
    
    headers = { 'content-type': "application/x-www-form-urlencoded" ,}
    
    url="https://"+domain+"/oauth/token"
    print(url)

    response=requests.post(url, headers=headers, data={
        "grant_type":"client_credentials",
        "client_id":client_id,
        "client_secret":client_secret,
        "audience":audience,
        #"scope":"read:users",
        })
    
    print(response.content)
    management_token=json.loads(response.content).get("access_token")
    
    return(management_token)
    


def generate_flask_callback_app(domain, client_id, client_secret, audience, store_user_function=None, logged_in_html_template="logged.html"):
    app = Flask(__name__)
    
    @app.route('/api/auth/callback')
    def callback():
        # Extract the fragment from the URL
        url = request.url#.split('#')[1]
        print(url)
    
        authorization_code=url.split("code=")[1]
        
        response=requests.post("https://"+domain+"/oauth/token", json=
                      {"grant_type": 'authorization_code',
             "client_id": client_id,
             "client_secret": client_secret,
             "code": authorization_code,
             "redirect_uri": 'http://localhost:5000/api/auth/callback',
             "audience":audience,
             "scope":"openid profile email offline_access"})
        print(response.content)  
        
        result=json.loads(response.content)
        print(result)
        token=result["access_token"]
        print(token)
        
        decoded_result=jwt.decode(token ,algorithms=["RS256"], options={"verify_signature": False})
    
        print(decoded_result)
        sub=decoded_result.get("sub")
        print(sub)
        management_token=get_management_token(domain, client_id, client_secret, audience)
        print(management_token)
        all_users=get_all_users(management_token)
        print(all_users)
        user_index=[x["user_id"] for x in all_users].index(sub)
        print(all_users[user_index])
        user=all_users[user_index]
        if store_user_function is not None:
            try:
                store_user_function(user)
            except Exception as e:
                print("User couldn't be stored, check that your store_user_function has exactly one input, the error message:",e)
        else:
            print("User was validated but wasn't stored anyhow, check that you defined 'store_user_function' parameter")
            
        
        
     
        return render_template(logged_in_html_template)
    
    
    
        #return jsonify(fragment)
    return(app)
    


#if __name__ == '__main__':
#    app=generate_flask_callback_app(domain, client_id, client_secret, audience)
#    app.run(debug=True)