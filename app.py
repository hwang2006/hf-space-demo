# Import libraries
import gradio as gr
from transformers import pipeline

# Create a summarization pipeline
summarizer = pipeline("summarization")

# Define a function that takes a text and returns a summary
def summarize(text):
  summary = summarizer(text, max_length=200, min_length=40, do_sample=False)[0]
  return summary["summary_text"]

# Create a Gradio interface
interface = gr.Interface(
  fn=summarize, # the function to wrap
  inputs=gr.Textbox(lines=10, label="Input Text"), # the input component
  outputs=gr.Textbox(label="Summary") # the output component
)

# Launch the interface
interface.launch()