# Exercice tiré de https://alan-turing-institute.github.io/rsd-engineeringcourse/ch00python/010exemplar.html
import matplotlib
# À ajouter pour linux
# matplotlib.use('TkAgg')

import geopy
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import imageio.v2 as imageio
import numpy as np


def geolocate(geocoder, place):
    return geocoder.geocode(place, exactly_one=False)[0][1]


def request_map_at(lat, long, satellite=True, zoom=9, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)


def map_at(*args, **kwargs):
    return request_map_at(*args, **kwargs).content


def display_image(im):
    pixels = imageio.imread(BytesIO(im))
    plt.figure()
    plt.imshow(pixels)
    plt.show()

def display_images(images):
    nb_images = len(images)
    plt.figure()
    for i in range(nb_images):
        pixels = imageio.imread(BytesIO(images[i]))
        ax = plt.subplot(1, nb_images, i+1)
        ax.imshow(pixels)
    plt.show()

def is_green(pixels):
    threshold = 1.1
    greener_than_red = pixels[:, :, 1] > threshold * pixels[:, :, 0]
    greener_than_blue = pixels[:, :, 1] > threshold * pixels[:, :, 2]
    green = np.logical_and(greener_than_red, greener_than_blue)
    return green


def show_green_in_png(im):
    pixels = imageio.imread(BytesIO(im))
    print(pixels.shape)
    print(pixels.min(), pixels.max())
    green = is_green(pixels)

    # Créer l'image de couverture végétale et changer en uint8
    out = (green[:, :, np.newaxis] * np.array([0, 255, 0])[np.newaxis, np.newaxis, :]).astype(np.uint8)

    buffer = BytesIO()
    result = imageio.imwrite(buffer, out, format='png')
    return buffer.getvalue()


def pourcentage_vegetal(im):
    pixels = imageio.imread(BytesIO(im))
    number_of_pixels = pixels.shape[0] * pixels.shape[1]
    resultat = np.sum(is_green(pixels)) / number_of_pixels * 100
    return round(resultat, 2)


def location_sequence(start, end, steps):
    lats = np.linspace(start[0], end[0], steps)
    longs = np.linspace(start[1], end[1], steps)
    return np.vstack([lats, longs]).transpose()


if __name__ == "__main__":
    ville = 'Montreal'  # Montreal, Quebec, Magog, Sherbrooke

    geocoder = geopy.geocoders.Nominatim(user_agent="couverture-vegetale")


    montreal_location = geolocate(geocoder, ville)
    print(f'La latitude et longitude de {ville} sont {montreal_location}')

    map_png = map_at(*montreal_location)

    # Calcul de la couverture végétale
    #display_image(map_png)
    #display_image(map_at(*montreal_location, satellite=False))
    #display_image(show_green_in_png(map_png))
    print(f'La couverture végétale de {ville} est {pourcentage_vegetal(map_png)} %')
    display_images([map_png, map_at(*montreal_location, satellite=False), show_green_in_png(map_png)])

    ###############################################################################################################################################################
    # Calcul de la couverture végétale entre Montréal et Québec et entre Montréal et Sherbrooke
    # Création de la figure
    # fig, (ax1, ax2) = plt.subplots(1, 2)

    # # Graphique des données pour chaque trajet
    # ax1.plot([pourcentage_vegetal(map_at(*location)) for location in location_sequence(geolocate(geocoder, "Montreal"), geolocate(geocoder, "Quebec"), 10)])
    # ax1.set_title('Montréal-Québec')

    # ax2.plot([pourcentage_vegetal(map_at(*location)) for location in location_sequence(geolocate(geocoder, "Montreal"), geolocate(geocoder, "Sherbrooke"), 10)])
    # ax2.set_title('Montréal-Sherbrooke')

    # # Ajouter un xlabel et ylabel globaux
    # fig.supxlabel("Position entre les villes (points intermédiaires)")
    # fig.supylabel("Pourcentage de couverture végétale (%)")

    # # Afficher la figure
    # plt.show()


