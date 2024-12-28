# Consider using this https://github.com/meta-llama/llama-models
# https://github.com/meta-llama/llama-models/blob/main/models/scripts/example_text_completion.py

# Copyright (c) Meta Platforms, Inc. and affiliates.

from typing import Optional

import fire

from llama_models.llama_models.llama3.reference_impl.generation import Llama
from termcolor import cprint


def run_main(
    ckpt_dir: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 4,
    max_gen_len: int = 64,
    model_parallel_size: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
        model_parallel_size=model_parallel_size,
    )

    prompts = [
        "The color of the sky is blue but sometimes it can also be",
        """\
apple is pomme,
bannana is banane,
cherry is""",
        "1, 2, 3, 5, 8, 13",
        "ba ba black sheep, have you any wool?",
    ]
    for prompt in prompts:
        result = generator.text_completion(
            prompt,
            temperature=0.6,
            top_p=0.9,
            max_gen_len=max_gen_len,
            logprobs=False,
        )

        cprint(f"{prompt}", end="")
        cprint(f"{result.generation}", color="yellow")
        print("\n==================================\n")


def main():
    fire.Fire(run_main)


if __name__ == "__main__":
    main()