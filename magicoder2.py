from vllm import LLM, SamplingParams
import sys

prompt = " ".join(sys.argv[1:])
prompt_template=f'''You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{prompt}

@@ Response
'''

sampling_params = SamplingParams(
    n=1,
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    max_tokens=512,
    repetition_penalty=1.1,
    skip_special_tokens=True
)

llm = LLM(
    model="TheBloke/Magicoder-S-DS-6.7B-AWQ",
    quantization="awq",
    dtype='half',
    device="cuda",
    gpu_memory_utilization=0.9,
    max_model_len=1024,
)

outputs = llm.generate(prompt_template.format(prompt=prompt), sampling_params, use_tqdm=False)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    for t in generated_text.split('\n'):
        print(t)
