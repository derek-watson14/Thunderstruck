from flashcardz_app import create_app

app = create_app()

if __name__ == "main":
    app.run(host="127.0.0.1:5000")