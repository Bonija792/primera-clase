meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
if word in meme_dict.keys():
    print ("esa palabra significa lo siguiente", (meme_dict[word]))
    
else:
    print ("actualmente esta palabra no se encuentra en nuestro registro, si necesitas otra palabra estamos para ayudarte, recuerda que debe ser en mayusculas")
