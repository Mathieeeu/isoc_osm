import folium
import folium.features
import osmnx as ox
import json
import webbrowser
ox.config(use_cache=True, log_console=True)

class IXP:
    def __init__(self, id, city, lat, lon, pays, iata=None):
        self.id = id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.pays = pays
        self.iata = iata

    def __str__(self):
        return f"IXP {self.id} in {self.city} ({self.lat}, {self.lon}) - {self.pays} - IATA:{self.iata}"
    
    def __repr__(self) -> str:
        return str(self)
    

def get_city_from_coords(lat, lon):
    gdf = ox.geocode_to_gdf({'latitude': lat, 'longitude': lon})
    return gdf['name'].iloc[0]

def get_coords_from_city(city):
    gdf = ox.geocode_to_gdf(city)
    return gdf['geometry'].iloc[0].centroid.y, gdf['geometry'].iloc[0].centroid.x


def get_ixps(file):
    """
    trouve l'id, la ville, la latitude et la longitude depuis le json ({}>fac>[]data>{}id)
    """
    ixps = []
    #si fichier json
    if file.endswith(".json"):
        json_file = file
        with open(json_file, "r") as f:
            data = json.load(f)
            for ixp in data['fac']['data']:
                ixps.append(IXP(ixp['id'], ixp['city'], ixp['latitude'], ixp['longitude'], ixp['country']))
    elif file.endswith(".csv"):
        csv_file = file
        i=0
        with open(csv_file, "r") as f:
            for line in f:
                if i==0:
                    i+=1
                    continue
                line = line.split(";")
                if line[7]=="Yes":
                    iata = line[8][:-1]
                    if len(iata)>1:
                        ixps.append(IXP(i, line[1], float(line[5]), float(line[6]), line[0], iata))
                    else:
                        ixps.append(IXP(i, line[1], float(line[5]), float(line[6]), line[0]))
                    i+=1
    return ixps

def get_color(liste_couleurs_icones,distance):
    """
    retourne la couleur et l'icone correspondant à la distance
    """
    for i in range(len(liste_couleurs_icones)-1):
        if liste_couleurs_icones[i][0]<=distance<liste_couleurs_icones[i+1][0]:
            return liste_couleurs_icones[i][1],liste_couleurs_icones[i][2]
    return liste_couleurs_icones[-1][1],liste_couleurs_icones[-1][2]

def placer_marqueurs(map, ixps, city=None, distance=1000, pays=[], couleurs=[0,'red','cloud']):
    """
    Ajoute un marqueur pour chaque IXP dans la carte map s'il se situe à moins de distance km de la ville city (si city est renseignée, sinon tous les IXP sont ajoutés)
    """
    ok = 0
    paok = 0
    papri = 0
    nb_petit = 0
    nb_moyen = 0
    nb_large = 0
    ixp_ok = []
    if city is not None:
        lat, lon = get_coords_from_city(city)
        folium.Marker(
            [lat, lon], 
            popup=f"{city}",
            icon=folium.Icon(color='pink', icon='home', prefix='fa')
        ).add_to(map)
    for ixp in ixps:
        try :
            if city is not None and len(pays)!=0:
                if city is not None:
                    distance_a_ville=ox.distance.great_circle(lat, lon, ixp.lat, ixp.lon)/1000
                if (city is not None and distance > distance_a_ville) and (len(pays)!=0 and ixp.pays in pays):
                    color,icon = get_color(couleurs,distance_a_ville)
                    if color == 'lightgreen':
                        nb_petit+=1
                    elif color == 'beige':
                        nb_moyen+=1
                    else:
                        nb_large+=1
                    # liste de tous les icones possibles sur folium : https://fontawesome.com/v4.7.0/icons/
                    if city is not None:
                        folium.Marker(
                            [ixp.lat, ixp.lon], 
                            popup=f"{ixp.city} ({ixp.pays}-{int(distance_a_ville)}km)",
                            icon=folium.Icon(color=color,icon=icon, prefix='fa')
                        ).add_to(map)
                    else:
                        folium.Marker(
                            [ixp.lat, ixp.lon], 
                            popup=f"{ixp.city}({ixp.pays})",
                            icon=folium.Icon(color=color,icon=icon, prefix='fa')
                        ).add_to(map)  
                    ixp_ok.append(ixp)
                    ok += 1
                else:
                    papri += 1
            else:
                color,icon = get_color(couleurs,distance_a_ville)
                if color == 'lightgreen':
                    nb_petit+=1
                elif color == 'beige':
                    nb_moyen+=1
                else:
                    nb_large+=1
                folium.Marker(
                    [ixp.lat, ixp.lon], 
                    popup=f"{ixp.city} ({ixp.pays})",
                    icon=folium.Icon(color=color, icon=icon, prefix='fa')
                ).add_to(map)
                ok += 1
        except:
            paok += 1
    print(f"{ok} marqueurs placés, {papri} non-pris en compte,{paok} erreurs")
    couverture = ok/len(ixps)*100
    return couverture,nb_petit,nb_moyen,nb_large,ixp_ok

def triee_ixp(ixps, city, distance=0):
    """
    retourne la liste des ixps à moins de distance km de la ville city triés par distance croissante
    """
    ok = 0
    paok = 0
    papri = 0
    lat, lon = get_coords_from_city(city)
    liste_triee = []
    for ixp in ixps:
        try :
            distance_a_ville=ox.distance.great_circle(lat, lon, ixp.lat, ixp.lon)/1000
            if distance > distance_a_ville or distance == 0:
                liste_triee.append((ixp, distance_a_ville))
                ok += 1
            else:
                papri += 1
        except:
            paok += 1
    print(f"{ok} marqueurs placés, {papri} non-pris en compte,{paok} erreurs")
    liste_triee.sort(key=lambda x: x[1])
    return liste_triee

def generer_map(city=None,lat=None,lon=None,distance=500,pays=[]):
    map = folium.Map(location=[48.8566, 2.3522], zoom_start=2)
    # ixps = get_ixps("peeringdb_2_dump_2021_03_01.json")
    ixps = get_ixps("ixp_active.csv")

    couverture,nb_petit,nb_moyen,nb_large,ixps_ok = placer_marqueurs(map, ixps, city, distance, pays, couleurs=[[0,'lightgreen','battery-three-quarters'],[250,'beige','battery-half'],[700,'red','battery-quarter']])
    map.save("map.html")


    return couverture,nb_petit,nb_moyen,nb_large,ixps_ok

def open_map():
    # Open the "map.html" file in the default web browser
    webbrowser.open("map.html")

