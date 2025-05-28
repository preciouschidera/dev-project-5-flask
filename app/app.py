from flask import Flask

app = Flask(__name__)

@app.route('/')
def dashboard():
    return """
    <html>
    <head>
        <style>
            body {
                background-color: purple;
                color: white;
                font-family: Arial, sans-serif;
                padding: 40px;
                text-align: center;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 0.5em;
            }
            p {
                font-size: 1.5em;
                margin-top: 0.2em;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Flask Monitoring Dashboard</h1>
        <p><strong>God help me na die I dey with this DEVOPS</strong></p>
        <p><em>THANK YOU CYNTHIA FOR EVERYTHING</em></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()

