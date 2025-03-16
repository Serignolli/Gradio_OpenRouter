import gradio as gr
from OpenRouter import reviewCode
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

def codeReviewerUI(code, language):
    try:
        return reviewCode(code, language)
    except Exception as e:
        return f"**Erro:** {str(e)}"


LANGUAGES = ["python", "c", "cpp", "markdown", "json", "html", "css",
             "javascript", "jinja2", "typescript", "yaml", "dockerfile",
             "shell", "r", "sql", "sql-msSQL", "sql-mySQL", "sql-mariaDB",
             "sql-sqlite", "sql-cassandra", "sql-plSQL"]

with gr.Blocks() as interface:
    gr.Markdown("""
    # AI Code Reviewer & Explainer
    **Paste your code and get an AI-powered explanation, feedback, and suggestions for improvement.**
    """, elem_id="title")

    with gr.Row():
        language_dropdown = gr.Dropdown(
            choices=LANGUAGES, value="python", label="Choose the Programming Language"
        )

    with gr.Row():
        code_input = gr.Code(language="python", lines=20, label="Paste your code here")
        explanation_output = gr.Markdown(value="AI Analysis & Suggestions", min_height=50)

    with gr.Row():
        submit_button = gr.Button("Analyze Code", variant="primary")
        clear_button = gr.Button("Clear")


    def update_code_language(language):
        return gr.update(language=language)


    def clear_fields():
        return "", ""


    language_dropdown.change(update_code_language, inputs=[language_dropdown], outputs=[code_input])
    submit_button.click(codeReviewerUI, inputs=[code_input, language_dropdown], outputs=[explanation_output])
    clear_button.click(clear_fields, inputs=[], outputs=[code_input, explanation_output])


PORT = int(os.getenv("PORT", 7860))

@app.get("/")
async def root():
    return RedirectResponse(url="/gradio")

@app.get("/ads.txt")
async def ads():
    return FileResponse("ads.txt")

# Integrando Gradio ao FastAPI
app = gr.mount_gradio_app(app, interface, path="/gradio")
