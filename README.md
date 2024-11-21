# Mystery-Dungeon-A-Text-Based-Game
Mystery Dungeon Game
#Description:-
Mystery Dungeon is a text-based adventure game written in Python. Players explore a dungeon filled with traps, monsters, and secrets in search of a hidden treasure. Each decision shapes the player's journey and outcome, making it an engaging and interactive experience.

Objectives:-
Create an immersive, decision-driven text-based game.
Use randomness for unpredictable outcomes and replayability.
Encourage strategic thinking through choices and consequences.

Features:-

Interactive Story: Players make decisions that determine their fate.
Randomized Outcomes: Events such as battles and traps rely on Python's random module, making each playthrough unique.
Multiple Endings: Outcomes vary depending on the player's choices (e.g., win, lose, or neutral escape).
Dynamic Paths: Different routes and surprises based on user input.
Replayability: Explore different paths and endings by replaying.

How to Play:-

Ensure Python (3.7 or later) is installed on your system.
Clone the repository:
git clone https://github.com/your-username/mystery-dungeon-game.git
Navigate to the project directory:
cd mystery-dungeon-game
Run the game:
python mystery_dungeon.py

## Diagram

 +-------------------------+
                        |      Start Game         |
                        +-------------------------+
                                 |
                                 v
                        +-------------------------+
                        |  Enter the Dungeon?     |
                        +-------------------------+
                         /          \
                      yes            no
                       /                \
                      v                  v
          +-------------------+   +------------------+
          | Meet Mysterious   |   |   Game Over      |
          | Guide?             |   +------------------+
          +-------------------+   
               /       \
            trust       ignore
              |            |
              v            v
   +----------------+  +----------------+
   |  Glowing Map   |  | Continue Alone  |
   +----------------+  +----------------+
          |                 |
          v                 v
   +----------------+   +------------------+
   |  First Path?   |   |  First Path?     |
   +----------------+   +------------------+
       /       \             /        \
    left        right    left          right
      |           |        |              |
      v           v        v              v
+---------------+  +----------------+   +------------------+
| Encounter     |  | Secret Door    |   | Encounter         |
| Monster?      |  +----------------+   | Trap or Secret    |
+---------------+        /     \         | Door or Bribe    |
       |                 open   ignore    +-----------------+
       v                    |        |            |
+--------------+          +---+  +----+        +------+
|  Fight       |          |   |  |    |        |   Game Over|
| Monster     |          |   |  |    |        +----------+
+--------------+         +---+ |    |        |    |
     |               \     v   v    v         v
     |        +------------------+  +---------------+
     |        |   Find Treasure   |  |  Cursed Chest |
     |        |   and Win!        |  | (Game Over)   |
     |        +------------------+  +---------------+  
     v                |
   Game Over      Treasure Found
