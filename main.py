# this line will import the "website" package we just created
# add something new
# testing git within VScode
# some update from masin branch
from website import create_app

app = create_app()  # create instance of the application

if __name__ == '__main__':
    # start the development server by enabling debug mode - https://flask.palletsprojects.com/en/2.2.x/quickstart/#debug-mode
    app.run(debug=True)
