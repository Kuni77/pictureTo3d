# pictureTo3d

# Ce Projet a pour but de generer une forme 3d à partir d'une photo

Python comme langage principal (avec des bibliothèques comme OpenCV, PyTorch)
Blender pour le traitement 3D (via son API Python)
Frameworks de reconstruction 3D comme COLMAP ou OpenMVG

Étapes principales du projet :

Capture et traitement d'image

OpenCV pour la capture
Détection des points clés du visage avec dlib ou MediaPipe


Reconstruction 3D

Utiliser des modèles pré-entraînés comme SMPL pour le corps
PIFuHD ou similaire pour la reconstruction 3D depuis une seule image
Adaptation du maillage 3D selon la morphologie


Texturing et rendu

UV mapping du visage
Application des textures extraites de la photo
Rendu final avec Blender


Défis principaux :

Précision de la reconstruction 3D à partir d'une seule image
Qualité du mapping des textures
Performance et optimisation
Gestion des différentes morphologies
