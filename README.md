# Useful Local LLM Scripts

## Usage

Single prompt
```sh
# Usage:
function @l() {
    conda activate coder-slm
    python $HOME/path_to/local-llm/qwen.py $@
    conda deactivate
}

# Query LLM
@l "example of Python reduce function"
@l "linked list in Rust"
@l "how to center a div"
```

Serve via OpenAI compatible API server on localhost:8000
```sh
vllm serve deepseek-ai/deepseek-coder-1.3b-instruct --trust-remote-code --max-model-len=8000 --api-key=123 

# optionally to test it with aider
export OPENAI_API_BASE=http://0.0.0.0:8000/v1
export OPENAI_API_KEY=123
aider --model openai/deepseek-ai/deepseek-coder-1.3b-instruct
```

![example](example.png)


### Pre-Requisites
- GPU with at least 8GB
- miniconda
- conda environment with vllm installed

```sh
conda create -n coder-slm python=3.12 -y
conda activate coder-slm
pip install vllm
```

# Resources
https://aider.chat/
https://docs.vllm.ai
https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct