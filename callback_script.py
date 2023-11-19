
import requests


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/auth/callback')
def callback():
    # Extract the fragment from the URL
    fragment = request.url#.split('#')[1]
    print(fragment)

    code=fragment.split("code=")[1]
    
    response=requests.post("https://"+domain+"/oauth/token", json=
                  {"grant_type": 'authorization_code',
         "client_id": client_id,
         "client_secret": client_secret,
         "code": code,
         "redirect_uri": 'http://localhost:5000/api/auth/callback'})
    print(response.content)    


    # Perform actions with the fragment as needed
    # For example, you can extract parameters from the fragment
    # # access_token = request.args.get('access_token')
    # # expires_in = request.args.get('expires_in')
    # # token_type = request.args.get('token_type')

    # response_data = {
    #     'access_token': access_token,
    #     'expires_in': expires_in,
    #     'token_type': token_type,
    #     'fragment': fragment,
    # }

    return jsonify(fragment)

if __name__ == '__main__':
    app.run(debug=True)