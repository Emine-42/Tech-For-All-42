#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération de sujet_fr.html / index.html
- Thème Clair 42 (Light Mode)
- Chiffrement Zero-Knowledge
- Système de Score (500 pts) et Indices Dégressifs (Mode Collège / Lycée)
- Liens hébergés (station.html)
"""

import hashlib
import base64
import json

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def encrypt(plaintext: str, key: str) -> str:
    data = ("42_OK::" + plaintext).encode("utf-8")
    res = bytearray()
    counter = 0
    while len(res) < len(data):
        h = sha256_hex(f"{key}:{counter}")
        h_bytes = bytes.fromhex(h)
        for b in h_bytes:
            if len(res) < len(data):
                res.append(data[len(res)] ^ b)
            else:
                break
        counter += 1
    return base64.b64encode(res).decode("ascii")

# ------------------------------------------------------------------------------
# CONTENUS DES NIVEAUX (ÉPREUVES RÉVISÉES)
# ------------------------------------------------------------------------------

# NIVEAU 2 : Inspection Web de la page hébergée station.html
lvl2_html = """<p class="desc">Le premier code a déverrouillé l'accès à la <strong>Station d'Accès Sécurisée</strong> hébergée sur le serveur. Sur cette page, un jeton secret d'autorisation a été injecté dans la structure du document.</p>

<div class="rules-callout" style="border-left-color: #00babc; background: #f0fdfa;">
    <strong style="color: #007779;">🎯 Objectif de l'épreuve :</strong>
    <p style="margin: 4px 0 10px 0;">Ouvrez la page cible dans un nouvel onglet, ouvrez l'inspecteur d'éléments (touche <code class="inline">F12</code>) et repérez la clé secrète.</p>
    <a href="station.html" target="_blank" class="action-link-btn">🔗 Ouvrir la Station d'Accès Sécurisée ↗</a>
</div>

<ul class="step-list">
    <li>Cliquez sur le lien ci-dessus pour ouvrir la page <code class="inline">station.html</code>.</li>
    <li>Appuyez sur <code class="inline">F12</code> (ou clic droit &gt; <em>Inspecter</em>) pour explorer la page.</li>
    <li><strong>Masque de la clé recherchée :</strong> <code class="inline" style="letter-spacing: 2px; font-weight: 700; color: #b91c1c;">W**-*NS******-**</code></li>
    <li><em>Attention aux pièges :</em> plusieurs clés leurres au même format sont dissimulées sur la page. Seul le jeton d'autorisation officiel placé dans le formulaire de connexion est valide.</li>
    <li>Une fois la clé identifiée, copiez-la et collez-la ci-dessous pour valider l'Étoile 2 !</li>
</ul>

<!-- WIDGET D'INDICE (MODE COLLÈGE / LYCÉE) -->
<div class="hint-widget" id="hint-widget-2">
    <div class="hint-header">
        <button class="hint-btn" id="hint-btn-2" onclick="requestHint(2)">💡 Demander un indice (-50 pts)</button>
        <span class="hint-points-status" id="hint-pts-2">Valeur : 100 / 100 pts</span>
    </div>
    <div class="hint-box" id="hint-box-2" style="display: none;"></div>
</div>

<div class="validation-box">
    <div class="validation-header">
        <span class="validation-title">🔑 Validation du Niveau 2</span>
    </div>
    <p class="validation-hint">Entrez le jeton secret correspondant au format <code class="inline">W**-*NS******-**</code> :</p>
    <div class="validation-form">
        <input type="text" class="validation-input" id="input-level-2" placeholder="Entrez le jeton secret (format W**-*NS******-**)..." autocomplete="off">
        <button class="validate-btn" onclick="validateLevel2()">Valider l'Étoile 2 ⭐⭐</button>
    </div>
    <div class="feedback-msg" id="feedback-level-2"></div>
</div>"""

# NIVEAU 3 : Cryptanalyse César (Saisie directe du message en clair, pas de moulinette)
lvl3_html = """<div id="unlock-alert-decrypt" class="rules-callout" style="border-left-color: #10b981; background: #ecfdf5; margin-bottom: 20px;">
    <strong style="color: #047857;">🔓 Fichier débloqué dans votre terminal :</strong>
    <p style="margin: 6px 0 10px 0; color: #065f46; font-size: 0.92rem;">
        Le script Python à trous <code class="inline">decrypt.py</code> vient d'apparaître sur votre Bureau dans le dossier <code class="inline">mission_42/</code> !
    </p>
    <a href="/download/decrypt.py" download class="action-link-btn" style="background: #059669; font-size: 0.85rem; padding: 6px 14px;">📥 Télécharger decrypt.py (si distant)</a>
</div>

<p class="desc">Le message récupéré a été chiffré par un <strong>Chiffre de César</strong> (décalage de lettres dans l'alphabet). Votre mission : compléter le script Python à trous <code class="inline">decrypt.py</code> pour tester les 26 décalages possibles et trouver le lien en clair.</p>

<div class="code-container">
    <div class="code-header">
        <span>Fichier : decrypt.py (Python 3)</span>
        <button class="copy-btn" onclick="copyCode('code-decrypt')">Copier le code</button>
    </div>
    <pre id="code-decrypt"><span class="code-comment"># ==============================================================================
# NIVEAU 3 : decrypt.py (Code à trous)
# ==============================================================================</span>
message_secret = <span class="code-highlight">"42_PDFKLQH_D_VRXV"</span>

<span class="code-comment"># On teste les 26 décalages possibles de l'alphabet (Force Brute)</span>
<span class="code-keyword">for</span> decalage <span class="code-keyword">in</span> range(1, 26):
    resultat = ""
    <span class="code-keyword">for</span> lettre <span class="code-keyword">in</span> message_secret:
        <span class="code-keyword">if</span> 'A' &lt;= lettre &lt;= 'Z':
            <span class="code-comment"># ------------------------------------------------------------------
            # À COMPLÉTER : Recule de 'decalage' crans dans l'alphabet (modulo 26)
            # ord(lettre) donne le code ASCII (A=65, B=66...)
            # chr(...) reconvertit le nombre calculé en lettre majuscule
            # ------------------------------------------------------------------</span>
            ...
        <span class="code-keyword">else</span>:
            <span class="code-comment"># Si c'est un symbole (chiffres, _, :, /, etc.), on le conserve intact</span>
            ...
    print(f"Clé {decalage:02d} : {resultat}")</pre>
</div>

<ul class="step-list">
    <li>Ouvrez <code class="inline">decrypt.py</code> situé dans votre dossier <code class="inline">mission_42</code>.</li>
    <li>Complétez le calcul du décalage et lancez le programme avec <code class="inline">python3 decrypt.py</code>.</li>
    <li>Dans les 26 lignes affichées, <strong>repérez le message lisible commençant par 42_...</strong></li>
    <li>Copiez ce message déchiffré et entrez-le directement ci-dessous pour déverrouiller le Niveau 4 !</li>
</ul>

<!-- WIDGET D'INDICE (MODE COLLÈGE / LYCÉE) -->
<div class="hint-widget" id="hint-widget-3">
    <div class="hint-header">
        <button class="hint-btn" id="hint-btn-3" onclick="requestHint(3)">💡 Demander un indice (-50 pts)</button>
        <span class="hint-points-status" id="hint-pts-3">Valeur : 100 / 100 pts</span>
    </div>
    <div class="hint-box" id="hint-box-3" style="display: none;"></div>
</div>

<div class="validation-box">
    <div class="validation-header">
        <span class="validation-title">🔑 Validation du Niveau 3 (Message Déchiffré)</span>
    </div>
    <p class="validation-hint">Entrez le message secret déchiffré en clair dans le terminal :</p>
    <div class="validation-form">
        <input type="text" class="validation-input" id="input-level-3" placeholder="Entrez le message secret déchiffré..." autocomplete="off">
        <button class="validate-btn" onclick="validateLevel3()">Valider l'Étoile 3 ⭐⭐⭐</button>
    </div>
    <div class="feedback-msg" id="feedback-level-3"></div>
</div>"""

# NIVEAU 4 : Machine à sous (Consignes strictes d'affichage pour la Moulinette)
lvl4_html = """<div id="unlock-alert-slot" class="rules-callout" style="border-left-color: #10b981; background: #ecfdf5; margin-bottom: 20px;">
    <strong style="color: #047857;">🔓 Fichiers débloqués dans votre terminal :</strong>
    <p style="margin: 6px 0 10px 0; color: #065f46; font-size: 0.92rem;">
        Les scripts <code class="inline">slot_machine.py</code> et <code class="inline">moulinette.py</code> viennent d'apparaître sur votre Bureau dans le dossier <code class="inline">mission_42/</code> !
    </p>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="/download/slot_machine.py" download class="action-link-btn" style="background: #059669; font-size: 0.85rem; padding: 6px 14px;">📥 Télécharger slot_machine.py</a>
        <a href="/download/moulinette.py" download class="action-link-btn" style="background: #059669; font-size: 0.85rem; padding: 6px 14px;">📥 Télécharger moulinette.py</a>
    </div>
</div>

<p class="desc">Vous avez débloqué le jeu <code class="inline">slot_machine.py</code> ! Votre objectif est de programmer les <strong>conditions de gains</strong> (instructions <code class="inline">if / elif / else</code>) pour faire fonctionner la machine.</p>

<div class="rules-callout" style="border-left-color: #f59e0b; background: #fffdf5;">
    <strong style="color: #b45309;">🎯 Cahier des charges STRICT (Obligatoire pour la Moulinette) :</strong>
    <span style="display: block; margin-top: 6px;">
    • Démarrage à <strong>100 crédits</strong>. Chaque tirage coûte <strong>-10 crédits</strong>.<br>
    • <strong>3 symboles identiques :</strong> Afficher obligatoirement le mot <code class="inline" style="color: #b45309; font-weight: bold;">"JACKPOT"</code> et ajouter <strong>+50 crédits</strong>.<br>
    • <strong>Au moins 2 symboles identiques :</strong> Afficher obligatoirement le mot <code class="inline" style="color: #b45309; font-weight: bold;">"PAIRE"</code> et ajouter <strong>+15 crédits</strong>.<br>
    • <strong>Tous différents :</strong> Afficher obligatoirement le mot <code class="inline" style="color: #b45309; font-weight: bold;">"PERDU"</code> (gain : 0 crédit).
    </span>
</div>

<div class="code-container">
    <div class="code-header">
        <span>Fichier : slot_machine.py (Python 3)</span>
        <button class="copy-btn" onclick="copyCode('code-slot')">Copier le code</button>
    </div>
    <pre id="code-slot"><span class="code-comment"># ==============================================================================
# NIVEAU 4 : slot_machine.py (Code à trous)
# ==============================================================================</span>
<span class="code-keyword">import</span> random

credits = 100
symboles = ["7", "@", "#", "$"]

print("🎰 BIENVENUE AU CASINO DE 42 🎰")

<span class="code-keyword">while</span> credits &gt;= 10:
    input(f"\\n[Crédits : {credits}] Appuie sur ENTRÉE pour lancer (-10)...")
    credits -= 10
    
    r1 = random.choice(symboles)
    r2 = random.choice(symboles)
    r3 = random.choice(symboles)
    print(f"Résultat : [ {r1} | {r2} | {r3} ]")

    <span class="code-comment"># --------------------------------------------------------------------------
    # À COMPLÉTER : RÈGLES DE GAINS STRICTES
    # --------------------------------------------------------------------------</span>
    
    <span class="code-comment"># CAS 1 : 3 symboles identiques (Jackpot !)</span>
    ...

    <span class="code-comment"># CAS 2 : Au moins 2 symboles identiques (Paire)</span>
    ...

    <span class="code-comment"># CAS 3 : Aucun symbole identique (Perdu)</span>
    ...

print("\\n💀 Game Over ! Tu n'as plus assez de crédits.")</pre>
</div>

<ul class="step-list">
    <li>Complétez le fichier <code class="inline">slot_machine.py</code> avec les mots-clés exacts ci-dessus.</li>
    <li>Testez votre jeu avec <code class="inline">python3 slot_machine.py</code>.</li>
    <li><strong>Pour certifier votre code</strong>, lancez la Moulinette dans le terminal :<br>
        <code class="inline">python3 moulinette.py</code></li>
    <li>La Moulinette simulera des lancers pour certifier que les mots <code class="inline">JACKPOT</code>, <code class="inline">PAIRE</code> et <code class="inline">PERDU</code> ainsi que les crédits sont justes, puis vous délivrera le <strong>Code d'accès au Niveau 5</strong> !</li>
</ul>

<!-- WIDGET D'INDICE (MODE COLLÈGE / LYCÉE) -->
<div class="hint-widget" id="hint-widget-4">
    <div class="hint-header">
        <button class="hint-btn" id="hint-btn-4" onclick="requestHint(4)">💡 Demander un indice (-50 pts)</button>
        <span class="hint-points-status" id="hint-pts-4">Valeur : 100 / 100 pts</span>
    </div>
    <div class="hint-box" id="hint-box-4" style="display: none;"></div>
</div>

<div class="validation-box">
    <div class="validation-header">
        <span class="validation-title">⚙️ Validation par la Moulinette</span>
    </div>
    <p class="validation-hint">Entrez le code secret affiché par la Moulinette après le test de <code class="inline">slot_machine.py</code> :</p>
    <div class="validation-form">
        <input type="text" class="validation-input" id="input-level-4" placeholder="Entrez le code certifié par la Moulinette..." autocomplete="off">
        <button class="validate-btn" onclick="validateLevel4()">Valider l'Étoile 4 ⭐⭐⭐⭐</button>
    </div>
    <div class="feedback-msg" id="feedback-level-4"></div>
</div>"""

# NIVEAU 5 : Peer-Learning & Mentor
lvl5_html = """<p class="desc"><strong>À 42, on ne réussit jamais seul.</strong> Vous avez prouvé vos compétences techniques, il ne vous reste plus qu'à valider la compétence la plus importante de l'école : <strong>transmettre et aider vos pairs</strong>.</p>

<div class="mentor-callout">
    <strong>📜 Le Protocole Peer-Learning :</strong>
    <ul class="step-list" style="margin: 0;">
        <li>Repérez une autre équipe dans la salle qui est encore bloquée aux Niveaux 1, 2 ou 3.</li>
        <li><strong>RÈGLE ABSOLUE : Interdiction formelle de toucher à leur clavier ou à leur souris !</strong></li>
        <li>Posez-leur des questions pour les aider à trouver la solution par eux-mêmes (<em>"Que dit le terminal ?", "Avez-vous bien exploré l'arborescence ?"</em>).</li>
        <li>Dès que l'autre équipe a franchi son étape grâce à vos explications, <strong>levez la main pour appeler un Mentor 42</strong></li>
    </ul>
</div>

<div class="validation-box mentor-box">
    <div class="validation-header">
        <span class="validation-title">👑 Zone Réservée au Mentor 42</span>
        <span class="mentor-tag">Validation Physique</span>
    </div>
    <p class="validation-hint" style="color: #92400e;">Le mentor vient vérifier votre entraide sur place et saisit son mot de passe secret pour vous attribuer la 5ème Étoile :</p>
    <div class="validation-form">
        <input type="password" class="validation-input" id="input-level-5" placeholder="Mot de passe confidentiel du Mentor..." autocomplete="off">
        <button class="validate-btn mentor-btn" onclick="validateLevel5()">Valider la 5ème Étoile ⭐⭐⭐⭐⭐</button>
    </div>
    <div class="feedback-msg" id="feedback-level-5"></div>
</div>"""

victory_html = """<div class="victory-card">
    <div class="victory-stars">★★★★★</div>
    <h2>FÉLICITATIONS !</h2>
    <p>
        Vous venez de décrocher les <strong>5 Étoiles</strong> de la Chasse au Trésor de 42.<br><br>
        Terminal Linux, inspection web, cryptanalyse Python, logique algorithmique et entraide peer-to-peer : <strong>vous avez déjà l'étoffe d'un étudiant de 42 !</strong>
    </p>
    <div id="final-score-box" style="margin: 20px 0; padding: 15px; background: #f0fdfa; border: 1.5px solid #00babc; border-radius: 8px;">
        <span style="font-size: 1.1rem; font-weight: 700; color: #007779;">Score Final : <span id="final-points">500</span> / 500 Points 🏆</span>
    </div>
    <button class="victory-btn" onclick="closeVictoryModal()">Terminer l'Atelier 🏆</button>
</div>"""

payloads = {
    "level2": encrypt(lvl2_html, "BASH-EXPLORER-42"),
    "level3": encrypt(lvl3_html, "WEB-INSPECTOR-42"),
    "level4": encrypt(lvl4_html, "42_MACHINE_A_SOUS"),
    "level5": encrypt(lvl5_html, "CASINO-42-JACKPOT"),
    "victory": encrypt(victory_html, "MENTOR42")
}

with open("payloads.json", "w") as f:
    json.dump(payloads, f, indent=2)

payloads_js = json.dumps(payloads, indent=4)

# ------------------------------------------------------------------------------
# CODE HTML + CSS COMPLET DU SUJET CENTRAL (INDEX.HTML / SUJET_FR.HTML)
# ------------------------------------------------------------------------------

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>42 | Chasse au Trésor & Peer-Learning</title>

    <!-- Favicons -->
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="icon" type="image/png" sizes="96x96" href="favicon-96x96.png">
    <link rel="shortcut icon" href="favicon.ico">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">

    <!-- Typographies Officielles 42 (Offline Local) -->
    <link rel="stylesheet" href="fonts/fonts.css">

    <style>
        :root {{
            /* Palette Thème Clair Moderne 42 */
            --bg-body: #f4f6f9;
            --bg-card: #ffffff;
            --bg-card-header: #f8fafc;
            --border-card: #e2e8f0;
            --border-active: #00babc;
            
            --accent-42: #00babc;
            --accent-42-hover: #009ea0;
            --accent-42-dark: #007779;
            --accent-gold: #d97706;
            --accent-green: #059669;
            --accent-red: #dc2626;

            --text-main: #0f172a;
            --text-muted: #64748b;
            --text-light: #475569;

            --code-bg: #1e293b;
            --code-text: #f8fafc;
            
            --font-family: 'futura-pt', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-family);
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            min-height: 100vh;
            position: relative;
            background-image: 
                radial-gradient(circle at 10% 15%, rgba(0, 186, 188, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 90% 85%, rgba(16, 185, 129, 0.04) 0%, transparent 40%),
                linear-gradient(rgba(244, 246, 249, 0.96), rgba(244, 246, 249, 0.96)),
                url('bg.png');
            background-size: cover, cover, cover, 600px;
            background-attachment: fixed;
            padding-bottom: 80px;
        }}

        /* En-tête Sticky Clair */
        .top-navbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-card);
            padding: 12px 24px;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        }}

        .navbar-container {{
            max-width: 1050px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .brand-section {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .logo-42-img {{
            height: 40px;
            width: auto;
        }}

        .brand-text h1 {{
            font-size: 1.35rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .brand-text p {{
            font-size: 0.82rem;
            color: var(--accent-42-dark);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 700;
        }}

        .stats-section {{
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
        }}

        /* Badge de Mode (Contrôlé par l'Organisateur) */
        .mode-badge-box {{
            display: inline-flex;
            align-items: center;
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 20px;
            padding: 5px 14px;
            font-size: 0.82rem;
            font-weight: 700;
            color: #334155;
            gap: 8px;
        }}
        .admin-gear-btn {{
            background: #00babc;
            color: #042b2b;
            border: none;
            border-radius: 12px;
            padding: 3px 8px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
            margin-left: 6px;
            display: none;
            transition: all 0.2s;
        }}
        .admin-gear-btn:hover {{
            background: #008789;
            color: #fff;
        }}
        .admin-choice-card {{
            padding: 16px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
            background: #fff;
            width: 100%;
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .admin-choice-card:hover {{
            border-color: #00babc;
            background: #f0fdfa;
        }}
        .admin-choice-card.active {{
            border-color: #00babc;
            background: #f0fdfa;
            box-shadow: 0 0 0 1px #00babc;
        }}

        /* Jauge de Score */
        .score-counter {{
            background: #f0fdfa;
            border: 1px solid #ccfbf1;
            padding: 6px 14px;
            border-radius: 30px;
            font-weight: 700;
            color: #007779;
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.92rem;
        }}

        /* Chronomètre */
        .timer-box {{
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 6px 14px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-mono);
            font-size: 0.95rem;
            color: var(--accent-42-dark);
            font-weight: 600;
        }}

        .timer-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 0.85rem;
            transition: color 0.2s;
        }}
        .timer-btn:hover {{ color: var(--text-main); }}

        /* Étoiles du Header */
        .stars-counter {{
            background: #fef3c7;
            border: 1px solid #fde68a;
            padding: 6px 14px;
            border-radius: 30px;
            font-weight: 700;
            color: var(--accent-gold);
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.95rem;
        }}

        .stars-row {{
            display: flex;
            gap: 3px;
            font-size: 1.15rem;
        }}

        .star-item {{
            color: #cbd5e1;
            transition: transform 0.3s ease, color 0.3s ease;
        }}
        .star-item.unlocked {{
            color: var(--accent-gold);
            text-shadow: 0 0 6px rgba(217, 119, 6, 0.4);
            transform: scale(1.15);
        }}

        /* Barre de progression globale */
        .progress-bar-container {{
            width: 100%;
            height: 4px;
            background: #e2e8f0;
            position: absolute;
            bottom: 0;
            left: 0;
        }}
        .progress-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-42), #059669);
            width: 0%;
            transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        /* Container Principal */
        .main-wrapper {{
            max-width: 1050px;
            margin: 25px auto;
            padding: 0 20px;
        }}

        /* Intro Banner */
        .hero-banner {{
            background: #ffffff;
            border: 1px solid var(--border-card);
            border-top: 4px solid var(--accent-42);
            border-radius: 12px;
            padding: 24px 30px;
            margin-bottom: 25px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .hero-banner h2 {{
            font-size: 1.5rem;
            margin-bottom: 6px;
            color: var(--text-main);
        }}

        .hero-banner p {{
            color: var(--text-light);
            font-size: 1rem;
            margin-bottom: 16px;
        }}

        .rules-badge-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }}

        .rule-card {{
            background: #f8fafc;
            border: 1px solid var(--border-card);
            border-radius: 8px;
            padding: 14px 18px;
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }}

        .rule-card .rule-icon {{
            font-size: 1.5rem;
            line-height: 1;
        }}

        .rule-card strong {{
            display: block;
            color: var(--accent-42-dark);
            font-size: 0.92rem;
            margin-bottom: 4px;
        }}

        .rule-card span {{
            font-size: 0.85rem;
            color: var(--text-light);
        }}

        /* Fiche de Survie Terminal */
        .survival-box {{
            background: #ffffff;
            border: 1px solid var(--border-card);
            border-radius: 10px;
            padding: 16px 22px;
            margin-bottom: 25px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
        }}

        .survival-title {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            user-select: none;
        }}

        .survival-title h3 {{
            font-size: 1.05rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .survival-content {{
            margin-top: 15px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 12px;
            font-size: 0.9rem;
        }}

        .survival-item {{
            background: #f8fafc;
            padding: 10px 14px;
            border-radius: 6px;
            border: 1px solid var(--border-card);
            border-left: 3px solid var(--accent-42);
        }}

        .survival-item code {{
            font-family: var(--font-mono);
            color: #0369a1;
            font-size: 0.92rem;
            font-weight: 600;
            display: block;
            margin-bottom: 2px;
        }}

        .survival-item span {{
            color: var(--text-light);
            font-size: 0.82rem;
        }}

        /* Cartes de Niveau (CTF Cards) */
        .level-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 12px;
            margin-bottom: 25px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
        }}

        .level-card.active {{
            border-color: var(--accent-42);
            box-shadow: 0 4px 20px rgba(0, 186, 188, 0.15);
        }}

        .level-card.completed {{
            border-color: #a7f3d0;
        }}

        .level-card.locked {{
            opacity: 0.75;
            background: #fafafa;
        }}

        .level-card-header {{
            background: var(--bg-card-header);
            padding: 16px 22px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-card);
        }}

        .level-card-title {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .level-badge {{
            background: var(--accent-42);
            color: #042b2b;
            font-weight: 700;
            font-size: 0.85rem;
            padding: 4px 12px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .level-card.completed .level-badge {{
            background: var(--accent-green);
            color: #fff;
        }}

        .level-card.locked .level-badge {{
            background: #e2e8f0;
            color: #64748b;
        }}

        .level-card-title h3 {{
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .level-status-pill {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 4px 12px;
            border-radius: 20px;
        }}

        .status-locked {{
            background: #fee2e2;
            color: #b91c1c;
            border: 1px solid #fecaca;
        }}

        .status-active {{
            background: #e0f2fe;
            color: #0369a1;
            border: 1px solid #bae6fd;
            animation: pulse-glow 2s infinite;
        }}

        .status-completed {{
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #bbf7d0;
        }}

        @keyframes pulse-glow {{
            0%, 100% {{ box-shadow: 0 0 4px rgba(0, 186, 188, 0.2); }}
            50% {{ box-shadow: 0 0 10px rgba(0, 186, 188, 0.4); }}
        }}

        .level-card-body {{
            padding: 24px;
            position: relative;
        }}

        /* Placeholders de chiffrement (Zero-Knowledge) */
        .locked-vault {{
            padding: 35px 20px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            background: #f8fafc;
            border-radius: 8px;
            border: 1.5px dashed #cbd5e1;
        }}

        .vault-icon {{
            font-size: 2.2rem;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        }}

        .locked-vault h4 {{
            font-size: 1.15rem;
            color: #b91c1c;
            letter-spacing: 0.5px;
        }}

        .locked-vault p {{
            font-size: 0.92rem;
            color: var(--text-muted);
            max-width: 480px;
            line-height: 1.5;
        }}

        .vault-badge {{
            font-family: var(--font-mono);
            font-size: 0.78rem;
            background: #ffffff;
            color: #64748b;
            padding: 4px 10px;
            border-radius: 4px;
            border: 1px solid #cbd5e1;
        }}

        /* Typo et Blocs */
        p.desc {{
            color: var(--text-light);
            margin-bottom: 16px;
            font-size: 1rem;
        }}

        ul.step-list {{
            list-style: none;
            margin: 16px 0;
        }}

        ul.step-list li {{
            position: relative;
            padding-left: 28px;
            margin-bottom: 12px;
            color: var(--text-main);
            font-size: 0.95rem;
        }}

        ul.step-list li::before {{
            content: "▶";
            position: absolute;
            left: 0;
            color: var(--accent-42-dark);
            font-size: 0.8rem;
            top: 2px;
        }}

        code.inline {{
            font-family: var(--font-mono);
            background: #f1f5f9;
            color: #0369a1;
            border: 1px solid #cbd5e1;
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 0.9em;
            font-weight: 600;
        }}

        /* Bloc de code avec barre d'outils */
        .code-container {{
            position: relative;
            background: var(--code-bg);
            border: 1px solid #334155;
            border-radius: 8px;
            margin: 16px 0 24px 0;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        }}

        .code-header {{
            background: #0f172a;
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            font-size: 0.85rem;
            color: #94a3b8;
            font-family: var(--font-mono);
        }}

        .copy-btn {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #475569;
            color: #e2e8f0;
            padding: 4px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8rem;
            transition: all 0.2s;
        }}
        .copy-btn:hover {{
            background: var(--accent-42);
            color: #000;
            border-color: var(--accent-42);
        }}

        pre {{
            padding: 16px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 0.88rem;
            line-height: 1.5;
            color: #f8fafc;
        }}

        .code-comment {{ color: #94a3b8; font-style: italic; }}
        .code-keyword {{ color: #f472b6; font-weight: 600; }}
        .code-highlight {{
            background: rgba(245, 158, 11, 0.25);
            color: #fde047;
            padding: 1px 4px;
            border-radius: 3px;
            font-weight: 600;
        }}

        /* Bouton Lien Action */
        .action-link-btn {{
            display: inline-block;
            background: #00babc;
            color: #042b2b;
            text-decoration: none;
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 6px;
            margin-top: 6px;
            transition: background 0.2s, transform 0.1s;
        }}
        .action-link-btn:hover {{
            background: #009ea0;
            transform: translateY(-1px);
        }}

        /* Callouts */
        .rules-callout {{
            background: #f0fdfa;
            border: 1px solid #ccfbf1;
            border-left: 4px solid var(--accent-42);
            padding: 14px 18px;
            border-radius: 6px;
            margin-bottom: 18px;
        }}
        .rules-callout strong {{
            color: var(--accent-42-dark);
            display: block;
            margin-bottom: 4px;
        }}
        .rules-callout span {{
            font-size: 0.92rem;
            color: var(--text-light);
        }}

        .mentor-callout {{
            background: #fffbeb;
            border: 1px solid #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 16px 20px;
            border-radius: 6px;
            margin-bottom: 20px;
        }}
        .mentor-callout strong {{
            color: #b45309;
            display: block;
            margin-bottom: 6px;
            font-size: 1.05rem;
        }}

        /* Widget d'Indices & Pénalités (Mode Collège / Lycée) */
        .hint-widget {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 18px 0;
        }}

        .hint-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .hint-btn {{
            background: #fff;
            border: 1.5px solid #cbd5e1;
            color: #334155;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .hint-btn:hover {{
            border-color: #f59e0b;
            color: #b45309;
            background: #fffbeb;
        }}
        .hint-btn.warning {{
            border-color: #ef4444;
            color: #dc2626;
            background: #fef2f2;
        }}

        .hint-points-status {{
            font-size: 0.82rem;
            font-weight: 700;
            color: #64748b;
            font-family: var(--font-mono);
        }}

        .hint-box {{
            margin-top: 10px;
            padding: 12px 14px;
            background: #fffdf5;
            border: 1px solid #fef3c7;
            border-left: 3px solid #f59e0b;
            border-radius: 4px;
            font-size: 0.9rem;
            color: #78350f;
            line-height: 1.5;
        }}

        /* Boîte de validation CTF */
        .validation-box {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 18px 20px;
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .validation-box.mentor-box {{
            border-color: #fde68a;
            background: #fffdf5;
        }}

        .validation-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .validation-title {{
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--accent-42-dark);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .mentor-box .validation-title {{
            color: #b45309;
        }}

        .mentor-tag {{
            font-size: 0.8rem;
            color: #b45309;
            font-weight: 700;
            background: #fef3c7;
            padding: 2px 8px;
            border-radius: 12px;
            border: 1px solid #fde68a;
        }}

        .validation-hint {{
            font-size: 0.88rem;
            color: var(--text-muted);
        }}

        .validation-form {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .validation-input {{
            flex: 1;
            min-width: 260px;
            background: #ffffff;
            border: 1.5px solid #cbd5e1;
            border-radius: 6px;
            padding: 12px 16px;
            font-family: var(--font-mono);
            font-size: 0.95rem;
            color: var(--text-main);
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }}

        .validation-input:focus {{
            border-color: var(--accent-42);
            box-shadow: 0 0 0 3px rgba(0, 186, 188, 0.15);
        }}

        .validate-btn {{
            background: var(--accent-42);
            color: #042b2b;
            border: none;
            border-radius: 6px;
            padding: 12px 24px;
            font-weight: 700;
            font-family: var(--font-family);
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .validate-btn:hover {{
            background: var(--accent-42-hover);
            transform: translateY(-1px);
            box-shadow: 0 4px 10px rgba(0, 186, 188, 0.25);
        }}

        .mentor-btn {{
            background: #f59e0b;
            color: #000;
        }}
        .mentor-btn:hover {{
            background: #d97706;
            color: #fff;
            box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3);
        }}

        .feedback-msg {{
            font-size: 0.88rem;
            display: none;
            align-items: center;
            gap: 6px;
        }}

        .feedback-msg.error {{
            display: flex;
            color: #b91c1c;
            font-weight: 600;
        }}

        .feedback-msg.success {{
            display: flex;
            color: #15803d;
            font-weight: 600;
        }}

        /* Modal de Victoire Finale */
        .victory-modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(6px);
            z-index: 999;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .victory-card {{
            background: #ffffff;
            border: 2px solid #f59e0b;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            border-radius: 16px;
            max-width: 580px;
            width: 100%;
            padding: 40px;
            text-align: center;
            position: relative;
            animation: modal-pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}

        @keyframes modal-pop {{
            0% {{ transform: scale(0.85); opacity: 0; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}

        .victory-stars {{
            font-size: 2.4rem;
            color: #f59e0b;
            margin-bottom: 12px;
            letter-spacing: 4px;
        }}

        .victory-card h2 {{
            font-size: 2rem;
            color: var(--text-main);
            margin-bottom: 10px;
        }}

        .victory-card p {{
            color: var(--text-light);
            font-size: 1.05rem;
            margin-bottom: 24px;
            line-height: 1.6;
        }}

        .victory-btn {{
            background: linear-gradient(135deg, var(--accent-42), #059669);
            color: #ffffff;
            font-weight: 700;
            font-size: 1rem;
            padding: 12px 32px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            transition: transform 0.2s;
        }}
        .victory-btn:hover {{ transform: scale(1.04); }}

        /* Canvas de Confettis */
        #confetti-canvas {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1000;
        }}

        /* Footer */
        .site-footer {{
            max-width: 1050px;
            margin: 40px auto 0 auto;
            padding: 20px;
            border-top: 1px solid var(--border-card);
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .reset-btn {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: var(--text-muted);
            padding: 5px 14px;
            border-radius: 4px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .reset-btn:hover {{ color: #b91c1c; border-color: #b91c1c; }}

        @media (max-width: 768px) {{
            .navbar-container {{ flex-direction: column; align-items: flex-start; }}
            .stats-section {{ width: 100%; justify-content: space-between; }}
            .validation-form {{ flex-direction: column; }}
            .validate-btn {{ width: 100%; justify-content: center; }}
        }}
    </style>
</head>
<body>

    <canvas id="confetti-canvas"></canvas>

    <!-- Top Sticky Bar (Clair & Épuré) -->
    <header class="top-navbar">
        <div class="navbar-container">
            <div class="brand-section">
                <img src="42.png" alt="42 Logo" class="logo-42-img">
                <div class="brand-text">
                    <h1>CHASSE AU TRÉSOR</h1>
                    <p>Découverte & Peer-Learning — 1 Heure Chrono</p>
                </div>
            </div>

            <div class="stats-section">
                <!-- Statut de Mode (Fixé par l'Admin) -->
                <div class="mode-badge-box" id="mode-badge-box" title="Mode d'atelier fixé par l'organisateur">
                    <span id="mode-badge-icon">🎓</span>
                    <span id="mode-badge-text">Mode Lycée (Intermédiaire)</span>
                    <button class="admin-gear-btn" id="admin-gear-btn" onclick="openAdminModal()" title="Panneau Organisateur (Visible sur la machine hôte uniquement)">⚙️ Admin</button>
                </div>

                <!-- Score Points (Visible uniquement si Mode Collège) -->
                <div class="score-counter" id="score-counter-box" style="display: none;" title="Score total de la mission">
                    <span>🏆</span>
                    <span id="score-display">0 / 500 pts</span>
                </div>

                <!-- Chronomètre -->
                <div class="timer-box" title="Temps restant pour l'activité">
                    <span>⏱️</span>
                    <span id="timer-display">60:00</span>
                </div>

                <!-- Étoiles débloquées -->
                <div class="stars-counter">
                    <span id="stars-text">0 / 5</span>
                    <div class="stars-row" id="stars-row">
                        <span class="star-item" id="star-1">★</span>
                        <span class="star-item" id="star-2">★</span>
                        <span class="star-item" id="star-3">★</span>
                        <span class="star-item" id="star-4">★</span>
                        <span class="star-item" id="star-5">★</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="progress-bar-container">
            <div class="progress-bar-fill" id="progress-bar"></div>
        </div>
    </header>

    <main class="main-wrapper">

        <!-- Bannière d'introduction -->
        <section class="hero-banner">
            <h2>Bienvenue dans le modèle 42 🚀</h2>
            <p>Ici, pas de professeurs, pas d'estrade, pas de cours magistraux. Vous êtes aux commandes de votre apprentissage, en binôme ou en équipe.</p>
            
            <div class="rules-badge-grid">
                <div class="rule-card">
                    <div class="rule-icon">🧠</div>
                    <div>
                        <strong>Règle n°1 : L'Autonomie Totale</strong>
                        <span>Cherchez sur internet, lisez la documentation, testez, cassez votre code et recommencez.</span>
                    </div>
                </div>
                <div class="rule-card">
                    <div class="rule-icon">🤝</div>
                    <div>
                        <strong>Règle n°2 : Le Peer-Learning (Entraide)</strong>
                        <span>Si vous bloquez, demandez à vos voisins. Mais <u>interdiction absolue de toucher au clavier</u> d'une autre équipe !</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Fiche de Survie Terminal -->
        <section class="survival-box">
            <div class="survival-title" onclick="toggleSurvival()">
                <h3>🛠️ Boîte à Outils Terminal (Ubuntu 24)</h3>
                <span id="survival-toggle-icon">▼</span>
            </div>
            <div class="survival-content" id="survival-content">
                <div class="survival-item">
                    <code>Ctrl + Alt + T</code>
                    <span>Ouvrir un nouveau terminal sous Ubuntu</span>
                </div>
                <div class="survival-item">
                    <code>ls -la</code>
                    <span>Lister tous les fichiers (y compris cachés avec .)</span>
                </div>
                <div class="survival-item">
                    <code>cd dossier</code>
                    <span>Entrer dans un sous-dossier (<code class="inline">cd ..</code> pour reculer)</span>
                </div>
                <div class="survival-item">
                    <code>cat nom_fichier</code>
                    <span>Afficher le contenu d'un fichier texte</span>
                </div>
                <div class="survival-item">
                    <code>python3 script.py</code>
                    <span>Exécuter un script Python 3</span>
                </div>
                <div class="survival-item">
                    <code>python3 moulinette.py</code>
                    <span>Lancer la Moulinette de validation 42</span>
                </div>
            </div>
        </section>

        <!-- ============================================================== -->
        <!-- NIVEAU 1 : Visible dès le départ (Exercice révisé) -->
        <!-- ============================================================== -->
        <article class="level-card active" id="card-level-1">
            <div class="level-card-header">
                <div class="level-card-title">
                    <span class="level-badge">Niveau 1</span>
                    <h3>⭐ Exploration du Terminal & Arborescence (Bash)</h3>
                </div>
                <span class="level-status-pill status-active" id="badge-level-1">⚡ En cours</span>
            </div>

            <div class="level-card-body" id="body-level-1">
                <p class="desc">Un dossier nommé <code class="inline">mission_42</code> a été préparé sur votre machine. Votre premier objectif est de fouiller le dossier <code class="inline">mission_42/archives</code> pour retrouver la <strong>clé de sécurité système</strong> permettant de débloquer le Niveau 2.</p>

                <ul class="step-list">
                    <li>Ouvrez votre terminal avec le raccourci clavier.</li>
                    <li>Rendez-vous dans le dossier <code class="inline">~/Desktop/mission_42</code>.</li>
                    <li>Fouillez l'arborescence du dossier à l'aide des commandes de navigation de votre boîte à outils.</li>
                    <li>Récupérez la clé de sécurité et validez le niveau.</li>
                </ul>

                <!-- WIDGET D'INDICE (MODE COLLÈGE / LYCÉE) -->
                <div class="hint-widget" id="hint-widget-1">
                    <div class="hint-header">
                        <button class="hint-btn" id="hint-btn-1" onclick="requestHint(1)">💡 Demander un indice (-50 pts)</button>
                        <span class="hint-points-status" id="hint-pts-1">Valeur : 100 / 100 pts</span>
                    </div>
                    <div class="hint-box" id="hint-box-1" style="display: none;"></div>
                </div>

                <div class="validation-box">
                    <div class="validation-header">
                        <span class="validation-title">🔑 Validation du Niveau 1</span>
                    </div>
                    <p class="validation-hint">Collez la clé de sécurité trouvée dans le dossier archives :</p>
                    <div class="validation-form">
                        <input type="text" class="validation-input" id="input-level-1" placeholder="Entrez la clé de sécurité trouvée..." autocomplete="off">
                        <button class="validate-btn" onclick="validateLevel1()">Valider l'Étoile 1 ⭐</button>
                    </div>
                    <div class="feedback-msg" id="feedback-level-1"></div>
                </div>
            </div>
        </article>

        <!-- ============================================================== -->
        <!-- NIVEAU 2 : Chiffré (Zero-Knowledge) -->
        <!-- ============================================================== -->
        <article class="level-card locked" id="card-level-2">
            <div class="level-card-header">
                <div class="level-card-title">
                    <span class="level-badge">Niveau 2</span>
                    <h3>⭐⭐ L'Envers du Décor Web (Inspecteur F12)</h3>
                </div>
                <span class="level-status-pill status-locked" id="badge-level-2">🔒 Verrouillé</span>
            </div>

            <div class="level-card-body" id="body-level-2">
                <div class="locked-vault">
                    <div class="vault-icon">🔒</div>
                    <h4>CONTENU DU NIVEAU 2 CHIFFRÉ</h4>
                    <p>Ce niveau est protégé par un chiffrement cryptographique. Validez le Niveau 1 pour calculer la clé et révéler l'épreuve.</p>
                    <span class="vault-badge">PAYLOAD: SHA256-CTR ZERO-KNOWLEDGE</span>
                </div>
            </div>
        </article>

        <!-- ============================================================== -->
        <!-- NIVEAU 3 : Chiffré (Zero-Knowledge) -->
        <!-- ============================================================== -->
        <article class="level-card locked" id="card-level-3">
            <div class="level-card-header">
                <div class="level-card-title">
                    <span class="level-badge">Niveau 3</span>
                    <h3>⭐⭐⭐ Cryptanalyse & Brute Force César (Python)</h3>
                </div>
                <span class="level-status-pill status-locked" id="badge-level-3">🔒 Verrouillé</span>
            </div>

            <div class="level-card-body" id="body-level-3">
                <div class="locked-vault">
                    <div class="vault-icon">🔒</div>
                    <h4>CONTENU DU NIVEAU 3 CHIFFRÉ</h4>
                    <p>Ce niveau est protégé par un chiffrement cryptographique. Validez le Niveau 2 pour calculer la clé et révéler l'épreuve.</p>
                    <span class="vault-badge">PAYLOAD: SHA256-CTR ZERO-KNOWLEDGE</span>
                </div>
            </div>
        </article>

        <!-- ============================================================== -->
        <!-- NIVEAU 4 : Chiffré (Zero-Knowledge) -->
        <!-- ============================================================== -->
        <article class="level-card locked" id="card-level-4">
            <div class="level-card-header">
                <div class="level-card-title">
                    <span class="level-badge">Niveau 4</span>
                    <h3>⭐⭐⭐⭐ Coder la Machine à Sous (Casino 42)</h3>
                </div>
                <span class="level-status-pill status-locked" id="badge-level-4">🔒 Verrouillé</span>
            </div>

            <div class="level-card-body" id="body-level-4">
                <div class="locked-vault">
                    <div class="vault-icon">🔒</div>
                    <h4>CONTENU DU NIVEAU 4 CHIFFRÉ</h4>
                    <p>Ce niveau est protégé par un chiffrement cryptographique. Déchiffrez le code au Niveau 3 pour accéder au Casino de 42.</p>
                    <span class="vault-badge">PAYLOAD: SHA256-CTR ZERO-KNOWLEDGE</span>
                </div>
            </div>
        </article>

        <!-- ============================================================== -->
        <!-- NIVEAU 5 : Chiffré (Zero-Knowledge) -->
        <!-- ============================================================== -->
        <article class="level-card locked" id="card-level-5">
            <div class="level-card-header">
                <div class="level-card-title">
                    <span class="level-badge" style="background: var(--accent-gold); color: #000;">Niveau 5 (Ultime)</span>
                    <h3>⭐⭐⭐⭐⭐ L'Épreuve du Peer-Learning & Validation Mentor</h3>
                </div>
                <span class="level-status-pill status-locked" id="badge-level-5">🔒 Verrouillé</span>
            </div>

            <div class="level-card-body" id="body-level-5">
                <div class="locked-vault">
                    <div class="vault-icon">🔒</div>
                    <h4>ÉPREUVE ULTIME CHIFFRÉE</h4>
                    <p>Terminez la machine à sous au Niveau 4 pour débloquer le protocole de Peer-Learning.</p>
                    <span class="vault-badge">PAYLOAD: SHA256-CTR ZERO-KNOWLEDGE</span>
                </div>
            </div>
        </article>

        <!-- Footer -->
        <footer class="site-footer">
            <div>
                <strong>ÉCOLE 42</strong> — La Tech Pour Toutes — Édition Novembre 2026
            </div>
            <div>
                <button class="reset-btn" onclick="confirmResetProgress()">🔄 Réinitialiser la progression</button>
            </div>
        </footer>

    </main>

    <!-- Modal Victoire Finale -->
    <div class="victory-modal" id="victory-modal">
        <div id="victory-modal-content"></div>
    </div>

    <!-- Modal Admin (Uniquement accessible sur le poste hôte/serveur) -->
    <div class="victory-modal" id="admin-modal" style="display: none; background: rgba(15, 23, 42, 0.75);">
        <div class="victory-card" style="max-width: 480px; text-align: left; padding: 28px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.25rem; color: #0f172a;">🛡️ Panneau Organisateur (Admin)</h3>
                <button onclick="closeAdminModal()" style="background: none; border: none; font-size: 1.4rem; cursor: pointer; color: #64748b;">✕</button>
            </div>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 20px;">
                Basculez le mode d'atelier en direct pour <strong>tous les postes de la salle</strong> :
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px;">
                <button class="admin-choice-card" id="admin-card-intermediate" onclick="setServerMode('intermediate')">
                    <span style="font-size: 1.6rem;">🎓</span>
                    <div>
                        <strong style="display: block; font-size: 1rem; color: #0f172a;">Mode Lycée (Intermédiaire)</strong>
                        <span style="font-size: 0.82rem; color: #64748b;">Esprit 42 pur : Aucun indice pré-mâché, 100% peer-learning.</span>
                    </div>
                </button>
                <button class="admin-choice-card" id="admin-card-easy" onclick="setServerMode('easy')">
                    <span style="font-size: 1.6rem;">🎒</span>
                    <div>
                        <strong style="display: block; font-size: 1rem; color: #0f172a;">Mode Collège (Facile)</strong>
                        <span style="font-size: 0.82rem; color: #64748b;">Indices progressifs (-50 pts puis 0 pt) et score sur 500 pts.</span>
                    </div>
                </button>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span id="admin-sync-status" style="font-size: 0.8rem; color: #059669;">✓ Connecté au serveur 42</span>
                <button class="validate-btn" onclick="closeAdminModal()" style="padding: 8px 18px; font-size: 0.9rem;">Fermer</button>
            </div>
        </div>
    </div>

    <!-- MOTEUR CRYPTOGRAPHIQUE, SYSTÈME D'INDICES & SCORING -->
    <script>
        // ==============================================================================
        // PAYLOADS CHIFFRÉS ZERO-KNOWLEDGE (Impossible de les lire sans les clés !)
        // ==============================================================================
        const ENCRYPTED_PAYLOADS = {payloads_js};

        // Suivi des indices et des scores par niveau
        let sessionData = {{
            difficultyMode: 'intermediate',
            keys: {{}},
            hintsUsed: {{ 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }},
            levelScores: {{ 1: 100, 2: 100, 3: 100, 4: 100, 5: 100 }},
            earnedScores: {{ 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }}
        }};

        // ------------------------------------------------------------------------------
        // Fonctions Cryptographiques Standards (SHA256 & Stream Cipher SHA256-CTR)
        // ------------------------------------------------------------------------------
        function sha256(ascii) {{
            function rightRotate(value, amount) {{ return (value >>> amount) | (value << (32 - amount)); }}
            var mathPow = Math.pow, maxWord = mathPow(2, 32), lengthProperty = 'length', i, j, result = '', words = [];
            var asciiBitLength = ascii[lengthProperty] * 8, hash = sha256.h = sha256.h || [], k = sha256.k = sha256.k || [];
            var primeCounter = k[lengthProperty], isComposite = {{}};
            for (var candidate = 2; primeCounter < 64; candidate++) {{
                if (!isComposite[candidate]) {{
                    for (i = 0; i < 313; i += candidate) isComposite[i] = candidate;
                    hash[primeCounter] = (mathPow(candidate, .5) * maxWord) | 0;
                    k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
                }}
            }}
            ascii += '\\x80';
            while (ascii[lengthProperty] % 64 - 56) ascii += '\\x00';
            for (i = 0; i < ascii[lengthProperty]; i++) {{
                j = ascii.charCodeAt(i);
                if (j >> 8) return;
                words[i >> 2] |= j << ((3 - i) % 4) * 8;
            }}
            words[words[lengthProperty]] = ((asciiBitLength / maxWord) | 0);
            words[words[lengthProperty]] = (asciiBitLength);
            for (j = 0; j < words[lengthProperty];) {{
                var w = words.slice(j, j += 16), oldHash = hash;
                hash = hash.slice(0, 8);
                for (i = 0; i < 64; i++) {{
                    var i2 = i + j, w15 = w[i - 15], w2 = w[i - 2], a = hash[0], e = hash[4];
                    var temp1 = hash[7] + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) + ((e & hash[5]) ^ ((~e) & hash[6])) + k[i] + (w[i] = (i < 16) ? w[i] : (w[i - 16] + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3)) + w[i - 7] + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10))) | 0);
                    var temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) + ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
                    hash = [(temp1 + temp2) | 0].concat(hash);
                    hash[4] = (hash[4] + temp1) | 0;
                }}
                for (i = 0; i < 8; i++) hash[i] = (hash[i] + oldHash[i]) | 0;
            }}
            for (i = 0; i < 8; i++) {{
                for (j = 3; j + 1; j--) {{
                    var b = (hash[i] >> (j * 8)) & 255;
                    result += ((b < 16) ? 0 : '') + b.toString(16);
                }}
            }}
            return result;
        }}

        function hexToBytes(hex) {{
            const bytes = [];
            for (let c = 0; c < hex.length; c += 2) bytes.push(parseInt(hex.substr(c, 2), 16));
            return bytes;
        }}

        function base64ToBytes(b64) {{
            const binStr = atob(b64);
            const bytes = new Uint8Array(binStr.length);
            for (let i = 0; i < binStr.length; i++) bytes[i] = binStr.charCodeAt(i);
            return bytes;
        }}

        function bytesToUtf8(bytes) {{
            return new TextDecoder('utf-8').decode(bytes);
        }}

        function decryptPayload(cipherB64, keyCandidate) {{
            try {{
                const ct = base64ToBytes(cipherB64);
                const pt = new Uint8Array(ct.length);
                let counter = 0, ptIdx = 0;
                while (ptIdx < ct.length) {{
                    const h = sha256(keyCandidate + ':' + counter);
                    const hBytes = hexToBytes(h);
                    for (let i = 0; i < hBytes.length && ptIdx < ct.length; i++) {{
                        pt[ptIdx] = ct[ptIdx] ^ hBytes[i];
                        ptIdx++;
                    }}
                    counter++;
                }}
                const text = bytesToUtf8(pt);
                if (text.startsWith('42_OK::')) return text.substring(7);
            }} catch (e) {{}}
            return null;
        }}

        // ------------------------------------------------------------------------------
        // Gestion des Indices Sécurisés (Fournis par le Serveur Central uniquement)
        // ------------------------------------------------------------------------------
        async function requestHint(lvl) {{
            const currentHits = sessionData.hintsUsed[lvl] || 0;
            const nextStep = currentHits + 1;
            if (nextStep > 2) return;

            if (nextStep === 2) {{
                if (!confirm("⚠️ Attention : Afficher la solution directe vous attribuera 0 point pour cet exercice. Voulez-vous continuer ?")) {{
                    return;
                }}
            }}

            const box = document.getElementById(`hint-box-${{lvl}}`);
            const btn = document.getElementById(`hint-btn-${{lvl}}`);
            const ptsLabel = document.getElementById(`hint-pts-${{lvl}}`);

            try {{
                const resp = await fetch(`/api/hint?level=${{lvl}}&step=${{nextStep}}`);
                const data = await resp.json();
                if (!resp.ok || data.error) {{
                    alert(data.error || "Les indices sont désactivés pour cet atelier.");
                    return;
                }}

                if (nextStep === 1) {{
                    sessionData.hintsUsed[lvl] = 1;
                    sessionData.levelScores[lvl] = 50;
                    box.innerHTML = data.hint;
                    box.style.display = "block";
                    btn.innerHTML = "🚨 Demander la solution directe (0 pt sur l'épreuve)";
                    btn.className = "hint-btn warning";
                    ptsLabel.innerText = "Valeur : 50 / 100 pts";
                    ptsLabel.style.color = "#d97706";
                }} else if (nextStep === 2) {{
                    sessionData.hintsUsed[lvl] = 2;
                    sessionData.levelScores[lvl] = 0;
                    box.innerHTML += "<br><br>" + data.hint;
                    btn.disabled = true;
                    btn.style.opacity = "0.5";
                    btn.style.cursor = "default";
                    btn.innerText = "Solution affichée (0 pt)";
                    ptsLabel.innerText = "Valeur : 0 / 100 pts";
                    ptsLabel.style.color = "#dc2626";
                }}
                saveSession();
            }} catch (e) {{
                alert("Erreur de communication avec le serveur d'indices.");
            }}
        }}

        function restoreHintUI(lvl) {{
            const currentHits = sessionData.hintsUsed[lvl] || 0;
            const box = document.getElementById(`hint-box-${{lvl}}`);
            const btn = document.getElementById(`hint-btn-${{lvl}}`);
            const ptsLabel = document.getElementById(`hint-pts-${{lvl}}`);
            if (!box || !btn || !ptsLabel) return;

            if (currentHits === 1) {{
                btn.innerHTML = "🚨 Demander la solution directe (0 pt sur l'épreuve)";
                btn.className = "hint-btn warning";
                ptsLabel.innerText = "Valeur : 50 / 100 pts";
                ptsLabel.style.color = "#d97706";
                fetch(`/api/hint?level=${{lvl}}&step=1`).then(r => r.json()).then(d => {{
                    if (d.hint) {{ box.innerHTML = d.hint; box.style.display = "block"; }}
                }}).catch(() => {{}});
            }} else if (currentHits >= 2) {{
                btn.disabled = true;
                btn.style.opacity = "0.5";
                btn.style.cursor = "default";
                btn.innerText = "Solution affichée (0 pt)";
                ptsLabel.innerText = "Valeur : 0 / 100 pts";
                ptsLabel.style.color = "#dc2626";
                Promise.all([
                    fetch(`/api/hint?level=${{lvl}}&step=1`).then(r => r.json()),
                    fetch(`/api/hint?level=${{lvl}}&step=2`).then(r => r.json())
                ]).then(([d1, d2]) => {{
                    if (d1.hint && d2.hint) {{
                        box.innerHTML = d1.hint + "<br><br>" + d2.hint;
                        box.style.display = "block";
                    }}
                }}).catch(() => {{}});
            }}
        }}

        // ------------------------------------------------------------------------------
        // État de la session & Contrôle Admin Centralisé
        // ------------------------------------------------------------------------------
        function openAdminModal() {{
            document.getElementById('admin-modal').style.display = 'flex';
        }}
        function closeAdminModal() {{
            document.getElementById('admin-modal').style.display = 'none';
        }}

        async function setServerMode(mode) {{
            try {{
                const resp = await fetch('/api/mode', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ mode: mode }})
                }});
                const data = await resp.json();
                if (resp.ok) {{
                    applyDifficultyModeUI(mode);
                    closeAdminModal();
                }} else {{
                    alert(data.error || "Action refusée par le serveur.");
                }}
            }} catch (e) {{
                alert("Impossible de joindre le serveur.");
            }}
        }}

        function applyDifficultyModeUI(mode) {{
            sessionData.difficultyMode = mode;
            const isEasy = (mode === 'easy');

            const badgeIcon = document.getElementById('mode-badge-icon');
            const badgeText = document.getElementById('mode-badge-text');
            if (badgeIcon && badgeText) {{
                badgeIcon.innerText = isEasy ? "🎒" : "🎓";
                badgeText.innerText = isEasy ? "Mode Collège (Facile)" : "Mode Lycée (Intermédiaire)";
            }}

            const cardInter = document.getElementById('admin-card-intermediate');
            const cardEasy = document.getElementById('admin-card-easy');
            if (cardInter && cardEasy) {{
                if (isEasy) {{
                    cardEasy.classList.add('active');
                    cardInter.classList.remove('active');
                }} else {{
                    cardInter.classList.add('active');
                    cardEasy.classList.remove('active');
                }}
            }}

            const scoreBox = document.getElementById('score-counter-box');
            if (scoreBox) {{
                scoreBox.style.display = isEasy ? 'flex' : 'none';
            }}

            for (let i = 1; i <= 5; i++) {{
                const widget = document.getElementById(`hint-widget-${{i}}`);
                if (widget) {{
                    widget.style.display = isEasy ? 'block' : 'none';
                }}
            }}
        }}

        async function syncServerStatus() {{
            try {{
                const resp = await fetch('/api/status');
                if (resp.ok) {{
                    const data = await resp.json();
                    if (data.mode && data.mode !== sessionData.difficultyMode) {{
                        applyDifficultyModeUI(data.mode);
                    }}
                }}
            }} catch (e) {{}}
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            const isHostAdmin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1');
            const adminBtn = document.getElementById('admin-gear-btn');
            if (adminBtn && isHostAdmin) {{
                adminBtn.style.display = 'inline-block';
            }}

            loadSession();
            startTimer();
            syncServerStatus();
            setInterval(syncServerStatus, 3500);
        }});

        function saveSession() {{
            localStorage.setItem('42_session_v2', JSON.stringify(sessionData));
        }}

        function loadSession() {{
            const saved = localStorage.getItem('42_session_v2');
            if (saved) {{
                try {{
                    const parsed = JSON.parse(saved);
                    sessionData = Object.assign(sessionData, parsed);
                }} catch (e) {{}}
            }}
            applyDifficultyModeUI(sessionData.difficultyMode || 'intermediate');
            restoreAllUnlocked();
        }}

        async function confirmResetProgress() {{
            if (confirm("Réinitialiser toute votre progression et score à zéro ?")) {{
                try {{
                    await fetch('/api/reset');
                }} catch (e) {{}}
                localStorage.removeItem('42_session_v2');
                location.reload();
            }}
        }}

        function restoreAllUnlocked() {{
            let currentLevel = 1;

            restoreHintUI(1);

            // Niveau 2
            if (sessionData.keys.level2) {{
                const html2 = decryptPayload(ENCRYPTED_PAYLOADS.level2, sessionData.keys.level2);
                if (html2) {{
                    renderLevel(2, html2);
                    markLevelCompleted(1);
                    currentLevel = 2;
                    restoreHintUI(2);
                }}
            }}

            // Niveau 3 (decrypt.py débloqué)
            if (sessionData.keys.level3) {{
                fetch('/api/unlock?level=2').catch(() => {{}});
                const html3 = decryptPayload(ENCRYPTED_PAYLOADS.level3, sessionData.keys.level3);
                if (html3) {{
                    renderLevel(3, html3);
                    markLevelCompleted(2);
                    currentLevel = 3;
                    restoreHintUI(3);
                }}
            }}

            // Niveau 4 (slot_machine.py débloqué)
            if (sessionData.keys.level4) {{
                fetch('/api/unlock?level=3').catch(() => {{}});
                const html4 = decryptPayload(ENCRYPTED_PAYLOADS.level4, sessionData.keys.level4);
                if (html4) {{
                    renderLevel(4, html4);
                    markLevelCompleted(3);
                    currentLevel = 4;
                    restoreHintUI(4);
                }}
            }}

            // Niveau 5
            if (sessionData.keys.level5) {{
                const html5 = decryptPayload(ENCRYPTED_PAYLOADS.level5, sessionData.keys.level5);
                if (html5) {{
                    renderLevel(5, html5);
                    markLevelCompleted(4);
                    currentLevel = 5;
                }}
            }}

            // Victoire
            if (sessionData.keys.victory) {{
                const htmlVic = decryptPayload(ENCRYPTED_PAYLOADS.victory, sessionData.keys.victory);
                if (htmlVic) {{
                    document.getElementById('victory-modal-content').innerHTML = htmlVic;
                    markLevelCompleted(5);
                    currentLevel = 6;
                }}
            }}

            updateProgressUI(currentLevel);
        }}

        function renderLevel(lvl, html) {{
            const card = document.getElementById(`card-level-${{lvl}}`);
            const body = document.getElementById(`body-level-${{lvl}}`);
            const badge = document.getElementById(`badge-level-${{lvl}}`);

            card.className = "level-card active";
            badge.className = "level-status-pill status-active";
            badge.innerHTML = "⚡ En cours";
            body.innerHTML = html;

            const isEasy = (sessionData.difficultyMode === 'easy');
            const widget = document.getElementById(`hint-widget-${{lvl}}`);
            if (widget) {{
                widget.style.display = isEasy ? 'block' : 'none';
            }}
        }}

        function markLevelCompleted(lvl) {{
            const card = document.getElementById(`card-level-${{lvl}}`);
            const badge = document.getElementById(`badge-level-${{lvl}}`);
            card.className = "level-card completed";
            badge.className = "level-status-pill status-completed";
            badge.innerHTML = "✓ Validé";

            const input = document.getElementById(`input-level-${{lvl}}`);
            const btn = input?.parentElement?.querySelector('button');
            if (input) input.disabled = true;
            if (btn) {{
                btn.disabled = true;
                btn.style.opacity = "0.6";
                btn.style.cursor = "default";
                btn.innerText = "Étoile validée ! ✓";
            }}

            // Désactiver le widget d'indice une fois validé
            const hintBtn = document.getElementById(`hint-btn-${{lvl}}`);
            if (hintBtn) {{
                hintBtn.disabled = true;
                hintBtn.style.display = "none";
            }}
            const hintPts = document.getElementById(`hint-pts-${{lvl}}`);
            if (hintPts) {{
                hintPts.innerText = `Score gagné : ${{sessionData.earnedScores[lvl]}} / 100 pts ⭐`;
                hintPts.style.color = "#059669";
            }}
        }}

        function awardLevelScore(lvl) {{
            const earned = sessionData.levelScores[lvl] !== undefined ? sessionData.levelScores[lvl] : 100;
            sessionData.earnedScores[lvl] = earned;
            saveSession();
        }}

        function calculateTotalScore() {{
            let total = 0;
            for (let i = 1; i <= 5; i++) {{
                total += (sessionData.earnedScores[i] || 0);
            }}
            return total;
        }}

        function updateProgressUI(levelReached) {{
            const starsWon = Math.min(levelReached - 1, 5);
            document.getElementById('stars-text').innerText = `${{starsWon}} / 5`;
            document.getElementById('progress-bar').style.width = `${{(starsWon / 5) * 100}}%`;

            const totalScore = calculateTotalScore();
            document.getElementById('score-display').innerText = `${{totalScore}} / 500 pts`;

            for (let i = 1; i <= 5; i++) {{
                const starEl = document.getElementById(`star-${{i}}`);
                if (i <= starsWon) starEl.classList.add('unlocked');
                else starEl.classList.remove('unlocked');
            }}

            const finalPtsEl = document.getElementById('final-points');
            if (finalPtsEl) finalPtsEl.innerText = totalScore;
        }}

        function showFeedback(lvl, isSuccess, message) {{
            const fb = document.getElementById(`feedback-level-${{lvl}}`);
            if (!fb) return;
            fb.className = `feedback-msg ${{isSuccess ? 'success' : 'error'}}`;
            fb.innerHTML = (isSuccess ? "✓ " : "❌ ") + message;
            fb.style.display = "flex";
        }}

        function scrollToCard(id) {{
            setTimeout(() => {{
                const el = document.getElementById(id);
                if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}, 300);
        }}

        // ------------------------------------------------------------------------------
        // VALIDATEURS CLIENT-SIDE (DÉCHIFFREMENT ZERO-KNOWLEDGE RÉEL)
        // ------------------------------------------------------------------------------

        // Niveau 1 -> Déchiffre Niveau 2
        function validateLevel1() {{
            const input = document.getElementById('input-level-1').value.trim();
            if (!input) {{
                showFeedback(1, false, "Veuillez entrer une clé de sécurité.");
                return;
            }}

            const keyCandidate = input.toUpperCase();
            const decryptedHtml = decryptPayload(ENCRYPTED_PAYLOADS.level2, keyCandidate);

            if (decryptedHtml) {{
                sessionData.keys.level2 = keyCandidate;
                awardLevelScore(1);
                saveSession();
                showFeedback(1, true, `Niveau 1 validé ! (+${{sessionData.earnedScores[1]}} pts) — Niveau 2 débloqué !`);
                playAudioTone(523.25, 0.2);
                renderLevel(2, decryptedHtml);
                markLevelCompleted(1);
                updateProgressUI(2);
                scrollToCard('card-level-2');
            }} else {{
                showFeedback(1, false, "Clé incorrecte. Avez-vous bien exploré l'arborescence des archives avec 'ls -la' ?");
                playAudioTone(220, 0.3, 'sawtooth');
            }}
        }}

        // Niveau 2 -> Déchiffre Niveau 3
        function validateLevel2() {{
            const input = document.getElementById('input-level-2').value.trim().toUpperCase();
            if (!input) {{
                showFeedback(2, false, "Veuillez entrer le jeton secret.");
                return;
            }}

            const decryptedHtml = decryptPayload(ENCRYPTED_PAYLOADS.level3, input);

            if (decryptedHtml) {{
                sessionData.keys.level3 = input;
                awardLevelScore(2);
                saveSession();
                fetch('/api/unlock?level=2').catch(() => {{}});
                showFeedback(2, true, `Jeton secret validé ! (+${{sessionData.earnedScores[2]}} pts) — decrypt.py débloqué & Niveau 3 accessible !`);
                playAudioTone(587.33, 0.2);
                renderLevel(3, decryptedHtml);
                markLevelCompleted(2);
                updateProgressUI(3);
                scrollToCard('card-level-3');
            }} else {{
                showFeedback(2, false, "Jeton incorrect. Inspectez attentivement le formulaire de station.html pour trouver la clé au format W**-*NS******-**.");
                playAudioTone(220, 0.3, 'sawtooth');
            }}
        }}

        // Niveau 3 -> Déchiffre Niveau 4
        function validateLevel3() {{
            let input = document.getElementById('input-level-3').value.trim().toUpperCase();
            if (!input) {{
                showFeedback(3, false, "Veuillez entrer le message déchiffré.");
                return;
            }}

            if (input.includes('/')) {{
                input = input.split('/').pop().split('?')[0];
            }}

            const decryptedHtml = decryptPayload(ENCRYPTED_PAYLOADS.level4, input);

            if (decryptedHtml) {{
                sessionData.keys.level4 = input;
                awardLevelScore(3);
                saveSession();
                fetch('/api/unlock?level=3').catch(() => {{}});
                showFeedback(3, true, `Message déchiffré avec succès ! (+${{sessionData.earnedScores[3]}} pts) — slot_machine.py & moulinette.py débloqués !`);
                playAudioTone(659.25, 0.2);
                renderLevel(4, decryptedHtml);
                markLevelCompleted(3);
                updateProgressUI(4);
                scrollToCard('card-level-4');
            }} else {{
                showFeedback(3, false, "Message déchiffré incorrect. Lancez 'python3 decrypt.py' et cherchez la ligne lisible.");
                playAudioTone(220, 0.3, 'sawtooth');
            }}
        }}

        // Niveau 4 -> Déchiffre Niveau 5
        function validateLevel4() {{
            const input = document.getElementById('input-level-4').value.trim().toUpperCase();
            if (!input) {{
                showFeedback(4, false, "Veuillez entrer le code officiel de la Moulinette.");
                return;
            }}

            const decryptedHtml = decryptPayload(ENCRYPTED_PAYLOADS.level5, input);

            if (decryptedHtml) {{
                sessionData.keys.level5 = input;
                awardLevelScore(4);
                saveSession();
                showFeedback(4, true, `Machine à sous certifiée par la Moulinette ! (+${{sessionData.earnedScores[4]}} pts) — Niveau 5 accessible !`);
                playAudioTone(783.99, 0.2);
                renderLevel(5, decryptedHtml);
                markLevelCompleted(4);
                updateProgressUI(5);
                scrollToCard('card-level-5');
            }} else {{
                showFeedback(4, false, "Code invalide. Lancez 'python3 moulinette.py' dans votre terminal pour faire tester votre script.");
                playAudioTone(220, 0.3, 'sawtooth');
            }}
        }}

        // Niveau 5 -> Déchiffre la Victoire Finale (Mentor uniquement)
        function validateLevel5() {{
            const input = document.getElementById('input-level-5').value.trim().toUpperCase();
            if (!input) {{
                showFeedback(5, false, "Veuillez saisir le mot de passe confidentiel.");
                return;
            }}

            const decryptedHtml = decryptPayload(ENCRYPTED_PAYLOADS.victory, input);

            if (decryptedHtml) {{
                sessionData.keys.victory = input;
                awardLevelScore(5);
                saveSession();
                showFeedback(5, true, `Authentification Mentor réussie ! (+${{sessionData.earnedScores[5]}} pts) — 5ème Étoile !`);
                playVictoryFanfare();
                markLevelCompleted(5);
                updateProgressUI(6);
                document.getElementById('victory-modal-content').innerHTML = decryptedHtml;
                const finalPts = document.getElementById('final-points');
                if (finalPts) finalPts.innerText = calculateTotalScore();
                launchConfetti();
                setTimeout(() => {{
                    document.getElementById('victory-modal').style.display = 'flex';
                }}, 700);
            }} else {{
                showFeedback(5, false, "Mot de passe Mentor incorrect. Seul un mentor 42 peut valider cette épreuve finale.");
                playAudioTone(220, 0.3, 'sawtooth');
            }}
        }}

        function closeVictoryModal() {{
            document.getElementById('victory-modal').style.display = 'none';
        }}

        function copyCode(id) {{
            const pre = document.getElementById(id);
            if (!pre) return;
            const text = pre.innerText;
            navigator.clipboard.writeText(text).then(() => {{
                const btn = pre.parentElement.querySelector('.copy-btn');
                const orig = btn.innerText;
                btn.innerText = "Copié ! ✓";
                setTimeout(() => btn.innerText = orig, 1800);
            }});
        }}

        function toggleSurvival() {{
            const content = document.getElementById('survival-content');
            const icon = document.getElementById('survival-toggle-icon');
            if (content.style.display === 'none') {{
                content.style.display = 'grid';
                icon.innerText = '▼';
            }} else {{
                content.style.display = 'none';
                icon.innerText = '▶';
            }}
        }}

        // Chronomètre 60 minutes
        let timeLeft = 60 * 60;
        let timerInterval = null;
        let isRunning = false;

        function updateTimerDisplay() {{
            const mins = Math.floor(timeLeft / 60);
            const secs = timeLeft % 60;
            document.getElementById('timer-display').innerText = 
                `${{mins.toString().padStart(2, '0')}}:${{secs.toString().padStart(2, '0')}}`;
        }}

        function toggleTimer() {{
            const btn = document.getElementById('timer-toggle-btn');
            if (isRunning) {{
                clearInterval(timerInterval);
                isRunning = false;
                if (btn) btn.innerText = '▶';
            }} else {{
                timerInterval = setInterval(() => {{
                    if (timeLeft > 0) {{
                        timeLeft--;
                        updateTimerDisplay();
                    }} else {{
                        clearInterval(timerInterval);
                        isRunning = false;
                        if (btn) btn.innerText = '▶';
                        alert("⏱️ Fin des 60 minutes ! Rassemblement pour le débrief !");
                    }}
                }}, 1000);
                isRunning = true;
                if (btn) btn.innerText = '⏸';
            }}
        }}

        function startTimer() {{
            updateTimerDisplay();
            toggleTimer();
        }}

        function resetTimer() {{
            timeLeft = 60 * 60;
            updateTimerDisplay();
        }}

        // Audio synthétisé
        function playAudioTone(freq, duration, type = 'sine') {{
            try {{
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.12, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            }} catch (e) {{}}
        }}

        function playVictoryFanfare() {{
            const notes = [523.25, 659.25, 783.99, 1046.50];
            notes.forEach((freq, idx) => {{
                setTimeout(() => playAudioTone(freq, 0.3), idx * 160);
            }});
        }}

        // Animation Confettis
        function launchConfetti() {{
            const canvas = document.getElementById('confetti-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const particles = [];
            const colors = ['#00babc', '#d97706', '#059669', '#0284c7', '#db2777'];

            for (let i = 0; i < 150; i++) {{
                particles.push({{
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height - canvas.height,
                    size: Math.random() * 8 + 4,
                    color: colors[Math.floor(Math.random() * colors.length)],
                    velX: (Math.random() - 0.5) * 4,
                    velY: Math.random() * 4 + 3,
                    tilt: Math.random() * 10
                }});
            }}

            let frame = 0;
            function render() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles.forEach(p => {{
                    ctx.fillStyle = p.color;
                    ctx.fillRect(p.x, p.y, p.size, p.size);
                    p.x += p.velX;
                    p.y += p.velY;
                    if (p.y > canvas.height) {{
                        p.y = -10;
                        p.x = Math.random() * canvas.width;
                    }}
                }});
                frame++;
                if (frame < 260) {{
                    requestAnimationFrame(render);
                }} else {{
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                }}
            }}
            render();
        }}
    </script>
</body>
</html>"""

# Sauvegarde sous sujet_fr.html et index.html (pour hébergement web standard)
with open("sujet_fr.html", "w") as f:
    f.write(html_template)

with open("index.html", "w") as f:
    f.write(html_template)

print("Generated sujet_fr.html and index.html successfully!")
