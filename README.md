# 🎮 Shadow Escape Game

Shadow Escape is a 2D maze survival game built using **Python and Pygame**.  
The player must escape through multiple levels while avoiding a chasing monster, traps, and obstacles.

---

## 🚀 Game Overview

In Shadow Escape, you control a player inside a maze.  
Your goal is to reach the exit while surviving:

- 👾 A monster that hunts you using AI pathfinding (BFS)
- ⚠️ Hidden traps that reduce your HP
- 🗺️ Increasingly difficult maze levels

Each level becomes harder with faster monsters and more traps.

---

## ✨ Features

- 🧠 Monster AI using **Breadth First Search (BFS) pathfinding**
- 🗺️ Multiple handcrafted maze levels
- 👾 Chasing enemy that adapts to player position
- ⚠️ Trap system with damage mechanics
- ❤️ Player HP system (3 lives)
- 🎮 Smooth arrow-key movement
- 🎨 Different colors per level for visual variety
- 🏁 Win / Game Over screens

---

## 🛠️ Technologies Used

- Python 🐍  
- Pygame 🎮  
- Collections (deque for BFS algorithm)

---

## ▶️ How to Run

### 1. Install Python
Make sure Python 3 is installed on your system.
 
 ---
 
 🎮 Controls
⬆️ Arrow Up → Move Up
⬇️ Arrow Down → Move Down
⬅️ Arrow Left → Move Left
➡️ Arrow Right → Move Right
SPACE → Start Game
🧠 AI System

The monster uses BFS (Breadth First Search) algorithm to find the shortest path to the player.

This makes the enemy:

Smart
Persistent
Always chasing the optimal route
🗺️ Game Structure
levels[] → Contains maze layouts, traps, and difficulty settings
Player → Handles movement and health
Monster → AI enemy using BFS
Trap → Damage objects inside maze
Game → Main loop and game logic


👨‍💻 Author

Ismail Ahmed
- GitHub: https://github.com/ISMAIL-0wx
- LinkedIn: https://www.linkedin.com/in/ismail-ahmed-a17820233
  

### 2. Install Pygame
```bash
pip install pygame




