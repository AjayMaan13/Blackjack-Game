# 🃏 Blackjack Game

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Game](https://img.shields.io/badge/Game-Card%20Game-brightgreen)](https://en.wikipedia.org/wiki/Blackjack)
[![OOP](https://img.shields.io/badge/OOP-Classes-blue)](https://en.wikipedia.org/wiki/Object-oriented_programming)

> **Object-oriented Blackjack game in Python featuring classes, methods, and classic casino gameplay mechanics**

---

## 🔍 Overview

A fully functional Blackjack game built in Python demonstrating object-oriented programming principles, game logic implementation, and interactive CLI gameplay. Features realistic casino mechanics with betting, multiple rounds, and proper card handling.

**Developer:** Ajaypartap Singh Maan  
**Contact:** ajayapsmaanm13@gmail.com  

---

## 🛠️ Technologies & Skills

### **Core Technologies**
- **Python 3** - Object-oriented programming and game development
- **Random Module** - Card shuffling and deck randomization
- **CLI Interface** - Interactive command-line gameplay

### **Programming Concepts**
- **Object-Oriented Design** - Classes for Deck and Player
- **Data Structures** - Lists, dictionaries, tuples for game state
- **Game Logic** - Blackjack rules implementation
- **Error Handling** - Input validation and exception handling

---

## ✨ Key Features

### **🎮 Complete Blackjack Experience**
- **Full Deck Implementation** - 52-card deck with proper suits and ranks
- **Realistic Betting System** - Start with $2000, bet on each round
- **Multiple Rounds** - Play consecutive games with persistent money
- **Proper Blackjack Rules** - Hit/Stay mechanics, dealer logic

### **🏗️ Object-Oriented Architecture**
```python
class Deck:
    def __init__(self):
        self.all_cards = []
        self.value_cards = {}
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def hit_one(self):
        return self.all_cards.pop(0)

class Player:
    def __init__(self, name, money=2000):
        self.name = name
        self.money = money
        self.all_cards = []
    
    def bet(self):
        # Betting logic with input validation
    
    def add_money(self, amount):
        self.money += amount
```

### **🎯 Game Mechanics**
- **Card Values** - Proper values (Face cards = 10, Ace = 11)
- **Dealer Logic** - Dealer hits until 17 or higher
- **Win Conditions** - Player vs dealer comparison
- **Bust Detection** - Automatic loss when exceeding 21

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/blackjack-game.git
cd blackjack-game

# Run the game
python main.py
```

---

## 🎮 Gameplay Example

```
Player Enter your name: John
Player John has balance 2000

John has card: King of Hearts
John has card: Seven of Spades
Dealer have 1 card Ace of Clubs and other is hidden

Enter your Bet amount: 100
Round 1 begin:

John what do you want to do Hit or Stay: hit
Player John have card: Four of Diamonds

John what do you want to do Hit or Stay: stay

Dealer have card: Ace of Clubs
Dealer have card: Six of Hearts
Dealer have card: Three of Spades

🎉 Congratulations John you have won the bet 🎉
Player John has balance 2100
```

---

## 🏗️ Technical Implementation

### **Card System**
```python
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
```

### **Value Calculation**
```python
def value_check(list1):
    global value
    value = 0
    for n in list1:
        value += newdeck.value_cards[n]
    return int(value)

def value_21(list1):
    if value_check(list1) > 21:
        # Handle bust condition
        game_in_in = False
        game_in = False
        game_in_out = False
```

### **Betting System**
```python
def bet(self):
    while True:
        try:
            self.bet_amount = int(input("Enter your Bet amount: "))
            self.money = self.money - self.bet_amount
            return f'Your bet is {self.bet_amount}'
        except ValueError:
            print("Integer, please.")
```

---

## 🎯 Skills Demonstrated

### **Object-Oriented Programming**
- **Class Design** - Deck and Player classes with appropriate methods
- **Encapsulation** - Private data and public interfaces
- **Method Implementation** - Betting, card dealing, money management
- **State Management** - Player balance, cards, game status

### **Game Development**
- **Game Loop Implementation** - Multiple nested loops for rounds
- **Event Handling** - Player decisions (hit/stay)
- **Win/Loss Logic** - Proper comparison and payout calculation
- **User Experience** - Clear prompts and game status updates

### **Python Programming**
- **Data Structures** - Effective use of lists, dictionaries, tuples
- **Control Flow** - While loops, conditionals, exception handling
- **String Manipulation** - Card representation and formatting
- **Input Validation** - Robust error handling for user input

---

## 🔧 Current Implementation

### **Included Features**
- ✅ **Basic Blackjack Rules** - Hit, stay, bust detection
- ✅ **Dealer Logic** - Automatic dealer play (hits until 17+)
- ✅ **Betting System** - Player money management
- ✅ **Multiple Rounds** - Continuous gameplay
- ✅ **Proper Card Values** - Aces as 11, face cards as 10

### **Future Enhancements**
- 🔄 **Advanced Features** - Split, double down, surrender
- 🔄 **Flexible Aces** - Ace as 1 or 11 based on hand value
- 🔄 **Insurance Betting** - When dealer shows Ace
- 🔄 **GUI Implementation** - Tkinter or Pygame interface
- 🔄 **Multiplayer Support** - Multiple players vs dealer
- 🔄 **Save/Load Game** - Persistent player progress

---

## 📊 Code Quality Features

- **Clean Class Structure** - Well-organized object-oriented design
- **Descriptive Functions** - Clear, single-purpose methods
- **Input Validation** - Prevents crashes from invalid input
- **Global State Management** - Proper game state tracking
- **Modular Design** - Easy to extend with new features

---

## 🎲 Game Statistics

- **Starting Money:** $2000
- **Card Deck:** Standard 52-card deck
- **Dealer Rule:** Must hit on 16, stand on 17+
- **Player Options:** Hit or Stay
- **Payout:** 2:1 on wins (double bet amount)

---

## 📞 Contact

**Ajaypartap Singh Maan**  
📧 ajayapsmaanm13@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/ajaypartap-singh-maan)  
🐙 [GitHub](https://github.com/AjayMaan13)  

---

## 🏷️ Tags

`Python` `Object-Oriented Programming` `Game Development` `Blackjack` `CLI Application` `Card Game` `Casino Logic` `Class Design`

---

*Demonstrating solid object-oriented programming principles and game development fundamentals in Python*
