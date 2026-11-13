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
# 1. ARBORESCENCE DENSE DU DOSSIER ARCHIVES (EXERCICE 1)
# ------------------------------------------------------------------------------
mkdir -p "$DEST_DIR/archives/2021/rapports"
mkdir -p "$DEST_DIR/archives/2022/backups"
mkdir -p "$DEST_DIR/archives/2022/system"
mkdir -p "$DEST_DIR/archives/2023/configs"
mkdir -p "$DEST_DIR/archives/2023/logs"
mkdir -p "$DEST_DIR/archives/2024/db_dumps"
mkdir -p "$DEST_DIR/archives/2024/exports"
mkdir -p "$DEST_DIR/systeme/bin"
mkdir -p "$DEST_DIR/systeme/modules"
mkdir -p "$DEST_DIR/donnees/cache"

# Fichiers leurres (fichiers normaux)
echo "Rapport d'activité 2021 - Tous systèmes opérationnels." > "$DEST_DIR/archives/2021/rapports/bilan_annuel.txt"
echo "Sauvegarde base de données 2022 - Fichier corrompu." > "$DEST_DIR/archives/2022/backups/backup_2022.sql"
echo "kernel.core_pattern = /var/crash/core.%p" > "$DEST_DIR/archives/2022/system/sysctl.conf"
echo "[server]\nport=4242\nhost=0.0.0.0" > "$DEST_DIR/archives/2023/configs/app.ini"
echo "2023-11-04 14:22:01 [WARN] Connexion fermée par le pair." > "$DEST_DIR/archives/2023/logs/access.log"
echo "2023-11-04 15:30:12 [ERROR] Disque presque saturé." > "$DEST_DIR/archives/2023/logs/error.log"
echo "TABLE users (id INT, login VARCHAR(50));" > "$DEST_DIR/archives/2024/db_dumps/schema.sql"
echo "Export des données stagiaires 2024." > "$DEST_DIR/archives/2024/exports/liste_etudiants.csv"
echo "Faux chemin ! Continue de fouiller l'arborescence des archives." > "$DEST_DIR/systeme/readme.txt"
echo "# Cache temporaire" > "$DEST_DIR/donnees/cache/session.tmp"

# Faux fichiers cachés innocents
echo "TMP_DIR=/tmp" > "$DEST_DIR/archives/2022/system/.env.example"
echo "DEBUG=false" > "$DEST_DIR/archives/2023/logs/.debug"

# FICHIER SECRET DU NIVEAU 1 : .htaccess
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
# 2. SCRIPTS PYTHON FOURNIS AUX ÉLÈVES
# ------------------------------------------------------------------------------
cp "$SCRIPT_DIR/decrypt.py" "$DEST_DIR/"
cp "$SCRIPT_DIR/slot_machine.py" "$DEST_DIR/"
cp "$SCRIPT_DIR/moulinette.py" "$DEST_DIR/"
chmod +x "$DEST_DIR/moulinette.py"

echo "✅ Dossier mission_42 généré avec succès dans $DEST_DIR !"
