from flask import Flask
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    # --- Insights Data (for the chart) ---
    posts = ["Post 1", "Post 2", "Post 3", "Post 4"]
    interested = [3, 4, 2, 3]  # Example: number of people who asked to sign up
    ready = [2, 5, 3, 2]       # Example: number of people ready to start classes

    # Plot bar chart
    fig, ax = plt.subplots()
    ax.bar(posts, interested, label="Asked to Sign Up", color="#ff66cc")
    ax.bar(posts, ready, bottom=interested, label="Ready to Start", color="#cc66ff")
    ax.set_title("Instagram Training Interest")
    ax.set_ylabel("Number of People")
    ax.legend()

    # Convert plot to base64 for embedding in HTML
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()

    # --- HTML with Embedded Chart + Registration Info ---
    html = f"""
    <html>
    <head>
        <title>SkillShift Registration</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background-color: #1a1a1a;
                color: #f0f0f0;
                text-align: center;
                padding: 2em;
            }}
            .tagline {{
                font-size: 1.5em;
                color: #ff99cc;
                margin-bottom: 1em;
            }}
            .panel {{
                background-color: #333333;
                border-radius: 15px;
                padding: 2em;
                margin: 2em auto;
                max-width: 600px;
                box-shadow: 0 0 10px #ff4ddb;
            }}
            .cta-button {{
                background-color: #ff4ddb;
                color: white;
                padding: 0.8em 2em;
                border: none;
                border-radius: 5px;
                font-size: 1.1em;
                cursor: pointer;
                transition: background 0.3s;
            }}
            .cta-button:hover {{
                background-color: #ff1fbb;
            }}
            .chart-section {{
                margin-top: 3em;
            }}
            .credit {{
                margin-top: 3em;
                font-size: 0.9em;
                color: #999999;
                font-style: italic;
            }}
        </style>
    </head>
    <body>

        <h1>🚀 SkillShift Training Registration Open!</h1>
        <div class="tagline">Take the first step toward a brighter tech future 🌟</div>

        <div class="panel">
            <p>💻 Data Analysis • Azure Cloud • AWS DevOps • Cybersecurity • Web Development</p>
            <p>🔥 Real training. No cost. Just growth.</p>
            <p>🚀 Automated with Ansible, served via NGINX + Gunicorn</p>
            <p>📍 Deployed on AWS EC2 — powered by Flask</p>
            <button class="cta-button" onclick="window.open('https://Ceeyitsoluions.com', '_blank')">Register Now</button>
        </div>

        <div class="chart-section">
            <h2>📊 Instagram Interest Insight</h2>
            <p>This chart shows engagement from our last 4 posts.</p>
            <img src="data:image/png;base64,{chart_url}" width="500"/>
        </div>

        <div class="credit">— Built by Precious Chidera 💜</div>

    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


