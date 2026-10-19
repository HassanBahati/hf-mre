# MRE for https://github.com/gradio-app/gradio/issues/13976
# gr.Audio rejects .ogg uploads when the browser reports a non-audio/* MIME type.
import gradio as gr

with gr.Blocks() as demo:
    audio = gr.Audio()

demo.launch()
