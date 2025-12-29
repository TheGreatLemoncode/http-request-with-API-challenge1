from flask import Flask, jsonify, request, redirect

app = Flask(__name__)


@app.route("/")
def main():
    """
    Docstring pour main
    """
    return redirect("/api", 302)

@app.route("/api")
def api_index():
    """
    Docstring pour api_index
    """
    liste = ['banane', 'orange', 'pomme']
    return jsonify(liste)


if __name__ == '__main__':
    app.run('0.0.0.0')
