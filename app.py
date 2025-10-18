from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# simple HTML template
html = """
<!DOCTYPE html>
<html>
<head><title>Guess The Number</title></head>
<body>
  <h2>Guess The Number Game</h2>
  <form method="POST">
    <p>Guess a number between 1 and 100:</p>
    <input name="guess" type="number" min="1" max="100" required>
    <input type="submit" value="Submit">
  </form>
  <p>{{ message }}</p>
</body>
</html>
"""

number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    global number
    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess < number:
            message = "Too low! Try again."
        elif guess > number:
            message = "Too high! Try again."
        else:
            message = f"🎉 Correct! The number was {number}. Starting new game..."
            number = random.randint(1, 100)
    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run()
