import gradio as gr
from OpenRouter import reviewCode

# Function to process the input code based on language selection
def codeReviewerUI(code, language):
    return reviewCode(code, language)  # Modify reviewCode to handle different languages


# Available languages for selection
LANGUAGES = [
    "python", "javascript", "java", "c", "c++", "csharp", "go", "rust",
    "ruby", "swift", "kotlin", "typescript", "php"
]

# Gradio Interface
with gr.Blocks() as interface:
    gr.Markdown("# AI Code Reviewer & Explainer")
    gr.Markdown("Paste your code and get an AI-powered explanation, feedback, and suggestions for improvement.")

    with gr.Row():
        language_dropdown = gr.Dropdown(
            choices=LANGUAGES, value="python", label="Choose the Programming Language"
        )

    code_input = gr.Code(language="python", lines=20, label="Paste your code here")
    explanation_output = gr.Textbox(label="AI Analysis & Suggestions", lines=10)

    submit_button = gr.Button("Analyze Code")


    # Update the code input component dynamically when language changes
    def update_code_language(language):
        return gr.update(language=language)


    language_dropdown.change(update_code_language, inputs=[language_dropdown], outputs=[code_input])

    submit_button.click(codeReviewerUI, inputs=[code_input, language_dropdown], outputs=[explanation_output])

interface.launch(share=True)
