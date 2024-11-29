# Final Python Project 🎯

## Table of Contents 📚

1. [Project Description](#project-description)
2. [Requirements](#requirements)
   - 1. Requirements
   - 2. Directory Structure
3. [Run the Application](#6-run-the-application)

## Project Description 📝
Le jeu de la Vie de Conway est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. Le jeu se déroule sur une grille à deux dimensions comportant un nombre n * n de cellules. Chaque cellule est soit vivante, soit morte et possède 8 cellules voisines.

À chaque tour, le jeu se passe comme il suit :
- Si la cellule a exactement 3 voisines vivantes, elle devient vivante au
tour suivant
- Si la cellule a exactement 2 voisines vivantes, son état ne change pas
au tour suivant (mort = mort, vivant = vivant)
- Autrement, la cellule meurt au tour suivant
Pour passer au tour suivant, l’utilisateur doit appuyer sur Entrée, ou bien sur
Q ce qui aura pour effet de sauvegarder la grille et de fermer le programme 

**Technologies used:**
- Python3
- Python

## Requirements ⚙️

### 1. Python ou Python3
- Ensure you have Python or Python3 installed on your machine. You can download it from the official website (https://www.python.org/downloads/).
- You can check if it's installed and see the version by running the following command in your terminal:
    ```bash
    python3 -V
    ```
    ```bash
    python -V
    ```

### 2. Directory Structure 🗂️
- Ensure your project has a proper directory structure. You should have something like this:
    ```bash
    Game_of_life/ 
        ├── .gitignore
        ├── grid.py
        ├── main.py
        ├── prompt.py
        ├── README.md
        ├── save.py 
        └── variables.py
    ```

## Run The Application 🚀
- To start your game, navigate to the Game_of_life directory and tap:
    ```bash
    python3 main.py
    ```
    ```bash 
    python main.py
    ```
- You should see:
    ```
   Welcome to the Game of Life !

    This is an auto generate game.

    Load the previous grid, y/n: 
    ```