#import necessary libraries

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Check if a GPU is available and use it; otherwise, fall back to CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the pre-trained DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set the pad_token to eos_token if it's not already set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


def emotion_based_response(emotion: str, user_input: str, temperature: float) -> str:
    """
    Generate a response based on the user's emotion and input using the DialoGPT model.

    Args:
        emotion (str): The emotional tone (e.g., "Happy", "Sad", etc.) to guide the response.
        user_input (str): The input text from the user to generate a response for.
        temperature (float): A value to control the creativity of the model's response.
        
    Returns:
        str: The AI-generated response based on the emotional tone and user input.
    """
    try:
        # Check if the user input is empty or just whitespace
        if not user_input.strip():
            return ("Sorry, you told me your emotion but haven't said anything. "
                    "Come on, tell me something! Input something!")

        # Create the emotion-based prompt
        prompt = f"User is feeling {emotion}. Respond in that emotional tone: {user_input}"

        # Encode the input text to tokens, and also generate the attention_mask
        encoding = tokenizer(prompt + tokenizer.eos_token, return_tensors='pt', padding=True)
        input_ids = encoding['input_ids'].to(device)
        attention_mask = encoding['attention_mask'].to(device)

        # Generate the model's output with the specified temperature and enable sampling
        output = model.generate(
            input_ids,
            max_length=1000,
            temperature=temperature,
            do_sample=True,  # This enables sampling to use the temperature setting
            pad_token_id=tokenizer.eos_token_id,
            attention_mask=attention_mask,  # Pass the attention_mask to avoid confusion
            no_repeat_ngram_size=2
        )

        # Decode the output to text
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Return the generated text (after removing the prompt part)
        return response[len(prompt):]

    except Exception as e:
        return f"Error: {str(e)}"


# Define the Gradio interface (Updated with temperature slider)
iface = gr.Interface(
    fn=emotion_based_response,
    inputs=[
        gr.Dropdown(
            choices=["Happy", "Sad", "Angry", "Surprised", "Excited", "Neutral"],
            label="Select Emotion"
        ),
        gr.Textbox(
            lines=2,
            placeholder=(
                '"Happy": "I am having such a good day!"\n'
                '"Sad": "I feel so down today..."\n'
                '"Angry": "I am really upset about this situation!"\n'
                '"Surprised": "I can\'t believe this just happened!"\n'
                '"Excited": "I am so thrilled about this new opportunity!"\n'
                '"Neutral": "I just wanted to ask you a question."'
            ),
            label="Your Input"
        ),
        gr.Slider(minimum=0.1, maximum=0.9, step=0.1, value=0.5, label="Temperature")
    ],
    outputs="text",
    title="Emotion-Based Conversational AI using Microsoft's DialoGPT",
    description=(
        "Interact with an AI that generates responses in different emotional tones based on your input. "
        "Select an emotion (e.g., Happy, Sad, Angry) and type your message. Adjust the temperature slider "
        "to control the creativity of the AI's response. Perfect for experimenting with conversational AI that "
        "adapts to various emotional contexts!. "
        "This AI is powered by the **DialoGPT** model from Microsoft"
        
    ),
    flagging_mode="never",
)

# Launch the Gradio interface
iface.launch()
