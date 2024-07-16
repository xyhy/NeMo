# This is here to import it once, which improves the speed of launch when in debug-mode
try:
    import transformer_engine  # noqa
except ImportError:
    pass

from nemo.collections.llm import peft, tokenizer
from nemo.collections.llm.api import export_ckpt, finetune, import_ckpt, pretrain, train, validate
from nemo.collections.llm.gpt.data import (
    DollyDataModule,
    FineTuningDataModule,
    MockDataModule,
    PreTrainingDataModule,
    SquadDataModule,
)
from nemo.collections.llm.gpt.data.api import dolly, mock, squad
from nemo.collections.llm.gpt.model import (
    CodeGemmaConfig2B,
    CodeGemmaConfig7B,
    CodeLlamaConfig7B,
    CodeLlamaConfig13B,
    CodeLlamaConfig34B,
    CodeLlamaConfig70B,
    GemmaConfig,
    GemmaConfig2B,
    GemmaConfig7B,
    GemmaModel,
    GPTConfig,
    GPTConfig5B,
    GPTConfig7B,
    GPTConfig20B,
    GPTConfig40B,
    GPTConfig126M,
    GPTConfig175B,
    GPTModel,
    Llama2Config7B,
    Llama2Config13B,
    Llama2Config70B,
    Llama3Config8B,
    Llama3Config70B,
    LlamaConfig,
    LlamaModel,
    MaskedTokenLossReduction,
    MistralConfig7B,
    MistralModel,
    MixtralConfig8x7B,
    MixtralModel,
    gpt_data_step,
    gpt_forward_step,
)
from nemo.collections.llm.gpt.model.api import (
    code_gemma_2b,
    code_gemma_7b,
    code_llama_7b,
    code_llama_13b,
    code_llama_34b,
    code_llama_70b,
    gemma,
    gemma_2b,
    gemma_7b,
    llama2_7b,
    llama2_13b,
    llama2_70b,
    llama3_8b,
    llama3_70b,
    mistral,
    mixtral,
)

__all__ = [
    "MockDataModule",
    "GPTModel",
    "GPTConfig",
    "gpt_data_step",
    "gpt_forward_step",
    "MaskedTokenLossReduction",
    "MistralConfig7B",
    "MistralModel",
    "MixtralConfig8x7B",
    "MixtralModel",
    "LlamaConfig",
    "Llama2Config7B",
    "Llama2Config13B",
    "Llama2Config70B",
    "Llama3Config8B",
    "Llama3Config70B",
    "CodeLlamaConfig7B",
    "CodeLlamaConfig13B",
    "CodeLlamaConfig34B",
    "CodeLlamaConfig70B",
    "LlamaModel",
    "GemmaConfig",
    "GemmaConfig2B",
    "GemmaConfig7B",
    "CodeGemmaConfig2B",
    "CodeGemmaConfig7B",
    "GemmaModel",
    "PreTrainingDataModule",
    "FineTuningDataModule",
    "SquadDataModule",
    "DollyDataModule",
    "train",
    "import_ckpt",
    "export_ckpt",
    "pretrain",
    "validate",
    "finetune",
    "tokenizer",
    "mock",
    "squad",
    "dolly",
    "mistral",
    "mixtral",
    "llama2_7b",
    "llama3_8b",
    "llama2_13b",
    "llama2_70b",
    "llama3_70b",
    "code_llama_7b",
    "code_llama_13b",
    "code_llama_34b",
    "code_llama_70b",
    "gemma",
    "gemma_2b",
    "gemma_7b",
    "code_gemma_2b",
    "code_gemma_7b",
    "peft",
]
