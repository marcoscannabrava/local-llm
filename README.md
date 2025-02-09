# Local [DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct)

# Quickstart

1. Start llama.cpp or vLLM OpenAI-compatible Server
2. Use `llm` with the `llm-llamafile` plugin

```sh
# via llamafile
docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/models -p 8080:8080 ghcr.io/ggerganov/llama.cpp:server -m /models/hub/DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf -ngl 99

# OR via vLLM
docker run -d --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --max-model-len=8192 \
    --trust-remote-code \
    --gpu-memory-utilization=0.97 \
    --cpu-offload-gb=10 \
    --model deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct

# example usage
llm models default llamafile
llm "write a linked list in Rust"
```

# Requisites
- Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- Install [llm](https://github.com/simonw/llm) and [llm-llamafile plugin](https://github.com/simonw/llm-llamafile)


# Suggested usage

Add these commands to the aliases file sourced by .zshrc or your shell's .profile file.

```sh
# Download the GGUF model file for the model you want
# and put it in the ~/.cache/huggingface/hub folder
export DEFAULT_LLAMAFILE_MODEL="DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf"
function llm-serve {
    model=${1:-$DEFAULT_LLAMAFILE_MODEL}
    echo "Starting LLM server with model $model"
    if docker inspect $model > /dev/null 2>&1; then
        docker start $model
    else
        docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface/hub:/models -p 8080:8080 --name $model ghcr.io/ggerganov/llama.cpp:server -ngl 99 -m "/models/$model"
    fi
    llm models default llamafile
    until [[ $(curl -s localhost:8080/health | jq -r '.status') == "ok" ]]; do
        sleep 1
    done
    echo "LLM server is ready"
}

# Start server if not started
function @l() {
    if [[ $(curl -s localhost:8080/health | jq -r '.status') != "ok" ]]; then
        llm-serve
    fi
    llm $@
}
```

# Resources
[GitHub - ggerganov/llama.cpp: LLM inference in C/C++](https://github.com/ggerganov/llama.cpp)
[GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs](https://github.com/vllm-project/vllm)
[GitHub - simonw/llm: Access large language models from the command-line](https://github.com/simonw/llm)
[GitHub - simonw/llm-llamafile: Access llamafile localhost models via LLM](https://github.com/simonw/llm-llamafile)
