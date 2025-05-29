from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>DevOps Journey Dashboard</title>
      <style>
        body {
          background: linear-gradient(to bottom, #3a0ca3, #2f2f2f);
          color: #ffffff;
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          padding: 60px;
          text-align: center;
          animation: fadeIn 2s ease-in;
        }

        h1 {
          font-size: 3.2em;
          margin-bottom: 0.3em;
          color: #e0d7ff;
        }

        .tagline {
          font-size: 1.7em;
          margin-bottom: 2em;
          color: #c2b8ff;
          animation: pulse 2s infinite alternate;
        }

        .panel {
          background-color: #4b0082;
          padding: 25px;
          border-radius: 12px;
          box-shadow: 0 0 20px rgba(0,0,0,0.3);
          margin: 30px auto;
          max-width: 650px;
        }

        .panel p {
          font-size: 1.2em;
          margin: 10px 0;
          color: #f2f2f2;
        }

        .shoutout {
          font-size: 1.3em;
          margin-top: 1.5em;
          color: #ffb3ff;
        }

        .credit {
          margin-top: 2em;
          font-size: 1em;
          color: #cccccc;
          font-style: italic;
        }

        @keyframes fadeIn {
          from { opacity: 0; transform: scale(0.95); }
          to { opacity: 1; transform: scale(1); }
        }

        @keyframes pulse {
          from { transform: scale(1); }
          to { transform: scale(1.03); color: #ffffff; }
        }
      </style>
    </head>
    <body>

      <h1>🚀 Flask App Successfully Deployed</h1>
      <div class="tagline">I’m going to be a GREAT DevOps Engineer in the UK 🇬🇧</div>

      <div class="panel">
        <p>Powered by Flask ⚙️</p>
        <p>Deployed with Gunicorn + NGINX</p>
        <p>Automated using Ansible on AWS EC2 💻</p>
        <p>This is my DevOps journey — from Lagos to London.</p>
      </div>

      <p class="shoutout">God help me, na die I dey with this DevOps </p>
      <p class="shoutout">THANK YOU CYNTHIA FOR EVERYTHING 💜</p>

      <div class="credit">— Built by Precious Chidera | Lagos born, UK made 🌍</div>

    </body>
    </html>
    """

