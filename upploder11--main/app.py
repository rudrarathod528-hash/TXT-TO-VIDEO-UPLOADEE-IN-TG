from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TXT-TO-VIDEO Uploader</title>
    <style>
        body {
            background: #0f0f1a;
            color: #fff;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding-top: 80px;
        }
        h1 { color: #00e5ff; }
        p { color: #bbb; }
        .badge {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #1a1a2e;
            border-radius: 8px;
            color: #00e5ff;
        }
    </style>
</head>
<body>
    <h1>TXT-TO-VIDEO Uploader</h1>
    <p>Telegram bot that converts TXT links into videos and uploads them.</p>
    <div class="badge">Bot is running 🟢</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
