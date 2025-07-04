# init python:
#     import requests

# label show_players:
#     # python block
#     python:
#         try:
#             url = "http://humancc.site/ndhos/renpy_backend/fetch_name.php"
#             response = requests.get(url)
#             if response.status_code == 200:
#                 players = response.json()
#             else:
#                 players = ["Failed to fetch names."]
#         except Exception as e:
#             players = [f"Error: {e}"]
            
#     # renpy block
#     "Here are the recent players:"

#     # pyhton block
#     python:
#         for name in players:
#             renpy.say(None, name)

#     return

label show_players:
    python:
        import requests
        try:
            response = requests.get("http://humancc.site/ndhos/renpy_backend/fetch_name.php")
            recent_players = response.json()
        except Exception as e:
            recent_players = [f"Error: {e}"]

    $ name_count = len(recent_players)
    $ i = 0
    while i < name_count:
        $ name = recent_players[i]
        narrator "[name]{w=2.0}{nw}"
        $ i += 1
    return
