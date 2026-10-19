#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

brain = Brain()

brain_inertial = Inertial()
motor_1 = Motor(Ports.PORT1, False)
motor_5 = Motor(Ports.PORT5, True)

wait(100, MSEC)

def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

initializeRandomSeed()
#endregion VEXcode Generated Robot Configuration

import random

# ==============================================================================
# ROBOT EVENT BROADCAST & MOTOR CONTROL
# ==============================================================================
FWD = Event()
RT = Event()
LT = Event()

def motor1_move_forward():
    motor_1.spin_for(FORWARD, 425, DEGREES, wait=False)

def motor5_move_forward():
    motor_5.spin_for(FORWARD, 425, DEGREES, wait=True)

def motor1_turn_right():
    motor_1.spin_for(FORWARD, 220, DEGREES, wait=False)

def motor5_turn_right():
    motor_5.spin_for(REVERSE, 220, DEGREES, wait=True)

def motor1_turn_left():
    motor_1.spin_for(REVERSE, 220, DEGREES, wait=False)

def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES, wait=True)

FWD(motor1_move_forward)
FWD(motor5_move_forward) 
RT(motor1_turn_right)
RT(motor5_turn_right)
LT(motor1_turn_left)      
LT(motor5_turn_left)
wait(15, MSEC)

# ==============================================================================
# FULL-SCREEN GRAPHICAL CARD DRAWING FUNCTIONS
# ==============================================================================
def draw_uno_card_back():
    """Renders a graphical representation of the back of an UNO card on screen."""
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    
    # Outer Card Border
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
    
    # Red Inner Background
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(15, 15, 130, 78)
    
    # Yellow Oval Center
    brain.screen.set_fill_color(Color.YELLOW)
    brain.screen.draw_circle(80, 54, 25)
    
    # "UNO" Text
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 8)
    brain.screen.print("UNO")
    brain.screen.set_fill_color(Color.TRANSPARENT)

def draw_card_full_screen(card_str, color_code):
    """Renders front face of an UNO card."""
    brain.screen.clear_screen()
    if color_code == 'R': brain.screen.set_fill_color(Color.RED)
    elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
    elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
    elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
    else: brain.screen.set_fill_color(Color.BLACK)
    
    brain.screen.set_pen_color(Color.WHITE)
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
   
    card = card_str[1:]
    if card == "0":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
    elif card == "8":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(72+i, 20, 72+i, 85)
    elif card == "1":
        for i in range(15):
            brain.screen.draw_line(20, 47+i, 139, 47+i)
    elif card == "3":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
    elif card == "2":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "5":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "6":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "9":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "4" and "D" not in card_str:
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
    elif card == "7":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
    elif card == "Rv":
        for i in range(15):
            brain.screen.draw_line(62+i, 30, 62+i, 87)
            brain.screen.draw_line(69, 20, 52+i, 40)
            brain.screen.draw_line(69, 20, 82-i, 40)
            brain.screen.draw_line(82+i, 20, 82+i, 77)
            brain.screen.draw_line(89, 87, 74+i, 67)
            brain.screen.draw_line(89, 87, 104-i, 67)
    elif card == "S":
        for i in range(15):
            brain.screen.draw_rectangle(40+i, 20+i, 82-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(52+i, 20, 92+i, 80)
    elif card == "D2":
        brain.screen.set_fill_color(Color.WHITE)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        if color_code == 'R': brain.screen.set_fill_color(Color.RED)
        elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
        elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
        elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(47, 32, 40, 25)
        brain.screen.draw_rectangle(73, 52, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10+i, 66, 10+i, 79)
            brain.screen.draw_line(10, 66+i, 20, 66+i)
            brain.screen.draw_line(18+i, 66, 18+i, 79)
            brain.screen.draw_line(20, 75+i, 30, 75+i)
            brain.screen.draw_line(26+i, 66, 26+i, 79)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10-i, 107-66, 159-10-i, 107-79)
            brain.screen.draw_line(159-10, 107-66-i, 159-20, 107-66-i)
            brain.screen.draw_line(159-18-i, 107-66, 159-18-i, 107-79)
            brain.screen.draw_line(159-20, 107-75-i, 159-30, 107-75-i)
            brain.screen.draw_line(159-26-i, 107-66, 159-26-i, 107-79)
    elif card_str == "W":
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(50, 20, 30, 32)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(50, 52, 30, 32)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(80, 20, 30, 32)
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(80, 52, 30, 32)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.set_pen_width(3)
        for i in range(15):
            brain.screen.draw_circle(80, 52, 30-(i/5))
        brain.screen.set_pen_color(Color.BLACK)
        for i in range(65):
            brain.screen.draw_circle(80, 52, 31+(i/5))
        brain.screen.set_pen_width(1)
    elif card_str == "D4":
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(78, 42, 40, 25)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(60, 28, 40, 25)
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(42, 42, 40, 25)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(60, 56, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10, 75+i, 20, 75+i)
            brain.screen.draw_line(16+i, 75, 16+i, 66)
            brain.screen.draw_line(10, 66+i, 30, 66+i)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10, 107-75-i, 159-20, 107-75-i)
            brain.screen.draw_line(159-16-i, 107-75, 159-16-i, 107-66)
            brain.screen.draw_line(159-10, 107-66-i, 159-30, 107-66-i)
    else:
        brain.screen.set_fill_color(Color.RED)
        brain.screen.set_pen_color(Color.RED)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        brain.screen.set_pen_color(Color.YELLOW)
        for i in range(5):
            brain.screen.draw_line(75, 50+i-5, 85, 50+i-5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i+5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i-5)

            brain.screen.draw_line(75, 50+i-15, 85, 50+i-15)
            brain.screen.draw_line(75+(i/2), 50-15, 75+(i/2), 50-25)
            brain.screen.draw_line(83+(i/2), 50-15, 83+(i/2), 50-25)
            brain.screen.draw_line(75, 50+i-25, 85, 50+i-25)

            brain.screen.draw_line(75, 50+i+15, 85, 50+i+15)
            brain.screen.draw_line(83+(i/2), 50+15, 83+(i/2), 50+25)
            brain.screen.draw_line(75, 50+i+25, 85, 50+i+25)
            
    brain.screen.set_fill_color(Color.TRANSPARENT)

def render_card_graphic(card):
    """Maps card dictionary to card_str and color_code for full-screen drawing."""
    color_map = {"Red": 'R', "Yellow": 'Y', "Green": 'G', "Blue": 'B'}
    c_code = color_map.get(card['color'], 'W')
    
    t = card['type']
    if t == "Wild":
        c_str = "W"
    elif t == "Wild Draw Four":
        c_str = "D4"
    elif t == "Skip":
        c_str = c_code + "S"
    elif t == "Reverse":
        c_str = c_code + "Rv"
    elif t == "Draw Two":
        c_str = c_code + "D2"
    else: # Number 0-9
        c_str = c_code + str(t)
        
    draw_card_full_screen(c_str, c_code)

# ==============================================================================
# PRIVACY & SCREEN DISPLAY FUNCTIONS
# ==============================================================================
def hide_hand_screen():
    """Hides the player's hand during transit to protect privacy."""
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_cursor(2, 1)
    brain.screen.print("*** HAND HIDDEN ***")
    brain.screen.set_cursor(3, 1)
    brain.screen.print(" PRIVACY MODE ON ")

def display_uno_screen():
    """Displays layered UNO banner when player deposits 2nd-to-last card."""
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("====================")
    brain.screen.set_cursor(3, 1)
    brain.screen.print("    *** UNO! ***    ")
    brain.screen.set_cursor(5, 1)
    brain.screen.print("====================")

def display_all_cards(hand):
    """Displays player's current hand across the 5-line text screen."""
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("HAND (" + str(len(hand)) + " cards):")
    
    line = 2
    cards_str = ""
    for i, card in enumerate(hand):
        cards_str += str(i + 1) + "." + format_short_card(card) + " "
        if len(cards_str) >= 15 or i == len(hand) - 1:
            if line <= 5:
                brain.screen.set_cursor(line, 1)
                brain.screen.print(cards_str[:20])
                line += 1
                cards_str = ""

# ==============================================================================
# ROBOT NAVIGATION ROUTINES
# ==============================================================================
def drive_to_center(show_uno=False):
    """Drives to center table. Shows 'UNO!' overlay if triggered, else hides hand."""
    if show_uno:
        display_uno_screen()
    else:
        hide_hand_screen()
    wait(300, MSEC)
    FWD.broadcast_and_wait()
    FWD.broadcast_and_wait()

def drive_back_to_player():
    """Keeps hand hidden while returning to player."""
    hide_hand_screen()
    wait(300, MSEC)
    
    # 180 Degree Turn
    RT.broadcast_and_wait()
    RT.broadcast_and_wait()
    
    # Drive back
    FWD.broadcast_and_wait()
    FWD.broadcast_and_wait()
    
    # Turn back around to face starting position
    RT.broadcast_and_wait()
    RT.broadcast_and_wait()

# ==============================================================================
# HARDWARE BUTTON HANDLER
# ==============================================================================
def wait_for_button_press():
    """Waits for a physical brain button press and returns 'LEFT', 'RIGHT', or 'CHECK'."""
    while brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing():
        wait(20, MSEC)
    
    while True:
        if brain.buttonLeft.pressing():
            while brain.buttonLeft.pressing(): wait(20, MSEC)
            return "LEFT"
        if brain.buttonRight.pressing():
            while brain.buttonRight.pressing(): wait(20, MSEC)
            return "RIGHT"
        if brain.buttonCheck.pressing():
            while brain.buttonCheck.pressing(): wait(20, MSEC)
            return "CHECK"
        wait(20, MSEC)

# ==============================================================================
# UNO GAME LOGIC & DECK HELPERS
# ==============================================================================
COLORS = ["Red", "Yellow", "Green", "Blue"]
ACTION_CARDS = ["Skip", "Reverse", "Draw Two"]

def create_uno_deck():
    deck = []
    for color in COLORS:
        deck.append({"color": color, "type": "0"})
        for number in range(1, 10):
            deck.append({"color": color, "type": str(number)})
            deck.append({"color": color, "type": str(number)})
        for action in ACTION_CARDS:
            deck.append({"color": color, "type": action})
            deck.append({"color": color, "type": action})
            
    for _ in range(4):
        deck.append({"color": None, "type": "Wild"})
        deck.append({"color": None, "type": "Wild Draw Four"})
        
    return deck

def custom_shuffle(deck):
    deck_length = len(deck)
    for i in range(deck_length - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

def deal_starting_hand(deck, num_cards=7):
    hand = []
    for _ in range(num_cards):
        if len(deck) > 0:
            hand.append(deck.pop(0))
    return hand

def format_full_name(card):
    if card['color'] is None:
        return card['type']
    return str(card['color']) + " " + str(card['type'])

def format_short_card(card):
    color_map = {"Red": "R", "Yellow": "Y", "Green": "G", "Blue": "B"}
    color_code = color_map.get(card['color'], "W")
    
    type_map = {
        "Skip": "Sk",
        "Reverse": "Rv",
        "Draw Two": "D2",
        "Wild Draw Four": "W4"
    }
    card_type = type_map.get(card['type'], card['type'])
    return str(color_code) + "-" + str(card_type)

def check_playable(card, top_card):
    if card['color'] is None:
        return True
    if top_card['color'] is not None and card['color'] == top_card['color']:
        return True
    if card['type'] == top_card['type']:
        return True
    return False

def get_legal_cards(hand, top_card):
    legal_indices = []
    for idx, card in enumerate(hand):
        if check_playable(card, top_card):
            legal_indices.append(idx)
    return legal_indices

def draw_multiple_cards_with_back_graphic(deck, player_hand, count=1):
    """Displays the back of an UNO card at the center table when drawing."""
    for _ in range(count):
        if len(deck) > 0:
            player_hand.append(deck.pop(0))
            draw_uno_card_back()
            wait(1200, MSEC)  # Shows UNO card back graphic while drawing
        else:
            brain.screen.clear_screen()
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(2, 1)
            brain.screen.print("DECK IS EMPTY!")
            wait(1200, MSEC)
            break

# ==============================================================================
# MENU SELECTION ROUTINES
# ==============================================================================
def choose_cards_to_draw():
    """Prompts player to select how many cards they want to draw (1 to 4)."""
    draw_options = ["1 Card", "2 Cards", "3 Cards", "4 Cards"]
    idx = 0
    while True:
        brain.screen.clear_screen()
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("HOW MANY TO DRAW?")
        brain.screen.set_cursor(3, 1)
        brain.screen.print("< " + draw_options[idx] + " >")
        brain.screen.set_cursor(5, 1)
        brain.screen.print("[L/R]:Nav  [Check]:OK")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            idx = (idx - 1) % len(draw_options)
        elif btn == "RIGHT":
            idx = (idx + 1) % len(draw_options)
        elif btn == "CHECK":
            return idx + 1

def select_table_card():
    """Allows player to choose/set the active card on the table."""
    color_options = ["Red", "Yellow", "Green", "Blue", "Wild"]
    color_idx = 0
    
    while True:
        brain.screen.clear_screen()
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("CHOOSE TABLE COLOR:")
        brain.screen.set_cursor(2, 1)
        brain.screen.print("< " + color_options[color_idx] + " >")
        brain.screen.set_cursor(5, 1)
        brain.screen.print("[L/R]:Nav  [Check]:OK")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            color_idx = (color_idx - 1) % len(color_options)
        elif btn == "RIGHT":
            color_idx = (color_idx + 1) % len(color_options)
        elif btn == "CHECK":
            selected_color = None if color_options[color_idx] == "Wild" else color_options[color_idx]
            break

    if selected_color is None:
        wild_options = ["Wild", "Wild Draw Four"]
        wild_idx = 0
        while True:
            brain.screen.clear_screen()
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print("SELECT WILD TYPE:")
            brain.screen.set_cursor(2, 1)
            brain.screen.print("< " + wild_options[wild_idx] + " >")
            brain.screen.set_cursor(5, 1)
            brain.screen.print("[L/R]:Nav  [Check]:OK")
            
            btn = wait_for_button_press()
            if btn == "LEFT":
                wild_idx = (wild_idx - 1) % len(wild_options)
            elif btn == "RIGHT":
                wild_idx = (wild_idx + 1) % len(wild_options)
            elif btn == "CHECK":
                selected_type = wild_options[wild_idx]
                break
    else:
        types_options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
        type_idx = 0
        while True:
            brain.screen.clear_screen()
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print("TYPE FOR " + selected_color.upper() + ":")
            brain.screen.set_cursor(2, 1)
            brain.screen.print("< " + types_options[type_idx] + " >")
            brain.screen.set_cursor(5, 1)
            brain.screen.print("[L/R]:Nav  [Check]:OK")
            
            btn = wait_for_button_press()
            if btn == "LEFT":
                type_idx = (type_idx - 1) % len(types_options)
            elif btn == "RIGHT":
                type_idx = (type_idx + 1) % len(types_options)
            elif btn == "CHECK":
                selected_type = types_options[type_idx]
                break

    return {"color": selected_color, "type": selected_type}

def player_turn_menu(player_hand, current_table_card):
    """
    1. First, select/confirm the active table card to calculate legal moves.
    2. Then, choose action: ATTACK or DRAW CARD.
    """
    # Step 1: Set/Confirm Table Card
    updated_table_card = select_table_card()
    
    # Step 2: Choose Action (ATTACK vs DRAW CARD)
    turn_options = ["ATTACK", "DRAW CARD"]
    option_idx = 0
    
    while True:
        brain.screen.clear_screen()
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("TABLE: " + format_full_name(updated_table_card)[:13])
        brain.screen.set_cursor(2, 1)
        brain.screen.print("CHOOSE ACTION:")
        brain.screen.set_cursor(3, 1)
        brain.screen.print("< " + turn_options[option_idx] + " >")
        brain.screen.set_cursor(5, 1)
        brain.screen.print("[L/R]:Nav  [Check]:OK")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            option_idx = (option_idx - 1) % len(turn_options)
        elif btn == "RIGHT":
            option_idx = (option_idx + 1) % len(turn_options)
        elif btn == "CHECK":
            chosen_action = turn_options[option_idx]
            break

    # --- Choice A: DRAW CARD ---
    if chosen_action == "DRAW CARD":
        num_cards = choose_cards_to_draw()
        return ("DRAW", num_cards, updated_table_card)

    # --- Choice B: ATTACK ---
    legal_indices = get_legal_cards(player_hand, updated_table_card)
    
    if len(legal_indices) == 0:
        brain.screen.clear_screen()
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(2, 1)
        brain.screen.print("NO LEGAL CARDS!")
        brain.screen.set_cursor(3, 1)
        brain.screen.print("Forced to DRAW.")
        wait(1500, MSEC)
        num_cards = choose_cards_to_draw()
        return ("DRAW", num_cards, updated_table_card)

    # Step B1: Select playable card from player hand
    card_select_idx = 0
    while True:
        brain.screen.clear_screen()
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("SELECT HAND CARD:")
        
        card_idx = legal_indices[card_select_idx]
        card = player_hand[card_idx]
        
        brain.screen.set_cursor(2, 1)
        brain.screen.print("> " + format_short_card(card))
        brain.screen.set_cursor(3, 1)
        brain.screen.print("Card #" + str(card_idx + 1) + " (" + str(card_select_idx + 1) + "/" + str(len(legal_indices)) + ")")
        brain.screen.set_cursor(5, 1)
        brain.screen.print("[L/R]:Nav  [Check]:OK")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            card_select_idx = (card_select_idx - 1) % len(legal_indices)
        elif btn == "RIGHT":
            card_select_idx = (card_select_idx + 1) % len(legal_indices)
        elif btn == "CHECK":
            chosen_card_idx = legal_indices[card_select_idx]
            played_card = player_hand[chosen_card_idx]
            break

    return ("ATTACK", played_card, updated_table_card)

# ==============================================================================
# MAIN GAME LOOP
# ==============================================================================
def main():
    deck = create_uno_deck()
    custom_shuffle(deck)
    player_hand = deal_starting_hand(deck, 7)
    
    top_card = None  # Initialized so the variable exists for player_turn_menu
    
    while len(player_hand) > 0:
        # 1. Display current hand before taking turn
        display_all_cards(player_hand)
        wait(2000, MSEC)
        
        # 2. First select table card, then choose action (ATTACK or DRAW)
        action_type, action_data, top_card = player_turn_menu(player_hand, top_card)
        
        # 3. Check for UNO trigger (1 card left after playing)
        is_uno = (action_type == "ATTACK" and len(player_hand) == 2)
        
        if is_uno:
            brain.play_sound(SoundType.TADA)
        
        # 4. Drive to center table
        drive_to_center(show_uno=is_uno)
        wait(500, MSEC)
        
        # 5. Execute Action at center table
        if action_type == "DRAW":
            draw_count = action_data
            # Displays the back of an UNO card on screen for each drawn card
            draw_multiple_cards_with_back_graphic(deck, player_hand, count=draw_count)
        elif action_type == "ATTACK":
            played_card = action_data
            player_hand.remove(played_card)
            
            # Show full-screen graphical render of the played card at the center table
            render_card_graphic(played_card)
            wait(2000, MSEC)
            
        # 6. Drive back to player (Privacy maintained during transit)
        drive_back_to_player()
        
        # 7. Reveal updated card numbers & hand upon returning to player
        display_all_cards(player_hand)
        wait(2500, MSEC)

    # Win Screen
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_cursor(2, 1)
    brain.screen.print("*** YOU WIN! ***")
    brain.screen.set_cursor(3, 1)
    brain.screen.print("ALL CARDS PLAYED!")

main()