# Emotion-Based Conversational AI using Microsoft's DialoGPT

## Description

The **Emotion-Convo-AI-using-DialoGPT** is an interactive web application powered by the **DialoGPT** model from Microsoft. This app allows users to engage in conversations where the AI responds based on the emotional tone specified by the user. Whether you're feeling happy, sad, angry, surprised, excited, or neutral, the app generates a response tailored to your selected emotion. Users can also adjust the **temperature** to control the creativity of the AI's responses.

### Key Features:
- **Emotion-Based Response Generation**: Select an emotion (e.g., Happy, Sad, Angry) and get an AI response tailored to that emotion.
- **Interactive User Input**: Users can input text for the AI to respond to, based on the chosen emotional tone.
- **Temperature Control**: Adjust the temperature to control the randomness and creativity of the AI’s response.
- **Easy-to-Use Interface**: Built using **Gradio**, this app provides an intuitive and simple interface for interaction.

## Demo

You can interact with the AI by selecting an emotion, entering a text message, and adjusting the temperature to observe how the AI responds in different emotional tones.

### Example Usage:
1. **Select Emotion**: Choose between **Happy**, **Sad**, **Angry**, **Surprised**, **Excited**, and **Neutral**.
2. **Input Text**: Enter your message or question.
3. **Adjust Temperature**: Use the slider to set the temperature and influence the creativity of the response.

The app will generate and display a response based on the combination of your input, selected emotion, and temperature.

## Model Used
This app utilizes **DialoGPT**, a conversational AI model fine-tuned by Microsoft for generating human-like responses. Specifically, it uses the **DialoGPT-medium** model, which is well-suited for generating natural, contextually appropriate responses in a dialogue setting.

## Technologies Used

- **Gradio**: A Python library for building interactive web interfaces, allowing easy integration with machine learning models.
- **Hugging Face Transformers**: Provides pre-trained models like DialoGPT, enabling efficient natural language processing.
- **PyTorch**: Used for running the model and leveraging hardware acceleration like GPU for faster inference.
- **Microsoft DialoGPT**: The conversational model powering this app.
- **Python**: The primary programming language used to build the app.

## Installation

### Prerequisites

Ensure Python is installed. Then, clone the repository and install the required dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/karanheera/Emotion-Convo-AI-using-DialoGPT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Emotion-Convo-AI-using-DialoGPT
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
python app.py
```

The app will launch on your local server, typically accessible at [http://127.0.0.1:7860](http://127.0.0.1:7860/).

## File Structure

```plaintext
/Emotion-Based-AI-using-DialoGPT
│
├── app.py              # The main application file
├── CODE_OF_CONDUCT.md  # Code of conduct file
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # MIT License file
├── README.md           # This file
├── requirements.txt    # List of required Python libraries
```

## Usage

### Select Emotion
Choose the emotional tone from the dropdown, including options like **Happy**, **Sad**, **Angry**, **Surprised**, **Excited**, and **Neutral**.

### Enter User Input
Provide the input text, such as a statement or question, for which you want the AI to respond.

### Adjust Temperature
Use the **Temperature Slider** to control the creativity of the model’s responses. Higher values generate more creative and diverse responses, while lower values generate more predictable responses.

### Get AI Response
Once you’ve selected your emotion and entered your input, click the **Submit** button to receive an AI-generated response based on your settings.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project leverages the following libraries and technologies:

- **[DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium)**: A pre-trained conversational model from Microsoft fine-tuned for dialogue generation.
- **[Gradio](https://gradio.app/)**: A Python library for creating interactive machine learning demos.
- **[Transformers](https://huggingface.co/transformers/)**: Hugging Face’s library for accessing a variety of pre-trained models, including DialoGPT.
- **[PyTorch](https://pytorch.org/)**: A deep learning framework used for model execution and optimization.

Special thanks to **Microsoft** for providing the **DialoGPT** model, which powers this interactive conversational AI application.

## Contributing

Contributions are welcome! If you find a bug or have ideas for new features, feel free to fork the repository, create a new branch, and submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your forked repository.
4. Create a pull request with a clear explanation of your changes.

## Contact

For any questions or inquiries, feel free to reach out to the project maintainer:

**Karan Heera**  
- LinkedIn: [https://www.linkedin.com/in/karanheera/](https://www.linkedin.com/in/karanheera/)  
- GitHub: [https://github.com/karanheera](https://github.com/karanheera)
```

