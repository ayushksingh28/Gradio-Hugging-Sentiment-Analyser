# -*- coding: utf-8 -*-
"""Gradio and Hugging face.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHfGstfFieBLfx9FFIvoEpIMD0UtNTqP
"""

!pip install gradio
!pip install transformers

import gradio as gr
from transformers import pipeline

sentiment  = pipeline("sentiment-analysis")

def get_sentiment(input_text):
  return sentiment(input_text)

result = get_sentiment("The movie was very bad")

result

iface = gr.Interface(fn = get_sentiment, inputs = "text", outputs = ["text"],title ="Sentiment Analysis", description = "Get the sentiment of the text either Negative/Positive")

iface.launch(share=True)
