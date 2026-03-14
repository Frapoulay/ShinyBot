
MOVE_NAMES = [
    # Gen I
    "unknown", "Écras'Face", "Poing Karaté", "Torgnoles", "Poing Comète", "Ultimapoing", "Jackpot", "Poing Feu", "Poing Glace", "Poing-Éclair", "Griffe",
    "Force Poigne", "Guillotine", "Coupe-Vent", "Danse Lames", "Coupe", "Tornade", "Cru-Ailes", "Cyclone", "Vol", "Étreinte", "Souplesse", "Fouet Lianes",
    "Écrasement", "Double Pied", "Ultimawashi", "Pied Sauté", "Mawashi Geri", "Jet de Sable", "Coup d'Boule", "Koud'Korne", "Furie", "Empal'Korne", "Charge",
    "Plaquage", "Ligotage", "Bélier", "Mania", "Damoclès", "Mimi-Queue", "Dard-Venin", "Double Dard", "Dard-Nuée", "Groz'Yeux", "Morsure", "Rugissement",
    "Hurlement", "Berceuse", "Ultrason", "SonicBoom", "Entrave", "Acide", "Flammèche", "Lance-Flammes", "Brume", "Pistolet à O", "Hydrocanon", "Surf",
    "Laser Glace", "Blizzard", "Rafale Psy", "Bulles d'O", "Onde Boréale", "Ultralaser", "Picpic", "Bec Vrille", "Sacrifice", "Balayage", "Riposte", "Frappe Atlas",
    "Force", "Vol-Vie", "Méga-Sangsue", "Vampigraine", "Croissance", "Tranch'Herbe", "Lance-Soleil", "Poudre Toxik", "Para-Spore", "Poudre Dodo", "Danse Fleurs",
    "Sécrétion", "Draco-Rage", "Danse Flammes", "Éclair", "Tonnerre", "Cage-Éclair", "Fatal-Foudre", "Jet-Pierres", "Séisme", "Abîme", "Tunnel", "Toxik",
    "Choc Mental", "Psyko", "Hypnose", "Yoga", "Hâte", "Vive-attaque", "Frénésie", "Téléport", "Ténèbres", "Copie", "Grincement", "Reflet", "Soin", "Armure",
    "Lilliput", "Brouillard", "Onde Folie", "Repli", "Boul'Armure", "Bouclier", "Mur Lumière", "Buée Noire", "Protection", "Puissance", "Patience", "Métronome",
    "Mimique", "Destruction", "Bombe Oeuf", "Léchouille", "Purédpois", "Détritus", "Massd'Os", "Déflagration", "Cascade", "Claquoir", "Météores", "Coud'Krâne",
    "Picanon", "Constriction", "Amnésie", "Télékinésie", "E-Coque", "Pied Voltige", "Intimidation", "Dévorêve", "Gaz Toxik", "Pilonnage", "Vampirisme", "Grobisou",
    "Piqué", "Morphing", "Écume", "Uppercut", "Spore", "Flash", "Vague Psy", "Trempette", "Acidarmure", "Pince-Masse", "Explosion", "Combo-Griffe", "Osmerang",
    "Repos", "Éboulement", "Croc de Mort", "Affûtage", "Conversion", "Triplattaque", "Croc Fatal", "Tranche", "Clonage", "Lutte",
      
    # Gen II
    "Gribouille", "Triple Pied", "Larcin", "Toile", "Lire-Esprit", "Cauchemar", "Roue de Feu", "Ronflement", "Malédiction", "Fléau", "Conversion2", "Aéroblast",
    "Spore Coton", "Contre", "Dépit", "Poudreuse", "Abri", "Mach Punch", "Grimace", "Feinte", "Doux Baiser", "Cognobidon", "Bombe Beurk", "Coud'Boue", "Octazooka",
    "Picots", "Élecanon", "Clairvoyance", "Prlvt Destin", "Requiem", "Vent Glace", "Détection", "Charge Os", "Verrouillage", "Colère", "Tempête de Sable",
    "Giga-Sangsue", "Ténacité", "Charme", "Roulade", "Faux-Chage", "Vantardise", "Lait à Boire", "Étincelle", "Taillade", "Ailes d'Acier", "Regard Noir", "Attraction",
    "Blabla Dodo", "Glas de Soin", "Retour", "Cadeau", "Frustration", "Rune Protect", "Balance", "Feu Sacré", "Ampleur", "Dynamopoing", "Mégacorne", "Dracosouffle",
    "Relais", "Encore", "Poursuite", "Tour Rapide", "Doux Parfum", "Queue de Fer", "Griffe Acier", "Corps Perdu", "Aurore", "Synthèse", "Rayon Lune", "Puissance Cachée",
    "Coup Croix", "Ouragan", "Danse Pluie", "Zénith", "Mâchouille", "Voile Miroir", "Boost", "Vit.Extrême", "Pouv.Antique", "Ball'Ombre", "Prescience", "Éclate-Roc",
    "Siphon", "Baston",
    
    # Gen III
    "Bluff", "Brouhaha", "Stockage", "Relâche", "Avale", "Canicule", "Grêle", "Tourmente", "Flatterie", "Feu Follet", "Souvenir", "Façade", "Mitra-Poing", "Stimulant",
    "Par Ici", "Force Nature", "Chargeur", "Provoc", "Coup d'Main", "Tourmagik", "Imitation", "Voeu", "Assistance", "Racines", "Surpuissance", "Reflet Magik", "Recyclage",
    "Vendetta", "Casse-Brique", "Bâillement", "Sabotage", "Effort", "Éruption", "Échange", "Possessif", "Régénération", "Rancune", "Saisie", "Force Cachée", "Plongée",
    "Cogne", "Camouflage", "Lumi-Queue", "Lumi-Éclat", "Ball'Brume", "Danse Plumes", "Danse Folle", "Pied Brûleur", "Lance-Boue", "Ball'Glace", "Poing Dard", "Paresse",
    "Mégaphone", "Crochet Venin", "Éclate Griffe", "Rafale Feu", "Hydroblast", "Poing Météore", "Étonnement", "Ball'Météo", "Aromathérapie", "Croco Larme", "Tranch'Air",
    "Surchauffe", "Flair", "Tomberoche", "Vent Argenté", "Strido-Son", "Siffl'Herbe", "Chatouille", "Force Cosmique", "Giclédo", "Rayon Signal", "Poing Ombre",
    "Extrasenseur", "Stratopercut", "Tourbi-Sable", "Glaciation", "Ocroupi", "Balle Graine", "Aéropique", "Stalagtite", "Mur de Fer", "Barrage", "Grondement", "Draco-Griffe",
    "Végé-Attaque", "Gonflette", "Rebond", "Tir de Boue", "Queue-Poison", "Implore", "Électacle", "Feuillemagik", "Tourniquet", "Plénitude", "Lame-Feuille", "Danse Draco",
    "Boule Roc", "Onde de Choc", "Vibraqua", "Carnareket", "Psycho Boost",
    
    # Gen IV
    "Atterrissage", "Gravité", "Oeil Miracle", "Réveil Forcé", "Marto-Poing", "Gyroballe", "Voeu Soin", "Saumure", "Don Naturel", "Ruse", "Picore", "Vent Arrière",
    "Acupression", "Fulmifer", "Demi-Tour", "Close Combat", "Représailles", "Assurance", "Embargo", "Dégommage", "Échange Psy", "Atout", "Anti-Soin", "Essorage",
    "Astuce Force", "Suc Digestif", "Air Veinard", "Moi d'Abord", "Photocopie", "Permuforce", "Permugarde", "Punition", "Dernier Recours", "Soucigraine", "Coup Bas",
    "Pics Toxik", "Permucoeur", "Anneau Hydro", "Vol Magnétik", "Boutefeu", "Forte-Paume", "Aurasphère", "Poliroche", "Direct Toxik", "Vibrobscur", "Tranche-Nuit",
    "Hydroqueue", "Canon Graine", "Lame d'Air", "Plaie Croix", "Bourdon", "Draco-Choc", "Draco-Charge", "Rayon Gemme", "Vampipoing", "Onde Vide", "Exploforce", "Éco-Sphère",
    "Rapace", "Telluriforce", "Passe-Passe", "Giga Impact", "Machination", "Pisto-Poing", "Avalanche", "Éclats Glace", "Griffe Ombre", "Crocs Éclair", "Crocs Givre",
    "Crocs Feu", "Ombre Portée", "Boue-Bombe", "Coupe Psycho", "Psykoud'Boul", "Miroi-Tir", "Luminocanon", "Escalade", "Anti-Brume", "Distorsion", "Draco-Météore",
    "Coup d'Jus", "Ébullilave", "Tempête Verte", "Mégafouet", "Roc-Boulet", "Poison Croix", "Détricanon", "Tête de Fer", "Bombe Aimant", "Lame de Roc", "Séduction",
    "Piège de Roc", "Noeud Herbe", "Babil", "Jugement", "Piqûre", "Rayon Chargé", "Martobois", "Aqua-Jet", "Appel Attak", "Appel Défens", "Appel Soins", "Fracass'Tête",
    "Coup Double", "Hurle-Temps", "Spatio-Rift", "Danse Lune", "Presse", "Vortex Magma", "Trou Noir", "Fulmigraine", "Vent Mauvais", "Revenant"
]

# Dangerous moves
BELIER = MOVE_NAMES.index("Bélier")
REQUIEM = MOVE_NAMES.index("Requiem")
TELEPORT = MOVE_NAMES.index("Téléport")
HURLEMENT = MOVE_NAMES.index("Hurlement")
CYCLONE = MOVE_NAMES.index("Cyclone")
DESTRUCTION = MOVE_NAMES.index("Destruction")
EXPLOSION = MOVE_NAMES.index("Explosion")
PIED_VOLTIGE = MOVE_NAMES.index("Pied Voltige")
METRONOME = MOVE_NAMES.index("Métronome")
DANSE_FLEURS = MOVE_NAMES.index("Danse Fleurs")
MALEDICTION = MOVE_NAMES.index("Malédiction")
MARTOBOIS = MOVE_NAMES.index("Martobois")
SACRIFICE = MOVE_NAMES.index("Sacrifice")
MANIA = MOVE_NAMES.index("Mania")
DAMOCLES = MOVE_NAMES.index("Damoclès")
SOUVENIR = MOVE_NAMES.index("Souvenir")

DANGEROUS_MOVES = {
    # Kanto
	16: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49], "movesList": [[CYCLONE, 17]]}, # Roucool
	19: {"levelsLearnset": [1, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34], "movesList": [[DAMOCLES, 31]]}, # Rattata
	20: {"levelsLearnset": [1, 1, 1, 4, 7, 10, 13, 16, 19, 20, 24, 29, 34, 39, 44], "movesList": [[DAMOCLES, 39]]}, # Rattatac
	35: {"levelsLearnset": [1, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46], "movesList": [[METRONOME, 31]]}, # Mélofée
	37: {"levelsLearnset": [1, 4, 7, 11, 14, 17, 21, 24, 27, 31, 34, 37, 41, 44, 47], "movesList": [[HURLEMENT, 7]]}, # Goupix
	39: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49], "movesList": [[DAMOCLES, 49]]}, # Rondoudou
	43: {"levelsLearnset": [1, 5, 9, 13, 15, 17, 21, 25, 29, 33, 37, 41], "movesList": [[DANSE_FLEURS, 41]]}, # Mystherbe
	44: {"levelsLearnset": [1, 5, 9, 13, 15, 17, 23, 29, 35, 41, 47, 53], "movesList": [[DANSE_FLEURS, 53]]}, # Ortide
	56: {"levelsLearnset": [1, 1, 1, 1, 1, 9, 13, 17, 21, 25, 33, 37, 41, 45, 49], "movesList": [[MANIA, 41]]}, # Férosinge
	57: {"levelsLearnset": [1, 1, 1, 1, 1, 9, 13, 17, 21, 25, 28, 35, 41, 47, 53, 59], "movesList": [[MANIA, 47]]}, # Colossinge
	58: {"levelsLearnset": [1, 1, 6, 9, 14, 17, 20, 25, 28, 31, 34, 39, 42, 45, 48], "movesList": [[HURLEMENT, 1], [BELIER, 31]]}, # Caninos
	63: {"levelsLearnset": [1], "movesList": [[TELEPORT, 1]]}, # Abra
	64: {"levelsLearnset": [0, 1, 16, 18, 22, 24, 28, 30, 34, 36, 40, 42, 46], "movesList": [[TELEPORT, 1]]}, # Kadabra
	66: {"levelsLearnset": [1, 1, 7, 10, 13, 19, 22, 25, 31, 34, 37, 43, 46], "movesList": [[SACRIFICE, 31]]}, # Machoc
	67: {"levelsLearnset": [1, 1, 7, 10, 13, 19, 22, 25, 32, 36, 40, 44, 51], "movesList": [[SACRIFICE, 32]]}, # Machopeur
	74: {"levelsLearnset": [1, 1, 4, 8, 11, 15, 18, 22, 25, 29, 32, 36, 39], "movesList": [[DESTRUCTION, 18], [EXPLOSION, 32], [DAMOCLES, 36]]}, # Racaillou
	75: {"levelsLearnset": [1, 1, 4, 8, 11, 15, 18, 22, 27, 33, 38, 44, 49], "movesList": [[DESTRUCTION, 18], [EXPLOSION, 38], [DAMOCLES, 44]]}, # Gravalanch
	77: {"levelsLearnset": [1, 1, 6, 10, 15, 19, 24, 28, 33, 37, 42, 46], "movesList": [[BELIER, 28]]}, # Ponyta
	86: {"levelsLearnset": [1, 3, 7, 11, 13, 17, 21, 23, 27, 31, 33, 37, 41, 43, 47, 51], "movesList": [[BELIER, 37]]}, # Otaria
	87: {"levelsLearnset": [1, 1, 1, 1, 13, 17, 21, 23, 27, 31, 33, 34, 37, 41, 43, 47, 51], "movesList": [[BELIER, 37]]}, # Lamantine
	88: {"levelsLearnset": [1, 1, 4, 7, 12, 17, 20, 23, 28, 33, 36, 39, 44, 49], "movesList": [[SOUVENIR, 49]]}, # Tadmorv
	92: {"levelsLearnset": [1, 1, 5, 8, 12, 15, 19, 22, 26, 29, 33, 36, 40, 43], "movesList": [[MALEDICTION, 12]]}, # Fantominus
	93: {"levelsLearnset": [1, 1, 5, 8, 12, 15, 19, 22, 25, 28, 33, 39, 44, 50, 55], "movesList": [[MALEDICTION, 12]]}, # Spectrum
	94: {"levelsLearnset": [1, 1, 5, 8, 12, 15, 19, 22, 25, 28, 33, 39, 44, 50, 55], "movesList": [[MALEDICTION, 12]]}, # Ectoplasma
	95: {"levelsLearnset": [1, 1, 1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 54], "movesList": [[DAMOCLES, 49]]}, # Onix
	100: {"levelsLearnset": [1, 5, 8, 12, 15, 19, 22, 26, 29, 33, 36, 40, 43, 47], "movesList": [[DESTRUCTION, 29], [EXPLOSION, 43]]}, # Voltorbe
	104: {"levelsLearnset": [1, 3, 7, 11, 13, 17, 21, 23, 27, 31, 33, 37, 41, 43], "movesList": [[MANIA, 31], [DAMOCLES, 43]]}, # Osselait
	109: {"levelsLearnset": [1, 1, 6, 10, 15, 19, 24, 28, 33, 37, 42, 46, 51], "movesList": [[DESTRUCTION, 19], [EXPLOSION, 37], [SOUVENIR, 51]]}, # Smogo
	110: {"levelsLearnset": [1, 1, 6, 10, 15, 19, 24, 28, 33, 40, 48, 55, 63], "movesList": [[DESTRUCTION, 19], [EXPLOSION, 40], [SOUVENIR, 63]]}, # Smogogo
	111: {"levelsLearnset": [1, 1, 9, 13, 21, 25, 33, 37, 45, 49, 57], "movesList": [[BELIER, 33]]}, # Rhinocorne
	112: {"levelsLearnset": [1, 1, 1, 1, 21, 25, 33, 37, 42, 45, 49, 57], "movesList": [[BELIER, 33]]}, # Rhinoféros
	113: {"levelsLearnset": [1, 1, 5, 9, 12, 16, 20, 23, 27, 31, 34, 38, 42, 46], "movesList": [[DAMOCLES, 46]]}, # Leveinard
	124: {"levelsLearnset": [1, 1, 1, 1, 5, 8, 11, 15, 18, 21, 25, 28, 33, 39, 44, 49, 55], "movesList": [[REQUIEM, 49]]}, # Lippoutou
	127: {"levelsLearnset": [1, 1, 4, 8, 13, 18, 21, 25, 30, 35, 38, 42, 47, 52], "movesList": [[MANIA, 35], [SACRIFICE, 42]]}, # Scarabrute
	128: {"levelsLearnset": [1, 3, 5, 8, 11, 15, 19, 24, 29, 35, 41, 48, 55], "movesList": [[BELIER, 35], [MANIA, 48]]}, # Tauros
	130: {"levelsLearnset": [1, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47], "movesList": [[MANIA, 1]]}, # Léviator
	131: {"levelsLearnset": [1, 1, 1, 4, 7, 10, 14, 18, 22, 27, 32, 37, 43, 49, 55], "movesList": [[REQUIEM, 27]]}, # Lokhlass
	133: {"levelsLearnset": [1, 1, 1, 8, 15, 22, 29, 36, 43, 50, 57], "movesList": [[BELIER, 43]]}, # Évoli

    # Johto
	163: {"levelsLearnset": [1, 1, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49], "movesList": [[BELIER, 25]]}, # Hoothoot
	164: {"levelsLearnset": [1, 1, 1, 1, 5, 9, 13, 17, 22, 27, 32, 37, 42, 47, 52, 57], "movesList": [[BELIER, 27]]}, # Noarfang
	166: {"levelsLearnset": [1, 6, 9, 14, 14, 14, 17, 24, 29, 36, 41, 48, 53], "movesList": [[DAMOCLES, 48]]}, # Coxyclaque
	170: {"levelsLearnset": [1, 1, 6, 9, 12, 17, 20, 23, 28, 31, 34, 39, 42, 45], "movesList": [[BELIER, 23]]}, # Loupio
	171: {"levelsLearnset": [1, 1, 1, 6, 9, 12, 17, 20, 23, 27, 27, 27, 30, 35, 40, 47, 52, 57], "movesList": [[BELIER, 23]]}, # Lanturn
	175: {"levelsLearnset": [1, 1, 6, 10, 15, 19, 24, 28, 33, 37, 42, 46, 51], "movesList": [[METRONOME, 6], [DAMOCLES, 46]]}, # Togepi
	177: {"levelsLearnset": [1, 1, 6, 9, 12, 17, 20, 23, 28, 33, 36, 39, 44, 44, 47], "movesList": [[TELEPORT, 9]]}, # Natu
	183: {"levelsLearnset": [1, 2, 7, 10, 15, 18, 23, 27, 32, 37, 42], "movesList": [[DAMOCLES, 27]]}, # Marill
	184: {"levelsLearnset": [1, 2, 7, 10, 15, 20, 27, 33, 40, 47, 54], "movesList": [[DAMOCLES, 33]]}, # Azumarill
	185: {"levelsLearnset": [1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49], "movesList": [[MARTOBOIS, 1], [DAMOCLES, 46]]}, # Simularbre
	187: {"levelsLearnset": [1, 4, 7, 10, 12, 14, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43], "movesList": [[SOUVENIR, 43]]}, # Granivol
	188: {"levelsLearnset": [1, 4, 7, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52], "movesList": [[SOUVENIR, 52]]}, # Floravol
	200: {"levelsLearnset": [1, 1, 5, 10, 14, 19, 23, 28, 32, 37, 41, 46], "movesList": [[REQUIEM, 41]]}, # Feuforêve
	204: {"levelsLearnset": [1, 1, 6, 9, 12, 17, 20, 23, 28, 31, 34, 39, 42, 45], "movesList": [[DESTRUCTION, 6], [BELIER, 12], [EXPLOSION, 34], [DAMOCLES, 45]]}, # Pomdepik
	206: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53], "movesList": [[BELIER, 37]]}, # Insolourdo
	208: {"levelsLearnset": [1, 1, 1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 54], "movesList": [[DAMOCLES, 49]]}, # Steelix
	209: {"levelsLearnset": [1, 1, 1, 1, 7, 13, 19, 25, 31, 37, 43, 49], "movesList": [[HURLEMENT, 25], [BELIER, 37]]}, # Snubbull
	211: {"levelsLearnset": [1, 1, 1, 9, 9, 13, 17, 21, 25, 25, 29, 33, 37, 41, 45, 49, 53, 57], "movesList": [[BELIER, 41]]}, # Qwilfish
	214: {"levelsLearnset": [1, 1, 1, 1, 7, 13, 19, 25, 31, 37, 43, 49, 55], "movesList": [[BELIER, 31]]}, # Scarhino
	216: {"levelsLearnset": [1, 1, 1, 1, 1, 8, 15, 22, 29, 36, 43, 43, 50, 57], "movesList": [[MANIA, 50]]}, # Teddiursa
	217: {"levelsLearnset": [1, 1, 1, 1, 1, 8, 15, 22, 29, 38, 47, 49, 58, 67], "movesList": [[MANIA, 58]]}, # Ursaring
	220: {"levelsLearnset": [1, 1, 4, 8, 13, 16, 20, 25, 28, 32, 37, 40, 44, 49], "movesList": [[BELIER, 32]]}, # Marcacrin
	221: {"levelsLearnset": [1, 1, 1, 1, 4, 8, 13, 16, 20, 25, 28, 32, 33, 40, 48, 56, 65], "movesList": [[BELIER, 32]]}, # Cochignon
	228: {"levelsLearnset": [1, 1, 4, 9, 14, 17, 22, 27, 30, 35, 40, 43, 48, 53], "movesList": [[HURLEMENT, 14]]}, # Malosse
	229: {"levelsLearnset": [1, 1, 4, 9, 14, 17, 22, 28, 32, 38, 44, 48, 54, 60], "movesList": [[HURLEMENT, 14]]}, # Démolosse
	231: {"levelsLearnset": [1, 1, 1, 1, 6, 10, 15, 19, 24, 28, 33, 37, 42], "movesList": [[BELIER, 10], [DAMOCLES, 42]]}, # Phanpy
	234: {"levelsLearnset": [1, 3, 7, 10, 13, 16, 21, 23, 27, 33, 38, 43, 49, 53], "movesList": [[BELIER, 21]]}, # Cerfrousse
	238: {"levelsLearnset": [1, 5, 8, 11, 15, 18, 21, 25, 28, 31, 35, 38, 41, 45], "movesList": [[REQUIEM, 41]]}, # Lippouti
	246: {"levelsLearnset": [1, 1, 5, 10, 14, 19, 23, 28, 32, 37, 41, 46, 50], "movesList": [[MANIA, 23]]}, # Embrylex

    # Hoenn
	261: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53], "movesList": [[HURLEMENT, 21], [BELIER, 45]]}, # Medhyèna
	262: {"levelsLearnset": [1, 1, 1, 1, 5, 9, 13, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62], "movesList": [[HURLEMENT, 22], [BELIER, 52]]}, # Grahyèna
	267: {"levelsLearnset": [1, 13, 17, 20, 24, 27, 31, 34, 38, 41], "movesList": [[CYCLONE, 27]]}, # Charmillon
	269: {"levelsLearnset": [1, 13, 17, 20, 24, 27, 31, 34, 38, 41], "movesList": [[CYCLONE, 27]]}, # Papinox
	273: {"levelsLearnset": [1, 3, 7, 13, 21, 31, 43], "movesList": [[EXPLOSION, 43]]}, # Grainipiot
	280: {"levelsLearnset": [1, 6, 10, 12, 17, 21, 23, 28, 32, 34, 39, 43, 45], "movesList": [[TELEPORT, 12]]}, # Tarsal
	281: {"levelsLearnset": [1, 6, 10, 12, 17, 22, 25, 31, 36, 39, 45, 50, 53], "movesList": [[TELEPORT, 12]]}, # Kirlia
	284: {"levelsLearnset": [1, 1, 7, 13, 19, 22, 26, 33, 40, 47, 54, 61], "movesList": [[CYCLONE, 54]]}, # Maskadra
	294: {"levelsLearnset": [1, 5, 11, 15, 20, 23, 29, 37, 43, 51, 51, 57], "movesList": [[HURLEMENT, 43]]}, # Ramboum
	296: {"levelsLearnset": [1, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43], "movesList": [[CYCLONE, 16]]}, # Makuhita
	300: {"levelsLearnset": [1, 1, 1, 1, 4, 8, 11, 15, 18, 22, 25, 29, 32, 36, 39, 42, 46], "movesList": [[DAMOCLES, 42]]}, # Skitty
	304: {"levelsLearnset": [1, 4, 8, 11, 15, 18, 22, 25, 29, 32, 36, 39, 43, 46], "movesList": [[HURLEMENT, 22], [BELIER, 25], [DAMOCLES, 43]]}, # Galekid
	307: {"levelsLearnset": [1, 4, 8, 11, 15, 18, 22, 25, 29, 32, 36, 39, 43, 46], "movesList": [[PIED_VOLTIGE, 32]]}, # Méditikka
	308: {"levelsLearnset": [1, 4, 8, 11, 15, 18, 22, 25, 29, 32, 36, 42, 49, 55], "movesList": [[PIED_VOLTIGE, 32]]}, # Charmina
	309: {"levelsLearnset": [1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 41, 44, 49], "movesList": [[HURLEMENT, 36]]}, # Dynavolt
	313: {"levelsLearnset": [1, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45], "movesList": [[DAMOCLES, 45]]}, # Muciole
	315: {"levelsLearnset": [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46], "movesList": [[DANSE_FLEURS, 40]]}, # Rosélia
	318: {"levelsLearnset": [1, 1, 6, 8, 11, 16, 18, 21, 26, 28, 31, 36, 38], "movesList": [[BELIER, 38]]}, # Carvanha
	322: {"levelsLearnset": [1, 1, 5, 11, 15, 21, 25, 31, 35, 41, 45, 51], "movesList": [[BELIER, 21], [DAMOCLES, 51]]}, # Chamallot
	323: {"levelsLearnset": [1, 1, 1, 1, 5, 11, 15, 21, 25, 31, 33, 39, 49, 57, 67], "movesList": [[BELIER, 21]]}, # Camérupt
	327: {"levelsLearnset": [1, 5, 10, 14, 19, 23, 28, 32, 37, 41, 46, 50, 55], "movesList": [[DAMOCLES, 46], [MANIA, 55]]}, # Spinda
	333: {"levelsLearnset": [1, 1, 5, 9, 13, 18, 23, 28, 32, 36, 40, 45, 50], "movesList": [[BELIER, 28], [REQUIEM, 50]]}, # Tylton
	337: {"levelsLearnset": [1, 1, 1, 9, 12, 20, 23, 31, 34, 42, 45, 53, 56], "movesList": [[EXPLOSION, 56]]}, # Séléroc
	338: {"levelsLearnset": [1, 1, 1, 9, 12, 20, 23, 31, 34, 42, 45, 53, 56], "movesList": [[EXPLOSION, 56]]}, # Solaroc
	343: {"levelsLearnset": [1, 3, 5, 7, 11, 15, 19, 25, 31, 37, 45, 53, 61, 71], "movesList": [[DESTRUCTION, 19], [EXPLOSION, 71]]}, # Balbuto
	354: {"levelsLearnset": [1, 5, 8, 13, 16, 20, 23, 28, 31, 35, 42, 51, 58, 66], "movesList": [[MALEDICTION, 13]]}, # Branette
	355: {"levelsLearnset": [1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46], "movesList": [[MALEDICTION, 30]]}, # Skelénox
	356: {"levelsLearnset": [1, 1, 1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 37, 43, 51, 61], "movesList": [[MALEDICTION, 30]]}, # Téraclope
	357: {"levelsLearnset": [1, 1, 7, 11, 17, 21, 27, 31, 37, 41, 47, 51, 57, 61], "movesList": [[CYCLONE, 27]]}, # Tropius
	358: {"levelsLearnset": [1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49], "movesList": [[BELIER, 22], [DAMOCLES, 33]]}, # Éoko
	359: {"levelsLearnset": [1, 1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 41, 44, 49, 52, 57, 60, 65], "movesList": [[REQUIEM, 65]]}, # Absol
	369: {"levelsLearnset": [1, 1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78], "movesList": [[BELIER, 29], [DAMOCLES, 50]]}, # Relicanth
	370: {"levelsLearnset": [1, 4, 7, 9, 14, 17, 22, 27, 31, 37, 40, 46, 51], "movesList": [[BELIER, 14]]}, # Lovdisc
	371: {"levelsLearnset": [1, 5, 10, 16, 20, 25, 31, 35, 40, 46, 50, 55], "movesList": [[DAMOCLES, 55]]}, # Draby
	374: {"levelsLearnset": [1], "movesList": [[BELIER, 1]]}, # Terhal

    # Sinnoh
	396: {"levelsLearnset": [1, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37], "movesList": [[CYCLONE, 21], [BELIER, 29]]}, # Étourmi
	397: {"levelsLearnset": [1, 1, 1, 5, 9, 13, 18, 23, 28, 33, 38, 43], "movesList": [[CYCLONE, 23], [BELIER, 33]]}, # Étourvol
	399: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45], "movesList": [[BELIER, 33]]}, # Keunotor
	400: {"levelsLearnset": [1, 1, 5, 9, 13, 15, 18, 23, 28, 33, 38, 43, 48, 53], "movesList": [[BELIER, 38]]}, # Castorno
	402: {"levelsLearnset": [1, 1, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50], "movesList": [[REQUIEM, 50]]}, # Mélokrik
	403: {"levelsLearnset": [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41], "movesList": [[HURLEMENT, 21]]}, # Lixy
	404: {"levelsLearnset": [1, 5, 9, 13, 18, 23, 28, 33, 38, 43, 48], "movesList": [[HURLEMENT, 23]]}, # Luxio
	420: {"levelsLearnset": [1, 7, 10, 13, 19, 22, 28, 31, 37, 40], "movesList": [[BELIER, 31]]}, # Ceribou
	425: {"levelsLearnset": [1, 1, 6, 11, 14, 17, 22, 27, 27, 30, 33, 38, 43], "movesList": [[EXPLOSION, 43]]}, # Baudrive
	434: {"levelsLearnset": [1, 1, 4, 7, 11, 15, 20, 25, 31, 37, 44], "movesList": [[SOUVENIR, 37], [EXPLOSION, 44]]}, # Moufouette
	435: {"levelsLearnset": [1, 1, 4, 7, 11, 15, 20, 25, 31, 34, 41, 52], "movesList": [[SOUVENIR, 41], [EXPLOSION, 52]]}, # Moufflair
	438: {"levelsLearnset": [1, 1, 6, 9, 14, 17, 22, 25, 30, 33, 38, 41, 46], "movesList": [[DAMOCLES, 46]]}, # Manzaï
	442: {"levelsLearnset": [0, 0, 0, 0, 1, 7, 13, 19, 25, 31, 37, 43, 49], "movesList": [[MALEDICTION, 1], [SOUVENIR, 43]]}, # Spiritomb
	443: {"levelsLearnset": [1, 3, 7, 13, 15, 19, 25, 27, 31, 37], "movesList": [[BELIER, 15]]}, # Griknot
	444: {"levelsLearnset": [1, 1, 3, 7, 13, 15, 19, 28, 33, 40, 49], "movesList": [[BELIER, 15]]}, # Carmache
	446: {"levelsLearnset": [0, 0, 1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 41, 44, 49], "movesList": [[METRONOME, 1]]}, # Goinfrex
	449: {"levelsLearnset": [1, 1, 7, 13, 19, 25, 31, 37, 44, 50], "movesList": [[BELIER, 19], [DAMOCLES, 44]]}, # Hippopotas
	450: {"levelsLearnset": [1, 1, 1, 1, 7, 13, 19, 25, 31, 40, 50, 60], "movesList": [[BELIER, 19], [DAMOCLES, 50]]}, # Hippodocus
	458: {"levelsLearnset": [1, 1, 4, 10, 13, 19, 22, 28, 31, 37, 40, 46, 49], "movesList": [[BELIER, 31]]}, # Babimanta
	459: {"levelsLearnset": [1, 1, 5, 9, 13, 17, 21, 26, 31, 36, 41, 46], "movesList": [[MARTOBOIS, 36]]}, # Blizzi
	460: {"levelsLearnset": [1, 1, 1, 5, 9, 13, 17, 21, 26, 31, 36, 47, 58], "movesList": [[MARTOBOIS, 36]]}, # Blizzaroi
	480: {"levelsLearnset": [1, 1, 6, 16, 21, 31, 36, 46, 51, 61, 66, 76], "movesList": [[SOUVENIR, 76]]}, # Créhelf
	482: {"levelsLearnset": [1, 1, 6, 16, 21, 31, 36, 46, 51, 61, 66, 76], "movesList": [[EXPLOSION, 76]]}, # Créfadet
}