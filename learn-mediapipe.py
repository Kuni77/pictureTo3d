import cv2
import mediapipe as mp

# Initialisation de MediaPipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh()

try:
    # Capture une image avec la webcam
    cap = cv2.VideoCapture(0)
    ret, image = cap.read()
    
    if not ret:
        raise Exception("Échec de la capture")

    # Convertit l'image en RGB (MediaPipe utilise RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Détecte les points du visage
    results = face_mesh.process(image_rgb)
    
    # Si des visages sont détectés
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Dessine les points sur le visage
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(
                    color=(0, 255, 0), thickness=1, circle_radius=1
                )
            )
    
    # Sauvegarde l'image avec les points détectés
    cv2.imwrite('visage_detecte.jpg', image)
    print("Image sauvegardée avec les points du visage")

except Exception as e:
    print(f"Une erreur est survenue : {e}")

finally:
    # Libère la caméra
    cap.release()
    # Libère les ressources
    face_mesh.close()