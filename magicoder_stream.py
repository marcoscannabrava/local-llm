from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_name_or_path = "TheBloke/Magicoder-S-DS-6.7B-AWQ"
device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    low_cpu_mem_usage=True,
    device_map=device,
)

# Using the text streamer to stream output one token at a time
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "example of Python reduce function"
prompt_template=f'''You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{prompt}

@@ Response
'''

# Convert prompt to tokens
tokens = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()

generation_params = {
    "do_sample": True,
    "temperature": 0.1,
    "top_p": 0.95,
    "top_k": 40,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}

# Generate streamed output, visible one token at a time
model.generate(
    tokens,
    streamer=streamer,
    **generation_params,
    pad_token_id=tokenizer.eos_token_id
)
