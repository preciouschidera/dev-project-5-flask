from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Skill Shift Tech Training</title>
      <style>
        body {
          background-color: #121212;
          color: #e6e6e6;
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          text-align: center;
          padding: 2em;
          animation: fadeIn 1s ease-in-out;
        }

        h1 {
          color: #00ffff;
          font-size: 2.5em;
          margin-bottom: 0.3em;
        }

        .tagline {
          font-size: 1.2em;
          color: #ffd700;
          margin-bottom: 1em;
        }

        .panel {
          background-color: #1e1e1e;
          padding: 2em;
          border-radius: 12px;
          margin-top: 1.5em;
          box-shadow: 0 0 10px #00ffff44;
        }

        .panel p {
          margin: 0.5em 0;
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

        .cta {
          margin-top: 2em;
        }

        .register-button {
          background-color: #00ffff;
          color: #121212;
          padding: 0.8em 1.5em;
          font-size: 1.2em;
          font-weight: bold;
          text-decoration: none;
          border-radius: 10px;
          transition: all 0.3s ease-in-out;
          box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff80;
          animation: pulse 2s infinite alternate;
        }

        .register-button:hover {
          background-color: #ffd700;
          color: #000;
          box-shadow: 0 0 15px #ffd700, 0 0 25px #ffd70080;
          transform: scale(1.05);
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

      <h1>🚀 Skill Shift Tech Training Program</h1>
      <div class="tagline">Take the first step towards a brighter tech future 🌍</div>

      <div class="cta">
        <a href="#" class="register-button">🚀 Register Now</a>
      </div>

      <div class="panel">
        <p>📊 Data Analysis &nbsp;&nbsp; ☁️ Azure Cloud &nbsp;&nbsp; 🛠️ DevOps with AWS</p>
        <p>🔒 Cybersecurity &nbsp;&nbsp; 🌐 Web Development</p>
        <p>Real training, no cost — just growth. 💡</p>
        <p>Powered by Flask ⚙️ | Deployed on AWS EC2 | Automated with Ansible</p>
      </div>

      <p class="shoutout">Join us and transform your tech career. Learn. Build. Grow. 💪</p>
      <p class="shoutout">THANK YOU SHIFT SKILL & CYNTHIA 💜</p>

      <div class="credit">— Built by Precious Chidera</div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

