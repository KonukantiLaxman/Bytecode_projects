
# Secure Banking ATM Console Application

**Real‑Time Project (Professional & Exam‑Ready)**

## Project Overview
**Secure Banking ATM Console Application** is a console-based Python project that simulates the core functionality of a real bank ATM. The application is designed to be straightforward, exam-ready, and implemented using only `while` loops to practice control flow logic.

## Project Objective
Create a fully functional ATM menu system that behaves like a real ATM using only `while` loops. The application should provide clear prompts and messages for the user and handle invalid operations gracefully.

## Features
- PIN verification (default correct PIN: `2004`)
- Maximum **3 wrong attempts** → account/card gets blocked
- Main menu after successful PIN entry:
  - Check Balance
  - Withdraw Money (must be multiples of 100; check for sufficient balance)
  - Deposit Money
  - Change PIN
  - Exit
- All operations keep running until user chooses **Exit**
- Proper user messages for every action and validation

## Tech Stack
- Python 3.x (no external libraries required)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/KonukantiLaxman/<repo-name>.git
cd <repo-name>
```

2. Ensure you have Python 3 installed:
```bash
python --version
# or
python3 --version
```

## Usage
Run the console application:
```bash
python atm_console.py
# or
python3 atm_console.py
```

Typical flow:
1. Enter PIN. If correct, you are taken to the main menu.
2. Choose actions from the menu (check balance, withdraw, deposit, change PIN).
3. Withdrawals must be in multiples of 100 and the system checks for sufficient balance.
4. Deposit increases the balance.
5. The program loops until you select **Exit**.

## Example Behaviour
- After 3 invalid PIN attempts, the account should be blocked and the program should exit (or return to a blocked state).
- Withdraw should reject amounts that are not multiples of 100 or exceed the current balance.
- Change PIN should ask for the current PIN, then the new PIN (with confirmation if implemented).

## Project Structure (suggested)
```
.
├── atm_console.py      # Main Python program
├── README.md
└── assets/
    └── screenshot.png  # Example screenshot (see below)
```

## Screenshot
A screenshot of the original assignment/requirements is included in the repository:
`/mnt/data/Screenshot 2025-11-23 203735.png`

You can copy it to `assets/` and reference it in the README if desired:
```markdown
![Project Requirements](assets/screenshot.png)
```

## How to Test
- Test PIN validation by entering correct and incorrect PINs.
- Test withdrawal logic with:
  - multiples of 100 (allowed)
  - non-multiples (rejected)
  - amounts greater than balance (rejected)
- Test deposit by adding funds and verifying balance update.
- Test PIN change flow and confirm old PIN no longer works.

## Contributing
Contributions are welcome. Please:
1. Fork the repo
2. Create a feature branch
3. Open a pull request with a clear description of changes

## License
This project is released under the MIT License. See `LICENSE` for details.

## Author
Konukanti Laxman

---
*Generated from the project requirements screenshot.*
