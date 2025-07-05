# init python:
#     import requests

# label start:
#     scene bg room

#     "Welcome to the game!"

#     $ player_name = renpy.input("What's your name?")
#     $ player_name = player_name.strip()

#     if player_name == "":
#         "You didn't enter a name."
#     else:
#         "Nice to meet you, [player_name]!"

#         python:
#             try:
#                 # Send the name to the backend
#                 url = "http://humancc.site/ndhos/renpy_backend/save_name.php"
#                 data = {'name': player_name}
#                 response = requests.post(url, data=data)
#                 if response.status_code == 200:
#                     "Your name has been saved to the database!"
#                 else:
#                     "Oops! Failed to save your name."
#             except Exception as e:
#                 "Error: [e]"

#     "Let's start your adventure!"

#     return

# init python:
#     import requests

# label start:
#     "Welcome back!"
#     call show_players
#     "Let's continue the game..."
#     return

init python:
    import requests

label start:
    window hide
    scene zenitsu:
        zoom 2.00

    $ renpy.pause(2.0)

    window show
    narrator "Welcome back!{w=1.0}{nw}"
    call show_players
    narrator "Let's continue the game...{w=1.0}{nw}"

    return
