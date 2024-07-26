#flask application

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/', methods = ['get'])

def home():
  html_content="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        main {
            background-color: white;
            padding: 20px;
            margin-top: 20px;
        }
        footer {
            background-color: #ddd;
            text-align: center;
            padding: 10px 0;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My First VCC Assignment</h1>
    </header>
    <main>
        <h2>Introduction to Cloud Computing</h2>
        <p>Cloud computing refers to the delivery of computing services over the internet ("the cloud").</p>
        <p>These services include storage, processing power, databases, networking, software, and analytics.</p>
        <p>Rather than owning and maintaining physical data centers or servers, organizations can rent access to these services from cloud providers, paying only for what they use.</p>
    </main>
    <footer>
        <p>&copy; 2024 Simple Web Page</p>
    </footer>
</body>
</html>

"""
  return render_template_string(html_content)
if __name__== "__main__":
 app.run(debug=True,host="0.0.0.0", port = 5000)
