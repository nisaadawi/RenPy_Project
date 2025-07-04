init python:
    import requests

label show_players:
    # python block
    python:
        try:
            url = "http://humancc.site/ndhos/renpy_backend/fetch_name.php"
            response = requests.get(url)
            if response.status_code == 200:
                players = response.json()
            else:
                players = ["Failed to fetch names."]
        except Exception as e:
            players = [f"Error: {e}"]
            
    # renpy block
    "Here are the recent players:"

    # pyhton block
    python:
        for name in players:
            renpy.say(None, name)

    return
