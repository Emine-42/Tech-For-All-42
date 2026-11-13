#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
42 | SERVEUR WEB CENTRALISÉ D'ATELIER & CONTRÔLE ADMIN
==============================================================================
Ce serveur héberge le sujet pour toute la salle et permet à l'organisateur
(et UNIQUEMENT à lui) de basculer le mode pour tout le monde :
  - Mode Lycée (Intermédiaire) : Zéro indice, esprit 42 pur.
  - Mode Collège (Facile)      : Indices progressifs (-50 pts puis 0 pt).

L'organisateur peut changer le mode :
  1. En direct depuis son terminal en tapant 'm' + Entrée
  2. Depuis son navigateur sur http://localhost:8000/ (bouton ⚙️ Admin)
  3. Depuis le tableau de bord dédié http://localhost:8000/admin

Usage :
    python3 server.py [PORT] [--easy | --intermediate]
Exemple :
    python3 server.py 8000
==============================================================================
"""

import sys
import os
import json
import socket
import threading
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, SimpleHTTPRequestHandler

# ------------------------------------------------------------------------------
# CONFIGURATION GLOBALE DU SERVEUR
# ------------------------------------------------------------------------------
ADMIN_SECRET_TOKEN = "42admin"
DEFAULT_MODE = "intermediate"  # "intermediate" (Lycée) ou "easy" (Collège)
current_mode = DEFAULT_MODE
mode_lock = threading.Lock()

# Banque d'indices confidentielle (réservée au serveur, invisible dans index.html)
SERVER_HINTS = {
    1: {
        1: "💡 <strong>Indice 1 (-50 pts) :</strong> Sous Linux, les fichiers système commencent souvent par un point <code>.</code> pour être masqués. Dans votre Boîte à Outils, repérez quelle commande permet de lister TOUS les fichiers (y compris cachés). Fouillez dans les sous-dossiers de <code>archives</code> !",
        2: "🚨 <strong>Solution directe (0 pt) :</strong> Le fichier se nomme <code>.htaccess</code> et se trouve dans <code>archives/2023/configs/</code>. Affichez-le avec : <code>cat archives/2023/configs/.htaccess</code> pour copier la clé."
    },
    2: {
        1: "💡 <strong>Indice 1 (-50 pts) :</strong> Ouvrez la page <code class=\"inline\">station.html</code>, appuyez sur <kbd>F12</kbd> pour afficher l'Inspecteur d'éléments, puis inspectez les champs à l'intérieur de la balise <code>&lt;form&gt;</code>.",
        2: "🚨 <strong>Solution directe (0 pt) :</strong> Le jeton est dissimulé dans le champ caché <code>&lt;input type=\"hidden\" id=\"auth_token\" value=\"WEB-INSPECTOR-42\"&gt;</code>."
    },
    3: {
        1: "💡 <strong>Indice 1 (-50 pts) :</strong> Pour reculer de 'decalage' crans dans l'alphabet (modulo 26) : <code>position = (ord(lettre) - ord('A') - decalage) % 26</code> puis <code>lettre_decalee = chr(position + ord('A'))</code>.",
        2: "🚨 <strong>Solution directe (0 pt) :</strong> Le bon décalage est la Clé 03. Le message secret déchiffré à entrer est : <code>42_MACHINE_A_SOUS</code>"
    },
    4: {
        1: "💡 <strong>Indice 1 (-50 pts) :</strong> Pour tester si au moins 2 symboles sont identiques, utilisez <code>or</code> : <code>elif r1 == r2 or r1 == r3 or r2 == r3:</code>. Respectez scrupuleusement la casse des mots <code>JACKPOT</code>, <code>PAIRE</code> et <code>PERDU</code>.",
        2: "🚨 <strong>Solution directe (0 pt) :</strong> 3 identiques : <code>print(\"JACKPOT\")</code> et <code>credits += 50</code>. Au moins 2 identiques : <code>print(\"PAIRE\")</code> et <code>credits += 15</code>. Sinon : <code>print(\"PERDU\")</code>. Puis lancez <code>python3 moulinette.py</code>."
    },
    5: {
        1: "💡 <strong>Indice 1 (-50 pts) :</strong> Trouvez un binôme bloqué dans la salle. Posez-leur des questions pour les débloquer SANS JAMAIS toucher à leur clavier ou souris !",
        2: "🚨 <strong>Solution directe (0 pt) :</strong> Une fois votre entraide effectuée, levez la main dans la salle pour appeler un Mentor 42. C'est lui qui viendra saisir son mot de passe confidentiel."
    }
}

def get_lan_ip():
    """Détecte l'adresse IP locale sur le réseau de la salle."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def get_current_mode():
    with mode_lock:
        return current_mode

def set_current_mode(new_mode):
    global current_mode
    with mode_lock:
        if new_mode in ("easy", "intermediate"):
            current_mode = new_mode
            label = "🎒 COLLÈGE (Facile)" if new_mode == "easy" else "🎓 LYCÉE (Intermédiaire)"
            print(f"\n📢 [ADMIN] Mode d'atelier basculé pour TOUTE la salle : {label}\n>>> ", end="", flush=True)
            return True
        return False

# ------------------------------------------------------------------------------
# PAGE HTML DU TABLEAU DE BORD ORGANISATEUR (/ADMIN)
# ------------------------------------------------------------------------------
ADMIN_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>42 | Panneau Organisateur (Admin)</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="stylesheet" href="fonts/fonts.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: #0b0f19;
            font-family: 'futura-pt', -apple-system, sans-serif;
            color: #f1f5f9;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .admin-card {
            background: #131b2a;
            border: 1px solid #223049;
            border-top: 4px solid #00babc;
            border-radius: 12px;
            padding: 35px 30px;
            max-width: 560px;
            width: 100%;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        }
        h1 { font-size: 1.4rem; color: #fff; margin-bottom: 6px; display: flex; align-items: center; gap: 10px; }
        p.sub { font-size: 0.88rem; color: #94a3b8; margin-bottom: 24px; }
        .mode-box {
            background: #090e1a;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .mode-status-title { font-size: 0.82rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 700; margin-bottom: 4px; }
        .mode-status-val { font-size: 1.15rem; font-weight: 700; color: #00babc; }
        .actions-grid { display: flex; flex-direction: column; gap: 12px; margin-bottom: 25px; }
        .btn-choice {
            background: #1a2538;
            border: 2px solid #2a3b59;
            color: #f1f5f9;
            padding: 16px 20px;
            border-radius: 8px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .btn-choice:hover { border-color: #00babc; background: #1e2c44; transform: translateY(-1px); }
        .btn-choice.active { border-color: #00babc; background: #002b2c; box-shadow: 0 0 15px rgba(0,186,188,0.25); }
        .btn-choice .icon { font-size: 1.8rem; }
        .btn-choice .text strong { display: block; font-size: 1rem; color: #fff; }
        .btn-choice .text small { color: #94a3b8; font-size: 0.82rem; }
        .server-links {
            background: #090e1a;
            border-radius: 6px;
            padding: 12px 16px;
            font-size: 0.85rem;
            color: #94a3b8;
            font-family: monospace;
            line-height: 1.6;
        }
        .server-links a { color: #00babc; text-decoration: none; }
        .server-links a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="admin-card">
        <h1>🛡️ Contrôle Organisateur 42</h1>
        <p class="sub">Changez le niveau d'accompagnement pour tous les élèves en temps réel</p>

        <div class="mode-box">
            <div>
                <div class="mode-status-title">Mode Actif sur le Réseau</div>
                <div class="mode-status-val" id="current-mode-label">Chargement...</div>
            </div>
            <span style="font-size: 2rem;" id="current-mode-emoji">⏳</span>
        </div>

        <div class="actions-grid">
            <button class="btn-choice" id="choice-intermediate" onclick="changeMode('intermediate')">
                <span class="icon">🎓</span>
                <div class="text">
                    <strong>Mode Lycée (Intermédiaire)</strong>
                    <small>Esprit 42 pur : Aucun bouton d'indice, autonomie et peer-learning obligatoires.</small>
                </div>
            </button>
            <button class="btn-choice" id="choice-easy" onclick="changeMode('easy')">
                <span class="icon">🎒</span>
                <div class="text">
                    <strong>Mode Collège (Facile)</strong>
                    <small>Indices progressifs activés (-50 pts puis 0 pt) et score visible sur 500 pts.</small>
                </div>
            </button>
        </div>

        <div class="server-links">
            <div>📡 Sujet Élevés : <a href="/" target="_blank" id="student-link">http://.../</a></div>
            <div>🔒 Page Station : <a href="/station.html" target="_blank">/station.html</a></div>
        </div>
    </div>

    <script>
        async function fetchStatus() {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();
                updateUI(data.mode);
                document.getElementById('student-link').innerText = `http://${data.lan_ip}:${data.port}/`;
                document.getElementById('student-link').href = `http://${data.lan_ip}:${data.port}/`;
            } catch(e) {}
        }

        function updateUI(mode) {
            const isEasy = (mode === 'easy');
            document.getElementById('current-mode-label').innerText = isEasy ? "🎒 Collège (Facile avec indices)" : "🎓 Lycée (Intermédiaire pur 42)";
            document.getElementById('current-mode-emoji').innerText = isEasy ? "🎒" : "🎓";
            
            const btnInter = document.getElementById('choice-intermediate');
            const btnEasy = document.getElementById('choice-easy');
            if (isEasy) {
                btnEasy.classList.add('active');
                btnInter.classList.remove('active');
            } else {
                btnInter.classList.add('active');
                btnEasy.classList.remove('active');
            }
        }

        async function changeMode(newMode) {
            try {
                const res = await fetch('/api/mode', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ mode: newMode })
                });
                const data = await res.json();
                if (data.status === 'ok') {
                    updateUI(data.mode);
                } else {
                    alert(data.error || "Action refusée.");
                }
            } catch(e) {
                alert("Erreur de connexion.");
            }
        }

        fetchStatus();
        setInterval(fetchStatus, 3000);
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------
# GESTIONNAIRE DE REQUÊTES HTTP SÉCURISÉ
# ------------------------------------------------------------------------------
class WorkshopHTTPHandler(SimpleHTTPRequestHandler):

    def is_admin_authorized(self):
        """Vérifie si la requête provient de la machine locale ou porte le jeton secret."""
        client_ip = self.client_address[0]
        if client_ip in ("127.0.0.1", "localhost", "::1"):
            return True
        auth_header = self.headers.get("Authorization", "")
        if auth_header == f"Bearer {ADMIN_SECRET_TOKEN}":
            return True
        token_header = self.headers.get("X-Admin-Token", "")
        if token_header == ADMIN_SECRET_TOKEN:
            return True
        return False

    def send_json(self, status_code, data):
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # 1. API Statut (accessible à tous pour synchronisation temps réel)
        if path == "/api/status":
            self.send_json(200, {
                "mode": get_current_mode(),
                "lan_ip": getattr(self.server, "lan_ip", "localhost"),
                "port": getattr(self.server, "server_port", 8000)
            })
            return

        # 2. Panneau d'Administration Organisateur (/admin)
        if path in ("/admin", "/admin/"):
            admin_bytes = ADMIN_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(admin_bytes)))
            self.end_headers()
            self.wfile.write(admin_bytes)
            return

        # 3. API d'Indices Sécurisée (/api/hint?level=X&step=Y)
        if path == "/api/hint":
            # Si le mode est Intermédiaire (Lycée), les indices sont formellement bloqués
            if get_current_mode() == "intermediate":
                self.send_json(403, {
                    "error": "Les indices sont désactivés pour cet atelier (Mode Lycée / Esprit 42)."
                })
                return

            qs = parse_qs(parsed.query)
            try:
                lvl = int(qs.get("level", [0])[0])
                step = int(qs.get("step", [1])[0])
                hint_text = SERVER_HINTS.get(lvl, {}).get(step)
                if hint_text:
                    self.send_json(200, {"hint": hint_text, "level": lvl, "step": step})
                else:
                    self.send_json(404, {"error": "Indice non trouvé."})
            except Exception:
                self.send_json(400, {"error": "Paramètres invalides."})
            return

        # 4. Fichiers statiques normaux (index.html, station.html, css, png...)
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # Changement de mode réservé à l'administrateur
        if path == "/api/mode":
            if not self.is_admin_authorized():
                self.send_json(403, {
                    "error": "Seul l'administrateur peut modifier le niveau d'atelier pour la salle."
                })
                return

            try:
                content_len = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_len).decode("utf-8")
                data = json.loads(body)
                requested_mode = data.get("mode")
                if set_current_mode(requested_mode):
                    self.send_json(200, {"status": "ok", "mode": get_current_mode()})
                else:
                    self.send_json(400, {"error": "Mode inconnu (choisir 'easy' ou 'intermediate')."})
            except Exception as e:
                self.send_json(500, {"error": str(e)})
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        # Filtre les requêtes de polling périodique pour garder le terminal propre
        if len(args) > 0 and any(p in str(args[0]) for p in ("/api/status", "favicon")):
            return
        super().log_message(format, *args)

# ------------------------------------------------------------------------------
# BOUCLE INTERACTIVE DU TERMINAL (POUR L'ORGANISATEUR)
# ------------------------------------------------------------------------------
def console_listener():
    """Permet à l'organisateur de taper 'm' dans le terminal pour basculer de mode."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            cmd = line.strip().lower()
            if cmd in ("m", "mode", "switch"):
                new_m = "easy" if get_current_mode() == "intermediate" else "intermediate"
                set_current_mode(new_m)
            elif cmd in ("status", "info"):
                m = get_current_mode()
                label = "🎒 Collège (Facile avec indices)" if m == "easy" else "🎓 Lycée (Intermédiaire pur 42)"
                print(f"[INFO] Mode d'atelier actuel : {label}\n>>> ", end="", flush=True)
            elif cmd in ("h", "help", "?"):
                print("Commandes disponibles :\n  'm'      : Basculer entre Collège et Lycée\n  'status' : Afficher le mode actif\n  'q'      : Quitter\n>>> ", end="", flush=True)
            elif cmd in ("q", "quit", "exit"):
                print("\nArrêt du serveur demandé.")
                os._exit(0)
            elif cmd:
                print("Tapez 'm' pour basculer le mode ou 'h' pour l'aide.\n>>> ", end="", flush=True)
        except Exception:
            break

# ------------------------------------------------------------------------------
# POINT D'ENTRÉE PRINCIPAL
# ------------------------------------------------------------------------------
def main():
    global current_mode
    port = 8000
    
    # Arguments CLI
    for arg in sys.argv[1:]:
        if arg.isdigit():
            port = int(arg)
        elif arg in ("--easy", "-e", "easy"):
            current_mode = "easy"
        elif arg in ("--intermediate", "-i", "intermediate"):
            current_mode = "intermediate"

    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workspace_dir)

    lan_ip = get_lan_ip()

    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, WorkshopHTTPHandler)
    httpd.lan_ip = lan_ip
    httpd.server_port = port

    mode_label = "🎒 COLLÈGE (Facile)" if current_mode == "easy" else "🎓 LYCÉE (Intermédiaire)"

    print("\n" + "=" * 75)
    print("  🚀 SERVEUR DE L'ATELIER 42 EN LIGNE !")
    print("=" * 75)
    print(f"\n  📡 Lien à donner aux ÉLÈVES dans la salle :")
    print(f"\n     👉  http://{lan_ip}:{port}/\n")
    print(f"  🛡️ Panneau Organisateur (Admin) :")
    print(f"     👉  http://localhost:{port}/admin\n")
    print(f"  ⚙️ Mode d'atelier actif : {mode_label}")
    print(f"     (Tapez 'm' + Entrée dans ce terminal pour basculer en direct !)")
    print("=" * 75 + "\n>>> ", end="", flush=True)

    # Démarre le thread de saisie console
    t = threading.Thread(target=console_listener, daemon=True)
    t.start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur. À bientôt à 42 !")
        httpd.server_close()

if __name__ == "__main__":
    main()
