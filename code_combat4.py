import random

# 1. Generazione del nome casuale per i personaggi
names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
surnames = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]

def generate_name():
    name = random.choice(names)
    surname = random.choice(surnames)
    return f"{name} {surname}"

# 2. Funzione per il lancio dei dadi
def roll_dice(dice, sides, drop_low=1, drop_high=1):
    rolls = [random.randint(1, sides) for _ in range(dice)]
    rolls.sort()
    
    # Rimuovi il dado più basso e quello più alto
    for _ in range(drop_low):
        rolls.pop(0)  # Rimuovi il dado più basso
    for _ in range(drop_high):
        rolls.pop()  # Rimuovi il dado più alto
        
    return rolls

# 3. Funzione per calcolare il danno e aggiornare la salute
def calculate_damage(rolls, shield):
    if rolls:
        damage = sum(rolls) - shield
        if damage > 0:
            return damage
    return 0  # Se il danno è 0 o meno, l'attacco è evitato

# 4. Ciclo di gioco
def game_turn(player1_name, player2_name, p1_health, p2_health, p1_shield, p2_shield):
    # Lancia i dadi per i due giocatori
    p1_rolls = roll_dice(6, 6, drop_low=1, drop_high=1)
    p2_rolls = roll_dice(4, 12, drop_low=1, drop_high=1)
    
    print(f"\n{player1_name} Health: {p1_health} | {player2_name} Health: {p2_health}")
    
    # Fasi di attacco
    p1_damage = calculate_damage(p1_rolls, p2_shield)
    p2_damage = calculate_damage(p2_rolls, p1_shield)
    
    # Aggiornamento della salute
    p1_health -= p2_damage
    p2_health -= p1_damage
    
    # Stampa dei risultati
    print(f"\n[{player1_name}] dice: {p1_rolls}")
    print(f"The lower dice ({p1_rolls[0]}) and the higher one ({p1_rolls[-1]}) has been removed.")
    if p1_damage > 0:
        print(f"[{player1_name}] Damage: {p1_damage} ({p1_health+p1_shield}-{p2_shield})")
    else:
        print(f"[{player1_name}] Damage: 0. The attack has been avoided.")
    
    print(f"[{player2_name}] Health: {p2_health}")
    
    print(f"\n[{player2_name}] dice: {p2_rolls}")
    print(f"The lower dice ({p2_rolls[0]}) and the higher one ({p2_rolls[-1]}) has been removed.")
    if p2_damage > 0:
        print(f"[{player2_name}] Damage: {p2_damage} ({p2_health+p2_shield}-{p1_shield})")
    else:
        print(f"[{player2_name}] Damage: 0. The attack has been avoided.")
    
    print(f"[{player1_name}] Health: {p1_health}")
    
    return p1_health, p2_health

# Funzione principale di gioco che gestisce più turni
def play_game():
    # Inizializzazione dei giocatori
    player1_name = generate_name()
    player2_name = generate_name()
    
    # Salute e scudi iniziali
    p1_health, p1_shield = 98, 6
    p2_health, p2_shield = 82, 9
    
    print(f"\n{player1_name} starting health: {p1_health}")
    print(f"{player1_name} shield: {p1_shield}")
    print(f"{player2_name} starting health: {p2_health}")
    print(f"{player2_name} shield: {p2_shield}")
    
    # Ciclo di gioco
    turn_count = 0
    while p1_health > 0 and p2_health > 0:
        turn_count += 1
        print(f"\n--- Turn {turn_count} ---")
        p1_health, p2_health = game_turn(player1_name, player2_name, p1_health, p2_health, p1_shield, p2_shield)
    
    # Determina il vincitore
    if p1_health <= 0:
        print(f"\n{player2_name} WINS!")
    elif p2_health <= 0:
        print(f"\n{player1_name} WINS!")
    print(f"Turns played: {turn_count}")

# Esecuzione del gioco
play_game()
