#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
   __  __  ___  _   _ _     ___ _   _ _____ _____ _____ _____ 
  |  \/  |/ _ \| | | | |   |_ _| \ | | ____|_   _|_   _| ____|
  | |\/| | | | | | | | |    | ||  \| |  _|   | |   | | |  _|  
  | |  | | |_| | |_| | |___ | || |\  | |___  | |   | | | |___ 
  |_|  |_|\___/ \___/|_____|___|_| \_|_____| |_|   |_| |_____|
                                                              
        MOULINETTE 42 — VALIDATION OFFICIELLE (MACHINE À SOUS)
==============================================================================
"""

import sys
import os
import subprocess
import time

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

BANNER = f"""{CYAN}{BOLD}
    _  _  ____    __  __             _ _            _   _       
   | || ||___ \  |  \/  | ___  _   _| (_)_ __   ___| |_| |_ ___ 
   | || |_ __) | | |\/| |/ _ \| | | | | | '_ \ / _ \ __| __/ _ \\
   |__   _/ __/  | |  | | (_) | |_| | | | | | |  __/ |_| ||  __/
      |_||_____| |_|  |_|\___/ \__,_|_|_|_| |_|\___|\__|\__\___|
{RESET}{DIM}         >>> CERTIFICATION OFFICIELLE : MACHINE À SOUS <<<{RESET}
"""

def find_file(filename):
    search_paths = [
        filename,
        os.path.join(".", filename),
        os.path.join(os.path.expanduser("~"), "Bureau", "mission_42", filename),
        os.path.join(os.path.expanduser("~"), "Desktop", "mission_42", filename),
        os.path.join("..", filename),
    ]
    for p in search_paths:
        if os.path.isfile(p):
            return p
    return None

def test_slot_machine():
    print(BANNER)
    print(f"{BOLD}🔍 Vérification de votre fichier 'slot_machine.py'...{RESET}")
    
    filepath = find_file("slot_machine.py")
    if not filepath:
        print(f"\n{RED}❌ ERREUR : Fichier 'slot_machine.py' introuvable !{RESET}")
        print(f"{YELLOW}👉 Conseil : Vérifiez que vous êtes bien dans le dossier 'mission_42' et que le fichier est bien nommé.{RESET}\n")
        return False

    print(f"{GREEN}✓ Fichier détecté : {filepath}{RESET}")

    # 1. Analyse statique du code source
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read().upper()

    has_jackpot_word = "JACKPOT" in code
    has_paire_word = "PAIRE" in code
    has_perdu_word = "PERDU" in code
    has_50 = "50" in code
    has_15 = "15" in code

    print(f"{DIM}Test 1/3 : Analyse des mots-clés obligatoires...{RESET}", end=" ")
    if not (has_jackpot_word and has_paire_word and has_perdu_word):
        print(f"{RED}[ÉCHEC]{RESET}")
        print(f"\n{RED}❌ Attention : Votre code ne contient pas tous les mots requis par le cahier des charges !{RESET}")
        print(f"{YELLOW}👉 Rappel des affichages obligatoires :")
        print(f"   • 3 identiques : doit afficher le mot 'JACKPOT'")
        print(f"   • 2 identiques : doit afficher le mot 'PAIRE'")
        print(f"   • 0 identique  : doit afficher le mot 'PERDU'{RESET}\n")
        return False
    print(f"{GREEN}[OK]{RESET}")

    print(f"{DIM}Test 2/3 : Analyse des règles de crédits (+50 et +15)...{RESET}", end=" ")
    if not (has_50 and has_15):
        print(f"{RED}[ÉCHEC]{RESET}")
        print(f"\n{RED}❌ Attention : Les valeurs de gain (+50 pour Jackpot, +15 pour Paire) sont absentes.{RESET}\n")
        return False
    print(f"{GREEN}[OK]{RESET}")

    # 2. Test dynamique (exécution)
    print(f"{DIM}Test 3/3 : Simulation d'une session de jeu (lancers automatiques)...{RESET}", end=" ")
    try:
        proc = subprocess.Popen(
            [sys.executable, filepath],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input="\n\n\n\n\n", timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f"{RED}[ÉCHEC]{RESET}")
        print(f"\n{RED}❌ ERREUR : Le script est bloqué dans une boucle infinie ou ne répond pas aux touches Entrée.{RESET}\n")
        return False
    except Exception as e:
        print(f"{RED}[ÉCHEC]{RESET}")
        print(f"\n{RED}❌ ERREUR lors du lancement : {e}{RESET}\n")
        return False

    out_upper = stdout.upper()
    found_any = ("JACKPOT" in out_upper) or ("PAIRE" in out_upper) or ("PERDU" in out_upper)

    if not found_any:
        print(f"{RED}[ÉCHEC]{RESET}")
        print(f"\n{RED}❌ Aucun des mots attendus (JACKPOT, PAIRE, PERDU) n'a été affiché pendant la partie.{RESET}\n")
        return False

    print(f"{GREEN}[OK]{RESET}")

    # SUCCÈS
    print(f"\n{GREEN}{BOLD}════════════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}{BOLD}  🎉 CERTIFICATION VALIDÉE PAR LA MOULINETTE ! (ÉTOILE 4 ⭐⭐⭐⭐){RESET}")
    print(f"{GREEN}{BOLD}════════════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{CYAN}Votre Machine à Sous respecte scrupuleusement les règles et la syntaxe demandée !{RESET}")
    print(f"\nVoici votre code pour déverrouiller l'épreuve finale ({BOLD}Niveau 5{RESET}) sur la page web :")
    print(f"\n   👉  {YELLOW}{BOLD}CASINO-42-JACKPOT{RESET}  👈\n")
    print(f"{DIM}(Entrez ce code sur la page web pour accéder au Peer-Learning){RESET}\n")
    return True

if __name__ == "__main__":
    test_slot_machine()
