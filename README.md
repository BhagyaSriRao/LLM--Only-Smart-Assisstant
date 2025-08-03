# Gemini Smart Assistant
 This is a Python CLI application powered by the Gemini API. It answers general user questions with clear, structured, and logically ordered step-by-step explanations using prompt engineering.

# Features
 * Uses Gemini 1.5 model for natural language understanding.
 * Responds to general knowledge questions in a numbered step-by-step format.
 * Designed to produce human-like, structured responses.

# Requirements
 * Python 3.8+
 * Google Generative AI SDK
 * Gemini API key from Google AI Studio

#  Installation
  * Install dependencies:
     ```bash
      pip install google-generativeai

  * Set your Gemini API key as an environment variable:
     * Windows (Command Prompt):
        ```bash
         set GEMINI_API_KEY=your-api-key-here
     * macOS/Linux (bash):
       ```bash
          export GEMINI_API_KEY=your-api-key-here
  * Clone the repository:
      ```bash
         git clone https://github.com/BhagyaSriRao/LLM--Only-Smart-Assisstant.git
         cd LLM--Only-Smart-Assisstant
# Run the Assisstant:
     
        python chatbot.py
    
# Sample Interaction
* You: Why do we see only one side of the moon?
* Assistant:
  1. The Moon rotates on its axis just as it orbits the Earth.
  2. However, the Moon takes the same amount of time to rotate once as it does to orbit once — about 27.3 days.
  3. This synchronous rotation causes the same side of the Moon to always face Earth.
  4. As a result, we never see the far side from Earth without space probes or satellites.


  





