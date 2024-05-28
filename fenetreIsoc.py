from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
from map import generer_map
from map import open_map
def page_input():
    global pays,pageCo,entry_ville,entry_latitude,entry_longitude,entry_rayon,entry
    set_appearance_mode("light")
    pageCo=CTk()
    pageCo.geometry("300x400")
    # pas d'agrandissement de page
    pageCo.resizable(False, False)
    pageCo.title("input")


    frame=CTkFrame(master=pageCo,width= 300,height=400)
    frame.place(x=0,y=0)

    ###########################################   emplacement   #####################################################
    ####   ville   ####
    label_emplacement=CTkLabel(frame, text='emplacement de la recherche de réseau', font=('Helvetica',12, "bold" ))
    label_emplacement.place(x=5, y=30, anchor="w")
    entry_ville=CTkEntry(frame,width=175,placeholder_text="nom de la ville ")
    entry_ville.place(x=60,y=60,anchor="w")
    #### Latitude/Longitude   ####

    entry_latitude=CTkEntry(frame,width=85,placeholder_text="latitude")
    #entry_latitude.place(x=60,y=90,anchor="w")


    entry_longitude=CTkEntry(frame,width=85,placeholder_text="longitude ")
    #entry_longitude.place(x=150,y=90,anchor="w")


    ###########################################  limite   #####################################################
    label_limite=CTkLabel(frame, text='limite du réseau ', font=('Helvetica',12, "bold" ))
    label_limite.place(x=5, y=140, anchor="w")

    #### liste des pays  ####


    def on_select(event):
        selected_items = event.widget.curselection()
        selected_values = [event.widget.get(i) for i in selected_items]
        entry.delete(0, END)
        entry.insert(0, ', '.join(selected_values))
        dropdown.place_forget()

    def on_entry_click(event):
        dropdown.pack(side=TOP, fill=BOTH)

    def on_canvas_click(event):
        dropdown.place_forget()



    # Créer un Canvas ou un Frame pour encadrer la Listbox
    canvas = Canvas(frame, width=200, height=200)
    canvas.place(x=115, y=280, anchor="w")
    canvas.bind('<Button-1>', on_canvas_click)

    # Créer une Listbox
    listbox = Listbox(canvas, selectmode=MULTIPLE)

    ###################### Insérer des éléments dans la Listbox mettre les payer plus tard ############################
    
    #LISTE DES PAYS A METTRE PLUS TARD !!
    pays = ["Afganistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
                "Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina",
                "Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic",
                "Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica",
                "Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland",
                "France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras",
                "Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Iceland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya",
                "Kiribati","Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia",
                "Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali",
                "Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco"
                "Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia",
                "Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar",
                "Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino",
                "Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia",
                "Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland",
                "Syria","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan",
                "Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City",
                "Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
    
    for i in range(len(pays)):
        listbox.insert(END, pays[i])

    # Lier une fonction à l'événement de sélection
    listbox.bind('<<ListboxSelect>>', on_select)

    # Créer un widget Frame pour encadrer la Listbox (optionnel)
    dropdown = Frame(canvas)
    listbox.pack(side=TOP, fill=BOTH)

    # Créer une Entry
    entry = Entry(frame)
    entry.place(x=115, y=380, anchor="w")
    entry.bind('<Button-1>', on_entry_click)

    #### Rayon ####

    entry_rayon=CTkEntry(frame,width=100,placeholder_text="rayon en km")
    entry_rayon.place(x=92,y=340,anchor="w")

    ##################################### bouton de recherche ###################################
    boutonrecherche=CTkButton(frame, text="rechercher",fg_color="grey",hover_color="white",command=recherche)
    boutonrecherche.place(x=75,y=375,anchor="w")
    pageCo.mainloop()

def recherche():
    global pays,pageCo,entry_ville,entry_latitude,entry_longitude,entry_rayon,entry
    ville=entry_ville.get()
    latitude=entry_latitude.get()
    longitude=entry_longitude.get()
    rayon=entry_rayon.get()
    liste_pays=entry.get()
    if liste_pays == "":
        liste_pays = pays
        print("pays vide")
    else:
        liste_pays=liste_pays.split(", ")

    if ville == "":
        couverture,nb_petit,nb_moyen,nb_large,ixps=generer_map(lat=float(latitude),lon=float(longitude),distance=int(rayon),pays=liste_pays)
    elif latitude == "" or longitude == "":
        couverture,nb_petit,nb_moyen,nb_large,ixps=generer_map(city=str(ville),distance=int(rayon),pays=liste_pays)
    else:
        messagebox.showerror("Erreur","Veuillez renseigner soit la ville soit la latitude et la longitude")
    pageCo.destroy()
    page_output(couverture,nb_petit,nb_moyen,nb_large,ixps)

def page_output(couverture,nb_petit,nb_moyen,nb_large,ixps):
    print(f"couverture : {round(couverture,2)}% des points pris en compte")
    print(f"nombre de petits : {nb_petit}")
    print(f"nombre de moyens : {nb_moyen}")
    print(f"nombre de larges : {nb_large}")

    for ixp in ixps:
        print(ixp)

    set_appearance_mode("light")
    pageCo=CTk()
    pageCo.geometry("300x450")
    # pas d'agrandissement de page
    pageCo.resizable(False, False)
    pageCo.title("output")


    frame=CTkFrame(master=pageCo,width= 300,height=450)
    frame.place(x=0,y=0)


    ###################################  ###############
    label_emplacement=CTkLabel(frame, text='pourcentage de reseau atteignable ', font=('Helvetica',12, "bold" ))
    label_emplacement.place(x=5, y=30, anchor="w")
    entry_pourcentage=CTkLabel(frame,width=25,text=str(f"couverture : {round(couverture,2)}% des points pris en compte"))
    entry_pourcentage.place(x=25,y=60,anchor="w")
    #### nb de point d'internet    ####
    label_nb=CTkLabel(frame, text='nombre de points d\'internet ', font=('Helvetica',12, "bold" ))
    label_nb.place(x=5, y=90, anchor="w")
    
    
    entry_large=CTkLabel(frame,width=85,text=f"nombre de larges : {nb_large}")
    entry_large.place(x=5,y=125,anchor="w")


    entry_moyen=CTkLabel(frame,width=85,text=f"nombre de moyens : {nb_moyen}")
    entry_moyen.place(x=5,y=145,anchor="w")

    entry_petit=CTkLabel(frame,width=85,text=f"nombre de petits : {nb_petit}")
    entry_petit.place(x=5,y=165,anchor="w")

    
    boutoncarte=CTkButton(frame, text="afficher la carte",fg_color="grey",hover_color="white",command=lambda: [open_map()])
    boutoncarte.place(x=75,y=190,anchor="w")

    label_nb=CTkLabel(frame, text='liste des points', font=('Helvetica',12, "bold" ))
    label_nb.place(x=5, y=230, anchor="w")
    # Créer un Canvas ou un Frame pour encadrer la Listbox
    canvas = Canvas(frame, width=200, height=120)
    canvas.place(x=100, y=410, anchor="w")
    canvas.bind('<Button-1>')

    # Créer une Listbox
    listbox = Listbox(canvas)

    ###################### Insérer des éléments dans la Listbox mettre les payer plus tard ############################
    for ixp in ixps:
        listbox.insert(END, f"IXP n°{ixp.id} ({ixp.city})")

    # Lier une fonction à l'événement de sélection
    listbox.bind('<<ListboxSelect>>')

    # Créer un widget Frame pour encadrer la Listbox (optionnel)
    dropdown = Frame(canvas)
    listbox.pack(side=TOP, fill=BOTH)

    
    


    pageCo.mainloop()

page_input()