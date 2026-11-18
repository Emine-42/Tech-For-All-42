# 🚀 42 Tech For All — Chasse au Trésor & Atelier Peer-Learning

> **Atelier d'initiation immersif de 1h30 à 2h** conçu pour faire vivre la pédagogie unique de l'**École 42** à des lycéens (ou collégiens) : autonomie totale, apprentissage par la pratique et entraide *peer-to-peer* (sans professeurs ni cours magistraux).

---

## ⚡ Guide Rapide de Démarrage (Pour l'Animateur / Admin)

Vous organisez l'atelier dans une salle ? Voici comment tout lancer en **3 étapes chrono** :

### Étape 1 : Préparer les postes des élèves
Sur chaque machine élève (ou via un script de déploiement de salle / image système clone) :
```bash
git clone git@github.com:Emine-42/Tech-For-All-42.git
cd Tech-For-All-42
./setup_mission.sh
```
*(Cela crée automatiquement le dossier `~/Bureau/mission_42` sur le bureau avec l'arborescence complète d'archives, les anecdotes historiques 42, les leurres et la moulinette).*

> 💡 **Apparition dynamique des scripts** : Initialement, `decrypt.py` et `slot_machine.py` ne sont **pas** visibles. `decrypt.py` apparaît automatiquement dès que le Niveau 2 est validé, et `slot_machine.py` apparaît dès que le Niveau 3 est validé !

### Étape 2 : Lancer le serveur sur la machine de l'animateur
Sur votre poste organisateur (connecté au même réseau local Wi-Fi ou Ethernet que les élèves) :
```bash
python3 server.py 8000
```
Le serveur multithreadé détecte automatiquement votre IP locale et affiche :
```text
===========================================================================
  🚀 SERVEUR DE L'ATELIER 42 EN LIGNE (MULTITHREADÉ) !
===========================================================================

  📡 Lien à donner aux ÉLÈVES dans la salle :
     👉  http://10.80.212.27:8000/

  🛡️ Panneau Organisateur (Admin) :
     👉  http://localhost:8000/admin

  ⚙️ Mode d'atelier actif : 🎓 LYCÉE (Intermédiaire)
     (Tapez 'm' + Entrée dans ce terminal pour basculer en direct !)
===========================================================================
```

### Étape 3 : Donner le lien aux élèves
Les élèves ouvrent simplement leur navigateur web (Chrome ou Firefox) et se rendent sur l'adresse IP affichée (ex: `http://10.80.212.27:8000/`). **L'atelier commence !**

---

## 🎮 Gestion du Niveau de Difficulté (Contrôle Admin Centralisé)

Le serveur central contrôle le niveau d'accompagnement pour **toute la salle en temps réel**. Les élèves ne peuvent pas modifier le mode eux-mêmes.

| Mode | Public Cible | Caractéristiques |
| :--- | :--- | :--- |
| **🎓 Mode Lycée (Intermédiaire)**<br>*(Par défaut)* | Lycéens (STD, Général, Pro) | **Esprit 42 pur** : Aucun bouton d'indice. Les élèves doivent s'entraider entre pairs et chercher par eux-mêmes. Pas de notion de score, focus sur les 5 étoiles et le chrono. |
| **🎒 Mode Collège (Facile)** | Collégiens / Débutants complets | **Accompagné & Équilibré** :<br>• **Indice 1 (-50 pts)** : Double les chances sans donner la réponse directe (chemin exact, syntaxe, élimination des leurres).<br>• **Indice 2 (0 pt)** : 100% de chances de réussir (solution/code direct).<br>Jauge de score globale sur 500 points. |

### 3 façons de changer le mode pour toute la salle :
1. **Dans le terminal de l'animateur** : Tapez simplement `m` puis `Entrée` dans la console de `server.py`.
2. **Sur votre navigateur hôte ([http://localhost:8000/](http://localhost:8000/))** : Un bouton **`⚙️ Admin`** apparaît dans l'en-tête (visible uniquement sur votre machine).
3. **Sur le tableau de bord web** : Rendez-vous sur [http://localhost:8000/admin](http://localhost:8000/admin).

> ⚡ **Mise à jour instantanée et sans blocage** : Le serveur utilise `ThreadingHTTPServer`. Le passage en Mode Collège ou Lycée s'effectue en temps réel sans ralentissement ni freeze de page.

---

## 🔑 Aide-Mémoire des 5 Épreuves & Solutions (Confidentiel Mentor)

Ce tableau récapitule les 5 étoiles de la mission, où se trouvent les solutions et comment chaque épreuve est validée :

| Étoile | Thématique | Ce que fait l'élève | Clé Secrète à Valider | Où elle se trouve |
| :---: | :--- | :--- | :--- | :--- |
| **⭐ 1** | **Terminal Linux & Bash** | Navigue dans le dossier `mission_42/archives/` avec `ls -la` et `cd` pour trouver le fichier d'accès système caché parmi les 25 faux fichiers et anecdotes 42. | `BASH-EXPLORER-42` | Dans `mission_42/archives/2023/configs/.htaccess` (affiché avec `cat`). |
| **⭐⭐ 2** | **Inspection Web (DevTools)** | Ouvre la page web `station.html` débloquée et utilise l'inspecteur d'éléments (`F12`) pour trouver le jeton au format `W***-INS*****-*2` sans tomber dans les clés leurres. | `WEB-INSPECTOR-42` | Dans le champ caché `<input type="hidden" id="auth_token">` du formulaire de `station.html`. |
| **⭐⭐⭐ 3** | **Cryptanalyse Python** | Complète le script à trous `decrypt.py` (qui vient d'apparaître) pour tester par force brute les 26 décalages d'un Chiffre de César. | `42_MACHINE_A_SOUS` | Résultat de la **Clé 03** affiché dans le terminal de l'élève en exécutant `python3 decrypt.py`. |
| **⭐⭐⭐⭐ 4** | **Logique & Moulinette** | Implémente les conditions `if / elif / else` de `slot_machine.py` (qui vient d'apparaître) et fait certifier son code par la Moulinette 42 officielle. | `CASINO-42-JACKPOT` | Code délivré dans le terminal par la commande `python3 moulinette.py` lorsque le jeu est fonctionnel. |
| **⭐⭐⭐⭐⭐ 5** | **Peer-Learning & Mentor** | Aide une autre équipe bloquée dans la salle **sans jamais toucher à leur clavier**, puis appelle un mentor. | `MENTOR42` | **Mot de passe physique** que le Mentor tape en personne sur le poste de l'élève après avoir validé l'entraide. |

---

## 📜 Le Protocole du Niveau 5 (Peer-Learning)

À 42, on ne réussit jamais seul. Le Niveau 5 met en pratique la compétence la plus essentielle : **transmettre et aider ses pairs**.

1. Lorsqu'une équipe termine le Niveau 4, elle est invitée à repérer une autre équipe encore bloquée aux Niveaux 1, 2 ou 3.
2. **Règle absolue** : Interdiction formelle de toucher au clavier ou à la souris de l'autre équipe. Ils doivent guider par la parole et les questions.
3. Dès que l'autre équipe débloque son niveau grâce à eux, ils vous appellent.
4. Vous venez sur leur poste, vérifiez rapidement qu'ils ont bien expliqué la démarche, et saisissez le mot de passe confidentiel :
   ```text
   MENTOR42
   ```
5. L'écran de victoire finale s'affiche avec fanfare 8-bit et lancer de confettis ! 🏆

---

## 🏗️ Structure du Projet

```text
Tech-For-All-42/
├── server.py              # Serveur multithreadé centralisé (API statut, déblocage dynamique, hints, /admin)
├── build_page.py          # Générateur Zero-Knowledge (chiffre les niveaux et compile index.html)
├── setup_mission.sh       # Script préparant mission_42 (arborescence enrichie, anecdotes, templates)
├── index.html             # Sujet web principal (Thème clair, offline, fonts 42 officielles)
├── station.html           # Page cible d'inspection web du Niveau 2 (leurres + jeton officiel)
├── decrypt.py             # Script starter de déchiffrement César (débloqué au Niveau 2)
├── slot_machine.py        # Script starter de machine à sous (débloqué au Niveau 3)
├── moulinette.py          # Outil de certification CLI officiel pour la machine à sous
├── payloads.json          # Données chiffrées des niveaux (SHA256-CTR)
├── fonts/                 # Typographies officielles 42 (Futura-PT, JetBrains Mono)
└── *.png, *.svg           # Logos 42 et icônes
```

---

## 🛡️ Sécurité & Tricherie (Zero-Knowledge)

* **Impossible de tricher via l'Inspecteur (`F12`)** : Les niveaux verrouillés sont chiffrés avec un algorithme de flux basé sur SHA256. Le contenu HTML des niveaux 2, 3, 4 et 5 n'existe tout simplement pas dans le navigateur de l'élève tant que la clé exacte n'a pas été saisie.
* **Aucune clé dans les placeholders ou commentaires** : Les champs de saisie utilisent des placeholders génériques et le JavaScript ne contient aucune liste de réponses en clair.
* **Indices protégés côté serveur** : En mode Lycée, le serveur refuse catégoriquement de délivrer les indices (`403 Forbidden`).
* **Déblocage dynamique synchronisé** : Les fichiers `decrypt.py` et `slot_machine.py` ne polluent pas le bureau dès le départ et ne sont injectés que lors de la validation effective. En cas de réinitialisation, ils sont nettoyés automatiquement.

---

## 🔧 Dépannage & FAQ

### Les élèves n'arrivent pas à ouvrir la page web (`http://IP:8000/`)
1. Vérifiez que la machine organisateur et les postes élèves sont bien sur le **même sous-réseau** (Wi-Fi ou switch Ethernet).
2. Vérifiez le pare-feu Ubuntu de la machine hôte :
   ```bash
   sudo ufw allow 8000/tcp
   ```
3. Testez l'accessibilité avec un simple `ping <IP_HÔTE>` depuis un poste élève.

### Un élève veut réinitialiser sa progression
Un bouton discret **`↺ Recommencer la mission`** est présent dans le pied de page du sujet web. Il réinitialise le `localStorage`, envoie une requête de nettoyage des fichiers au serveur (`/api/reset`), et recharge l'épreuve à zéro.

### Modifier un texte ou recompiler la page web
Si vous modifiez les textes ou les clés dans `build_page.py`, recompilez la page avec :
```bash
python3 build_page.py
```
Cela met à jour automatiquement `index.html`, `sujet_fr.html` et `payloads.json`.

---

## 👥 Crédits & Licence

Projet conçu pour les ateliers de découverte et événements **Tech For All** de l'**École 42 Paris**.
Libre d'utilisation et de partage pour tout événement éducatif associatif ou scolaire.
