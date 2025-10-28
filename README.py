## 🧠 Wumpus World AI Simulation

### 🎯 Overview

The **Wumpus World AI Simulation** is a classic **knowledge-based AI game** where an intelligent agent explores a 4×4 grid world to **find gold**, while avoiding deadly **pits** and the **Wumpus monster**.
It demonstrates concepts of **Artificial Intelligence reasoning**, **logic-based knowledge representation**, and **autonomous decision-making**.

---

### 🕹️ Features

* 🤖 **AI Agent** that perceives the environment and decides safe moves.
* 🕳️ **Pits** (cause death if fallen into).
* 👹 **Wumpus** (kills the agent if encountered).
* 💰 **Gold** (the goal to find).
* 💡 **Knowledge-based reasoning**:

  * Breeze ⇒ pit nearby
  * Stench ⇒ Wumpus nearby
  * Glitter ⇒ gold found
  * No breeze/stench ⇒ safe cells inferred
* 🔄 **Autonomous movement** and logical exploration.

---

### 🧩 Folder Structure

```
wumpus_project/
│
├── environment.py     # Handles world layout, percepts (breeze, stench, glitter)
├── agent.py           # Knowledge-based reasoning and movement logic
├── run_demo.py        # Main GUI and simulation loop
└── README.md          # Project documentation
```

---

### 🧰 Requirements

* Python 3.8 or higher
* Tkinter (included by default with Python)

To check Tkinter installation:

```bash
python -m tkinter
```

If a small window appears, it’s already installed ✅

---

### ▶️ How to Run

1. Clone or download this repository:

   ```bash
   git clone https://github.com/<your-username>/wumpus_project.git
   ```
2. Open the project folder:

   ```bash
   cd wumpus_project
   ```
3. Run using Python or IDLE:

   ```bash
   python run_demo.py
   ```

   Or, open `run_demo.py` in **IDLE** → press **F5**.

---

### 🖼️ Simulation Preview

Each cell on the grid represents part of the Wumpus world:

| Emoji | Meaning  |
| ----- | -------- |
| 🤖    | AI Agent |
| 💰    | Gold     |
| 👹    | Wumpus   |
| 🕳️   | Pit      |

The agent moves logically, senses danger, and tries to grab the gold 🏆.

---

### 🧩 AI Logic Summary

| Percept    | AI Inference                |
| ---------- | --------------------------- |
| Breeze     | There’s a pit nearby        |
| Stench     | Wumpus is nearby            |
| Glitter    | Gold is in this cell        |
| No Percept | All adjacent cells are safe |

---

### 🧾 Project Type

**AI Mini Project** — Suitable for college submissions under topics like:

* Knowledge-Based Systems
* Game Theory & Simulation
* Artificial Intelligence Agents
* Python-Based AI Simulation

---

### 🏁 Output Example (Console)

```
🤖 At [0, 0] perceives []
🤖 At [0, 1] perceives ['breeze']
🤖 At [1, 1] perceives []
🏆 Gold found at [2, 2]
🎉 AI Agent completed the mission!
```

---

### 💻 Author

**< BARATH S>**
Department of CSE(Artificial Intelligence and Machine Learning)
Project Title: *Wumpus World — A Knowledge-Based Game Simulation for AI Agents*

