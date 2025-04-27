# CT=22089

# 🧠 Tic-Tac-Toe AI: Minimax vs Alpha-Beta Pruning

This is a command-line implementation of Tic-Tac-Toe in Python where you play against an AI using the Minimax algorithm. It also compares the performance of standard **Minimax** and **Minimax with Alpha-Beta pruning** to demonstrate how optimization improves execution time.

## 🎮 Gameplay

- You play as **`X`**, and the AI plays as **`O`**.
- Enter your move using row and column numbers (0 to 2).
- After each of your moves, the AI will compute its optimal move using Alpha-Beta pruning.
- After the game, you'll see a performance comparison between the two algorithms.

---

## 📂 File Structure

```
.
├── tic_tac_toe_ai.py      # Main script to run the game
└── README.md              # This file
```

---

## 🚀 How to Run

### Requirements

No external libraries required. This project uses only standard Python libraries.

### Run the Game

```bash
python tic_tac_toe_ai.py
```

---

## 🧠 AI Logic

### Minimax Algorithm

- Explores all possible game states recursively.
- Returns the best score based on potential wins/losses.
- Computationally expensive as the number of possible states increases.

### Alpha-Beta Pruning

- Optimized version of Minimax.
- Prunes branches that don't influence the final decision.
- Significantly reduces execution time without affecting decision quality.

---

## 📊 Performance Comparison

At the end of each game, you'll see a report like:

```
Performance Comparison:
Standard Minimax total time: 0.154832 seconds
Alpha-Beta Pruning total time: 0.045612 seconds
Improvement: 70.54%
```

This shows how Alpha-Beta pruning improves efficiency while making the same strategic decisions.

---

## ✅ Features

- Full 3x3 Tic-Tac-Toe board rendering in terminal
- Input validation for human moves
- AI that never loses (perfect play)
- Side-by-side performance tracking of two AI approaches

---

## 📌 Future Improvements

- Add a GUI using `tkinter` or `pygame`
- Support different board sizes
- Implement difficulty levels by limiting search depth

---

