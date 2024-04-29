magicoder_chat() {
  if [ -z "$1" ]; then
    echo "Usage: @l <message>"
    echo "<message> should be the prompt sent to the model."
    return
  fi

  curl http://localhost:8999/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "TheBloke/Magicoder-S-DS-6.7B-AWQ",
    "messages": [
      {
        "role": "user",
        "content": "'$1'"
      }
    ]
  }' | jq '.choices[0].message.content' | sed 's/\\n/\
/g'
}

__conda_setup="$('$HOME/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
        . "$HOME/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="$HOME/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup

conda activate vllm
python -m vllm.entrypoints.openai.api_server --port 8999 --disable-log-stats --disable-log-requests --model TheBloke/Magicoder-S-DS-6.7B-AWQ --dtype half --max-model-len 4512 --quantization awq &
LLM_PID=$!

kill_llm() {
  kill $LLM_PID
}

alias @l=magicoder_chat
alias @lk=kill_llm

conda deactivate