import twitter
api = twitter.Api(consumer_key='G8M055F3K6LVIcn4Je6XGtyjc',
    consumer_secret='L6y0da736ownLW7QDsUi76sCjYxikdimUOLObA6w69CnbUlOCA',
    access_token_key='1445765872505655303-6Nw5KoA7ofuoIHeL9LgxJHAcIpPnjP',
    access_token_secret='uBjBs8sFPyVNZLLaupNkpc1gJlWpAxgAkxZCFaPIkHD49')
status = api.PostUpdate('I love python-twitter!')
print(status.text)