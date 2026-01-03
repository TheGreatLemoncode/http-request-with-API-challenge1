from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# This is our api. It will run on all interface from now 
# but can also run on localhost. His role will be to feed data 
# to the app and verify connections as if it had a database

@app.route("/")
def main():
    """
    Docstring pour main
    """
    return redirect("/api", 302)

@app.route("/api", methods=['GET', 'POST'])
def api_index():
    """
    Docstring for api_index
    """
    # Test the post method. When this route is call,
    # teh API try to get the data sent by json and if
    # all is correct with them send a message and a 200 code
    # will polish next time.
     
    if request.method == 'POST':
        data = request.get_json(silent=True)
        print(data)
        if data :
            return jsonify("Donnée reçu"), 200
        else:
            return jsonify("Données pas reçu"), 400

    liste = ['banane', 'orange', 'pomme']
    return jsonify(liste)

@app.route("/api/signup", methods=['POST'])
def api_creation():
    """Route whose role will be to verify user information"""
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify("The data did not arrive"), 400

    return jsonify('The data did arrive at the API'), 200

@app.route("/api/login", methods=['POST'])
def log_in():
    """Route that deal with user log in"""
    data = request.get_json(silent=True)
    response = {}
    if not data:
        response['message'] = 'The post method failed'
        response['connexion'] = False
        return jsonify(response), 400
    
    if data.get('mail') == 'hilemoncode@gmail.com' and data.get('password') == 'thegreatlemon':
        response['connexion'] = True
        response['message'] = f'Bienvenu {data.get('mail')}'
        return jsonify(response), 200
    
    response['connexion'] = False
    response['message'] = 'connexion refused'
    return jsonify(response), 200

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
