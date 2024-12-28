from vllm import LLM, SamplingParams
import sys

llm = LLM(model="Qwen/Qwen2.5-Coder-1.5B")

sampling_params = SamplingParams(temperature=0.7, top_p=0.8, max_tokens=2048)

if __name__ == "__main__":
    system_prompt = 'SYSTEM: You are a helpful coding assistant. Respond with just code.\n'
    
    if len(sys.argv) <= 1:
        example_for_debugging = 'boyer moore search function in C'
        print("Please provide a prompt as the first argument.")
        print(f"Running example prompt: {example_for_debugging}")
        prompt = system_prompt + example_for_debugging
    else:
        prompt = system_prompt + sys.argv[1]
    
    responses = llm.generate(prompt, sampling_params)
    for r in responses:
        print('\n\n')
        for o in r.outputs:
            print(o.text)