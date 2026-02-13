---

# Aetherfall

Ce projet est une démonstration technique d'un jeu de rôle (RPG) textuel développé en Python, mettant l'accent sur l'application rigoureuse des **Design Patterns** pour créer un système évolutif, découplé et structuré.

## Le Scénario

Le joueur incarne un héros qui commence son périple au **Village**. Après avoir activé une quête auprès d'un PNJ, il doit explorer la **Forêt** pour trouver la **Clé du Donjon**. Une fois la clé obtenue, il peut accéder au **Donjon** pour affronter le **Gardien du Donjon**, un boss redoutable possédant plusieurs phases de combat.

---

## Architecture & Design Patterns

Le projet utilise une combinaison de patterns pour gérer chaque aspect du gameplay :

### 1. Exploration & Monde (Strategy & Factory)

* **Strategy** : Chaque zone (**Village**, **Forêt**, **Donjon**) possède sa propre logique de génération d'événements (probabilités de combat, coffres, dialogues).
* **Factory** : Un `EvenementFactory` centralise la création des objets (Combat, Marchand, PNJ) pour éviter de dupliquer la logique d'instanciation.

### 2. Système de Quête & Inventaire (Observer)

* **Observer** : L'inventaire agit comme un **Sujet**. Lorsqu'un objet comme la "Clé du Donjon" est ajouté, il notifie automatiquement des **Observateurs** (comme la porte du Donjon) pour débloquer de nouvelles zones sans lier directement les classes.

### 3. Entités & Boss (State & Template Method)

* **State** : Le Boss (**Gardien du Donjon**) change de comportement dynamiquement. En dessous de 50% de PV, il passe de la `Phase1` à la `Phase2`, augmentant ses dégâts et changeant ses descriptions d'attaque.
* **Interface Ennemi** : Utilise une classe abstraite pour garantir que tous les monstres possèdent une méthode `attaquer()`.

### 4. Orchestration (Facade)

* **Facade (`Pas encore finalisée`)** : La classe principale qui sert d'interface unique. Elle initialise le système, gère la création du personnage, la boucle de jeu et les transitions entre les zones. Elle cache la complexité des patterns sous des méthodes simples comme `se_deplacer()`.

---

## Fonctionnalités

* **Progression Narrative** : Un booléen dans la `Village` permet de forcer le dialogue du PNJ avant d'autoriser l'accès au marchand.
* **Système de Combat** : Gestion des dégâts et des points de vie.
* **Exploration Aléatoire** : On aimerait que La forêt génère des rencontres basées sur des probabilités.
* **Persistance** :  A faire ! : Structure pour l'implémentation d'une sauvegarde de l'état du personnage et de la quête.

---

## Installation & Lancement

1. **Cloner le dépôt** :
```bash
git clone https://github.com/votre-compte/rpg-design-patterns.git

```

2. **Lancer le jeu** :
```bash
python main.py

```

---

## Équipe

* **Maïssaâ Hachi** 
* **Jovick Tchakala** 
---
