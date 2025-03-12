import gradio as gr
from DeepSeek import reviewCode

def codeReviewerUI(code):
    return reviewCode(code)

interface = gr.Interface(
    fn = codeReviewerUI,
    inputs = gr.Code(language='python', lines= 20, label="Paste your code here"),
    outputs = gr.Textbox(label = "Revision"),
    title = "Code reviewer assitant",
    description = "Analyze your code snippets, receive feedback, and discover improvements."
)

interface.launch(share = True)