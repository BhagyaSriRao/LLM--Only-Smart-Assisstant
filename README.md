🧠 Gemini Smart Assistant
This is a Python CLI application powered by the Gemini API. It answers general user questions with clear, structured, and logically ordered step-by-step explanations using prompt engineering.

🚀 Features
Uses Gemini 1.5 model for natural language understanding.

Responds to general knowledge questions in a numbered step-by-step format.

Designed to produce human-like, structured responses.

🛠️ Requirements
Python 3.8+

Google Generative AI SDK

Gemini API key from Google AI Studio

📦 Installation
Install dependencies:

bash
Copy
Edit
pip install google-generativeai
Set your Gemini API key as an environment variable:

Windows (Command Prompt):

bash
Copy
Edit
set GEMINI_API_KEY=your-api-key-here
macOS/Linux (bash):

bash
Copy
Edit
export GEMINI_API_KEY=your-api-key-here
▶️ Run the Assistant
bash
Copy
Edit
python chatbot.py
💬 Sample Interaction
vbnet
Copy
Edit
You: Why is the sky blue?
Assistant:
1. Sunlight contains all colors of visible light.
2. When it enters Earth's atmosphere, it collides with air molecules.
3. Blue light is scattered more than other colors because it travels in shorter, smaller waves.
4. As a result, the sky appears blue to our eyes during the day.
