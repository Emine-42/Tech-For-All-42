# ==============================================================================
# 42 | NIVEAU 3 : DÉCHIFFREMENT DU CODE SECRET (CHIFFRE DE CÉSAR)
# ==============================================================================
# Consigne :
# Le message secret a été chiffré en décalant chaque lettre dans l'alphabet.
# Complète les trous pour tester les 26 décalages possibles (Force Brute).
#
# Dès que tu vois un message lisible débuter par 42_...,
# COPIE ET ENTRE CE MESSAGE DÉCHIFFRÉ DIRECTEMENT SUR LA PAGE WEB DU SUJET !
# ==============================================================================

message_secret = "42_PDFKLQH_D_VRXV"

print("--- DÉBUT DE LA CRYPTANALYSE (26 ESSAIS) ---")

for decalage in range(1, 26):
    resultat = ""
    for lettre in message_secret:
        if 'A' <= lettre <= 'Z':
            # ------------------------------------------------------------------
            # À COMPLÉTER :
            # 1. Calcule la nouvelle position en reculant de 'decalage' (modulo 26)
            # 2. Reconvertis ce code en caractère avec chr(...)
            # ------------------------------------------------------------------
            position = (ord(lettre) - ord('A') - decalage) % 26
            lettre_decalee = chr(position + ord('A'))
            
            resultat += lettre_decalee
        else:
            # On conserve les caractères spéciaux (chiffres, _, :, /, etc.) intacts
            resultat += lettre

    print(f"Clé {decalage:02d} : {resultat}")

# ==============================================================================
# VALIDATION :
# Repère la ligne contenant le message lisible (ex: 42_...) et entre-le sur la page web !
# ==============================================================================
