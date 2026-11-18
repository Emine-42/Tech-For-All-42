# ==============================================================================
# 42 | NIVEAU 4 : LE CASINO DE 42 (MACHINE À SOUS)
# ==============================================================================
# CAHIER DES CHARGES STRICT (POUR LA MOULINETTE) :
#
# 1. On démarre avec 100 crédits. Chaque tirage coûte -10 crédits.
# 2. Si les 3 symboles sont identiques :
#    - Afficher OBLIGATOIREMENT le mot : "JACKPOT"
#    - Ajouter +50 crédits.
# 3. Si au moins 2 symboles sont identiques :
#    - Afficher OBLIGATOIREMENT le mot : "PAIRE"
#    - Ajouter +15 crédits.
# 4. Si tous les symboles sont différents :
#    - Afficher OBLIGATOIREMENT le mot : "PERDU"
#    - Gain : 0 crédit.
# ==============================================================================

import random

credits = 100
symboles = ["7", "@", "#", "$"]

print("🎰 BIENVENUE AU CASINO DE 42 🎰")
print(f"Crédits de départ : {credits} (Coût par tirage : 10 crédits)\n")

while credits >= 10:
    input(f"[Crédits : {credits}] Appuie sur ENTRÉE pour lancer le tirage (-10)...")
    credits -= 10
    
    r1 = random.choice(symboles)
    r2 = random.choice(symboles)
    r3 = random.choice(symboles)
    print(f"\n🎰 Tirage : [ {r1} | {r2} | {r3} ]")

    # --------------------------------------------------------------------------
    # À COMPLÉTER : RÈGLES DE GAINS STRICTES
    # --------------------------------------------------------------------------

    # CAS 1 : 3 symboles identiques (Jackpot !)
    ...

    # CAS 2 : Au moins 2 symboles identiques (Paire)
    ...

    # CAS 3 : Aucun symbole identique (Perdu)
    ...

print("\n💀 Game Over ! Tu n'as plus assez de crédits.")

# ==============================================================================
# VALIDATION :
# Lance la Moulinette dans ton terminal pour tester et certifier ton code :
#     python3 moulinette.py
# ==============================================================================
