#!/bin/bash
# ==============================================================================
# 42 | SCRIPT D'INSTALLATION DE LA MISSION (POUR L'ORGANISATEUR)
# ==============================================================================

if [ -d "$HOME/Bureau" ]; then
    DEST_DIR="$HOME/Bureau/mission_42"
else
    DEST_DIR="$HOME/Desktop/mission_42"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📁 Préparation du dossier de mission dans : $DEST_DIR"
rm -rf "$DEST_DIR"
mkdir -p "$DEST_DIR"

# ------------------------------------------------------------------------------
# 1. ARBORESCENCE DENSE DU DOSSIER ARCHIVES & SYSTÈME (EXERCICE 1)
# ------------------------------------------------------------------------------
mkdir -p "$DEST_DIR/archives/1989_origins"
mkdir -p "$DEST_DIR/archives/1991_kernel"
mkdir -p "$DEST_DIR/archives/2004_ubuntu"
mkdir -p "$DEST_DIR/archives/2013_fondation_42"
mkdir -p "$DEST_DIR/archives/2020/pedagogie"
mkdir -p "$DEST_DIR/archives/2021/rapports"
mkdir -p "$DEST_DIR/archives/2022/backups"
mkdir -p "$DEST_DIR/archives/2022/system"
mkdir -p "$DEST_DIR/archives/2022/hardware"
mkdir -p "$DEST_DIR/archives/2023/configs"
mkdir -p "$DEST_DIR/archives/2023/logs"
mkdir -p "$DEST_DIR/archives/2024/db_dumps"
mkdir -p "$DEST_DIR/archives/2024/exports"
mkdir -p "$DEST_DIR/archives/2024/ai_history"
mkdir -p "$DEST_DIR/archives/2025/infra"
mkdir -p "$DEST_DIR/archives/2025/norme"
mkdir -p "$DEST_DIR/systeme/bin"
mkdir -p "$DEST_DIR/systeme/modules"
mkdir -p "$DEST_DIR/donnees/cache"
mkdir -p "$DEST_DIR/donnees/telemetrie"

# ------------------------------------------------------------------------------
# 2. ANECDOTES HISTORIQUES & FUN FACTS (ESPRIT 42)
# ------------------------------------------------------------------------------
cat << 'EOF' > "$DEST_DIR/archives/1989_origins/bash_manifesto.txt"
[HISTOIRE BASH]
BASH signifie "Bourne Again SHell". Conçu par Brian Fox en 1989 pour le projet GNU,
c'est un jeu de mots avec le créateur de sh, Steve Bourne ("born again").
EOF

cat << 'EOF' > "$DEST_DIR/archives/1991_kernel/linus_note.txt"
[FUN FACT LINUX]
Tux, le manchot mascotte de Linux, a été suggéré par Linus Torvalds.
Lors d'une visite au zoo de Canberra en 1993, un petit manchot lui avait mordu le doigt !
EOF

cat << 'EOF' > "$DEST_DIR/archives/2004_ubuntu/humanity.txt"
[PHILOSOPHIE UBUNTU]
Ubuntu est un concept zoulou et xhosa : "Je suis ce que je suis grâce à ce que nous sommes tous".
Une distribution Linux créée pour rendre la puissance d'Unix accessible à chaque humain.
EOF

cat << 'EOF' > "$DEST_DIR/archives/2013_fondation_42/douglas_adams.txt"
[POURQUOI 42 ?]
Dans "Le Guide du voyageur galactique" de Douglas Adams, le supercalculateur Deep Thought
calcule pendant 7,5 millions d'années la Réponse à la Question Ultime sur la vie, l'univers
et le reste : le résultat est 42.
EOF

cat << 'EOF' > "$DEST_DIR/archives/2013_fondation_42/le_bocal.txt"
[LE BOCAL DE 42]
À l'École 42, l'équipe des administrateurs système et de la pédagogie travaille
dans une salle vitrée visible de tous, affectueusement baptisée "Le Bocal".
EOF

cat << 'EOF' > "$DEST_DIR/archives/2013_fondation_42/la_piscine.txt"
[LA PISCINE]
26 jours d'immersion totale jour et nuit. Pas de profs, pas d'horaires imposés,
du code C du matin au soir et de l'entraide mutuelle pour apprendre à nager !
EOF

cat << 'EOF' > "$DEST_DIR/archives/2020/pedagogie/peer_learning.txt"
[PEER-LEARNING]
À 42, vous n'êtes jamais passif devant un cours. Vous apprenez en faisant,
en posant des questions à vos pairs et en évaluant le code de vos camarades.
EOF

cat << 'EOF' > "$DEST_DIR/archives/2022/hardware/first_bug_hopper.txt"
[LE PREMIER BUG]
En 1947, l'informaticienne Grace Hopper découvre un papillon de nuit (moth)
coincé dans un relais du calculateur Mark II. Elle le colle dans son carnet :
c'est le premier bug informatique documenté de l'Histoire !
EOF

cat << 'EOF' > "$DEST_DIR/archives/2024/ai_history/turing_test.txt"
[ORIGINES DE L'IA]
En 1950, Alan Turing publie son article fondateur sur "The Imitation Game".
Il y pose la question vertigineuse : "Les machines peuvent-elles penser ?".
EOF

cat << 'EOF' > "$DEST_DIR/archives/2024/ai_history/perceptron_1958.txt"
[NEURONES ARTIFICIELS]
En 1958, Frank Rosenblatt conçoit le Perceptron au Cornell Aeronautical Lab.
C'est le tout premier modèle informatique de réseau neuronal capable d'apprendre.
EOF

cat << 'EOF' > "$DEST_DIR/archives/2025/norme/regles_42.txt"
[LA NORME 42]
Fonctions limitées à 25 lignes maximum. Pas plus de 5 variables par fonction.
Pas de boucles 'for', pas de 'switch'. La rigueur de code forgée par 42 !
EOF

# ------------------------------------------------------------------------------
# 3. FICHIERS SYSTÈMES & LEURRES D'ARCHIVES
# ------------------------------------------------------------------------------
echo "Rapport d'activité 2021 - Tous systèmes opérationnels." > "$DEST_DIR/archives/2021/rapports/bilan_annuel.txt"
echo "Sauvegarde base de données 2022 - Fichier corrompu." > "$DEST_DIR/archives/2022/backups/backup_2022.sql"
echo "kernel.core_pattern = /var/crash/core.%p" > "$DEST_DIR/archives/2022/system/sysctl.conf"
echo "[server]\nport=4242\nhost=0.0.0.0" > "$DEST_DIR/archives/2023/configs/app.ini"
echo "server { listen 80; server_name cluster42.lan; }" > "$DEST_DIR/archives/2023/configs/nginx_vhost.conf"
echo "2023-11-04 14:22:01 [WARN] Connexion fermée par le pair." > "$DEST_DIR/archives/2023/logs/access.log"
echo "2023-11-04 15:30:12 [ERROR] Disque presque saturé." > "$DEST_DIR/archives/2023/logs/error.log"
echo "TABLE users (id INT, login VARCHAR(50));" > "$DEST_DIR/archives/2024/db_dumps/schema.sql"
echo "Export des données stagiaires 2024." > "$DEST_DIR/archives/2024/exports/liste_etudiants.csv"
echo "Cluster nodes: 420 postes sous Ubuntu 24.04 LTS." > "$DEST_DIR/archives/2025/infra/cluster_notes.txt"
echo "Diagnostic système OK." > "$DEST_DIR/systeme/bin/diagnostic.sh"
echo "Faux chemin ! Continue de fouiller l'arborescence des archives." > "$DEST_DIR/systeme/readme.txt"
echo "# Cache temporaire" > "$DEST_DIR/donnees/cache/session.tmp"
echo "PING cluster OK - latence 0.42ms" > "$DEST_DIR/donnees/telemetrie/pings.log"

# Faux fichiers cachés innocents
echo "TMP_DIR=/tmp" > "$DEST_DIR/archives/2022/system/.env.example"
echo "DEBUG=false" > "$DEST_DIR/archives/2023/logs/.debug"
echo "build_hash=42a8f9c1" > "$DEST_DIR/archives/2025/infra/.docker_cache"

# ------------------------------------------------------------------------------
# 4. FICHIER SECRET DU NIVEAU 1 : .htaccess
# ------------------------------------------------------------------------------
cat << 'EOF' > "$DEST_DIR/archives/2023/configs/.htaccess"
# ==============================================================================
# 42 SECURITY CONFIGURATION FILE — ACCESS OVERRIDE
# ==============================================================================
# Bravo ! Vous avez repéré le fichier d'accès système !
#
# Clé de déverrouillage pour le Niveau 2 :
#
#    BASH-EXPLORER-42
#
# (Entrez cette clé sur la page web pour débloquer le Niveau 2)
# ==============================================================================
SetEnv MISSION_KEY "BASH-EXPLORER-42"
EOF

# ------------------------------------------------------------------------------
# 5. STOCKAGE ISOLÉ DES SCRIPTS DE DÉVERROUILLAGE
# (Stockés en dehors du dossier mission_42 dans ~/.local/share/42_mission_templates
# pour être 100% invisibles lors de l'exploration de l'Exercice 1)
# ------------------------------------------------------------------------------
STORAGE_DIR="$HOME/.local/share/42_mission_templates"
rm -rf "$STORAGE_DIR"
mkdir -p "$STORAGE_DIR"

cp "$SCRIPT_DIR/decrypt.py" "$STORAGE_DIR/"
cp "$SCRIPT_DIR/slot_machine.py" "$STORAGE_DIR/"
cp "$SCRIPT_DIR/moulinette.py" "$STORAGE_DIR/"
chmod +x "$STORAGE_DIR/moulinette.py"

echo "✅ Dossier mission_42 généré avec succès dans $DEST_DIR !"
echo "🔒 Templates des scripts stockés de manière isolée dans $STORAGE_DIR."
echo "ℹ️  decrypt.py, slot_machine.py et moulinette.py apparaîtront au moment opportun."
