from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

def chat(input_text=None):
    history_string = "\n".join(conversation_history)

    input_text ="hello, how are you doing?"

    # tokenization of user prompt and chat history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # print(inputs)

    # you can lear more about tokens and their associated pretrained vocabulary files
    # this property provides a mapping of pretrained models to their corresponding vocabulary files
    tokenizer.pretrained_vocab_files_map

    # generate output from model
    outputs = model.generate(**inputs)
    # print(outputs)

    # decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    # print(response)

    # update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

def get_conversation_history():
    return conversation_history

# clear conversation history
def clear_history():
    conversation_history.clear()