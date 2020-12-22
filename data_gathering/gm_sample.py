import google_streetview.api as sv 
import googlemaps

# API key
ky = ''
gmaps = googlemaps.Client(key=ky)

# get geocoords of desired address
gc = gmaps.geocode('43423 Squirrel Ridge Place, Leesburg, VA')

# set params for image retrieval
sz = '600x600'
coords = gc[0]['geometry']['location']
loc = '{},{}'.format(coords['lat'],coords['lng'])
params = [{'size':sz,'location':loc,'key':ky}]

# retrieve image
res = sv.results(params)
res.download_links('maces')