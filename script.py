import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Fonction pour déplacer les fichiers dans les bons dossiers
def move_files(folder):
    # Types de fichiers et leurs extensions associées
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Vidéos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Musique": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Autres": []
    }

    # Parcours des fichiers dans le dossier sélectionné
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Vérifier si c'est un fichier
        if os.path.isfile(file_path):
            moved = False
            # Déplacer les fichiers dans les bons dossiers
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination = os.path.join(folder, category, filename)
                    if not os.path.exists(os.path.join(folder, category)):
                        os.makedirs(os.path.join(folder, category))  # Créer le dossier s'il n'existe pas
                    shutil.move(file_path, destination)
                    moved = True
                    break
            # Si le fichier n'a pas été déplacé, le mettre dans "Autres"
            if not moved:
                if not os.path.exists(os.path.join(folder, "Autres")):
                    os.makedirs(os.path.join(folder, "Autres"))  # Créer le dossier "Autres" s'il n'existe pas
                shutil.move(file_path, os.path.join(folder, "Autres", filename))

    messagebox.showinfo("Succès", "Le dossier a été organisé avec succès !")

# Fonction pour sélectionner le dossier
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        move_files(folder_path)

# Création de l'interface graphique avec un design moderne et épuré
root = tk.Tk()  # Utilisation de Tk pour créer la fenêtre principale
root.title("Organisateur de Téléchargements")
root.geometry("500x300")
root.config(bg="#f0f0f0")  # Couleur de fond claire et moderne

# Titre de la fenêtre avec une police moderne et épurée
title_label = tk.Label(root, text="Organiser vos Téléchargements", font=("Helvetica Neue", 18, "bold"), fg="#333", bg="#f0f0f0")
title_label.pack(pady=20)

# Description courte et subtile
desc_label = tk.Label(root, text="Sélectionnez votre dossier de téléchargement et laissez l'application faire le travail.", font=("Helvetica Neue", 10), fg="#666", bg="#f0f0f0")
desc_label.pack(pady=5)

# Création du bouton épuré avec animation et design minimaliste
organize_button = ttk.Button(
    root, 
    text="Organiser", 
    command=select_folder, 
    width=20, 
    padding=15,
    style="TButton"
)
organize_button.pack(pady=30)

# Personnalisation du style du bouton avec effets modernes
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica Neue", 14),
                background="#4CAF50",
                foreground="white",
                relief="flat",
                borderwidth=0,
                padding=10)
style.map("TButton", background=[("active", "#45a049"), ("pressed", "#388e3c")])

# Ombres et effets subtils
organize_button.config(width=20)

# Ajout d'un pied de page moderne avec le copyright
footer_label = tk.Label(root, text="© 2024 Taysir Software", font=("Helvetica Neue", 8), fg="#999", bg="#f0f0f0")
footer_label.pack(side="bottom", pady=20)

# Lancer l'interface graphique
root.mainloop()
