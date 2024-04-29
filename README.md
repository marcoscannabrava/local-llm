# Useful Local LLM Scripts

## Magicoder
```sh
# Usage:
function @l() {
    conda activate magicoder
    python $HOME/code/local-llm/magicoder.py $@
    conda deactivate
}

# Query LLM
@l "example of Python reduce function"
@l "linked list in Rust"
@l "how to center a div"

```

### Pre-Requisites
- GPU with at least 8GB
- miniconda
- zsh
- conda environment with vllm installed

```sh
conda create -n magicoder python=3.9 -y
conda activate magicoder
pip install vllm
```