import torch
import os
import gradio as gr
from langchain_openai import ChatOpenAI
from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize OpenAI Chat LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define prompt template using ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that analyzes meeting transcripts and extracts key points."),
    ("user", "List the key points with details from the context:\n\nContext: {context}")
])

# Create LCEL chain using the pipe operator
llm_chain = prompt_template | llm | StrOutputParser()

#######------------- Speech2text-------------####
def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    # Transcribe the audio file and return the result
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
    result = llm_chain.invoke({"context": transcript_txt})
    return result

#######------------- Gradio-------------####
audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()
iface = gr.Interface(fn= transcript_audio, 
                    inputs= audio_input, outputs= output_text, 
                    title= "Audio Transcription App",
                    description= "Upload the audio file")
iface.launch(server_name="0.0.0.0", server_port=7860)