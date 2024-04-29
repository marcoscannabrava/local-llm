# Useful Local LLM Scripts

## Magicoder
```sh
# Usage:
alias magicoder=source <PATH_TO>/magicoder.sh

# Run LLM Inference Server
magicoder

# Query LLM
@l "example of Python reduce function"
@l "how to create a linked list in Rust"
@l "how to center a div"

# Kill LLM Server
@lk
```

### Pre-Requisites
- GPU with at least 8GB
- miniconda
- zsh
- conda environment with vllm installed

```sh
conda create -n vllm python=3.9 -y
conda activate vllm
pip install vllm
```