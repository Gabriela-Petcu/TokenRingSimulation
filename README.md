🧠 TokenRingSimulation 🧠
TokenRingSimulation is a Python project that simulates a basic Token Ring network, where computers exchange messages using a circulating token.

📌 Features
🖥️ 10 Computers: Automatically generated with unique random IP addresses.
🔄 Token Passing: Simulates token movement either forward or backward.
📬 Message Transmission: Sends messages from a randomly selected source to a random destination.
🔍 Debug Mode: Detailed step-by-step simulation tracing available.
🧹 Token Reset: After message delivery, the token resets and the network continues operating.

🛠️ Technologies Used
Python 3.x – Programming language.
OOP (Object-Oriented Programming) – For modeling computers, tokens, and network behavior.
Random module – To simulate real-world randomness in networks.

🎮 How It Works
At startup, 10 computers are created with random IP addresses.
The user selects the token circulation direction: forward or backward.
Each simulation round randomly chooses a source and destination.
The token is passed around the network carrying the message.
Debug mode displays token passing history and message delivery events.

🚀 Setup & Running
1. Clone the repository:
git clone https://github.com/your-username/TokenRingSimulation.git
cd TokenRingSimulation
2. Run the simulation:
python main.py
