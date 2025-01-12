import cv2

try:
    # Initialise la caméra
    cap = cv2.VideoCapture(0)
    # Initialise la capture vidéo
    # Le '0' indique la première caméra connectée (généralement la webcam intégrée)
    # Si vous avez plusieurs caméras, vous pouvez utiliser 1, 2, etc.
    
    # Vérifie si la caméra est ouverte correctement
    if not cap.isOpened():
        raise Exception("Impossible d'ouvrir la caméra")
    
    # Capture une image
    ret, frame = cap.read()
    # cap.read() capture une image de la caméra
    # ret : booléen qui indique si la capture a réussi (True) ou échoué (False)
    # frame : l'image capturée sous forme de tableau numpy
    
    # Vérifie si la capture a réussi
    if ret:
        # Sauvegarde l'image
        cv2.imwrite('photo.jpg', frame)
        # Sauvegarde l'image capturée
        # 'photo.jpg' est le nom du fichier où l'image sera sauvegardée
        # frame est l'image à sauvegarder
        print("Photo sauvegardée avec succès")
    else:
        print("Échec de la capture")
        
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    
finally:
    # Libère la caméra
    cap.release()