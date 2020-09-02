import json
import requests
import yagmail

try:
    # Get config
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Query endpoint and store results
    yag = yagmail.SMTP(config['sender'])
    resp = requests.get(config['queryUrl'])
    data = resp.json()
    results = data['results']

    # Get Database and store in dictionary
    database = {}
    with open('database.json') as json_file:
        database = json.load(json_file)

    # Check for new items and store them
    new_items = {}
    for result in data['results']:
        if result['uid'] not in database:
            database[result['uid']] = {
                'image_url': result['image_url'], 'url': result['url'], 'name': result['name']}
            new_items[result['uid']] = {
                'image_url': result['image_url'], 'url': result['url'], 'name': result['name']}

    # Update Database
    with open('database.json', 'w') as json_file:
        json.dump(database, json_file)

    # If new items exist, send email to recipient
    if new_items:
        items = ""
        baseUrl = config['baseUrl']
        for _, val in new_items.items():
            img = val['image_url']
            href = val['url']
            name = val['name']
            items += f'<div class="col col-auto"><a href="{baseUrl}{href}"><figure class="figure" style="margin:0 !important;"><img style="padding:50px;background-color:white;" width="252" height="414" src="{img}" alt="patagonia product" /><figcaption class="figure-caption" style="text-align:center;color:black;background-color:white;">{name[:25]}</figcaption></figure></a></div>'
        contents = f"""<!DOCTYPE html><html><head><!-- CSS only --><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" crossorigin="anonymous"></head><body style="background-color:#252732"><div class="container" style="background-color:black;"><div class="row"><div class="col"><h1 style="font-size:6vw;color:white;text-align:center;">👋 New Patagonia!</h1></div></div><div class="row justify-content-center no-gutters">{items}</div></div></body></html>"""
        # print(contents)
        yag.send(to=config['recipient'],
                 subject=config['emailTitle'], contents=contents)
    else:
        print('No new items!')
except Exception as error:
    print(f"Error, email was not sent: {error}")
