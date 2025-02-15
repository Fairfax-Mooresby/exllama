from model import ExLlama, ExLlamaCache, ExLlamaConfig
from tokenizer import ExLlamaTokenizer
from generator import ExLlamaGenerator
import torch

# Just a quick test to see if we are getting anything sensible out of the model.

torch.set_grad_enabled(False)
torch.cuda._lazy_init()

tokenizer_model_path = "/mnt/str/models/llama-7b-4bit-128g/tokenizer.model"
model_config_path = "/mnt/str/models/llama-7b-4bit-128g/config.json"
model_path = "/mnt/str/models/llama-7b-4bit-128g/llama-7b-4bit-128g.safetensors"

# tokenizer_model_path = "/mnt/str/models/llama-13b-4bit-128g/tokenizer.model"
# model_config_path = "/mnt/str/models/llama-13b-4bit-128g/config.json"
# model_path = "/mnt/str/models/llama-13b-4bit-128g/llama-13b-4bit-128g.safetensors"
#
# tokenizer_model_path = "/mnt/str/models/llama-30b-4bit-128g/tokenizer.model"
# model_config_path = "/mnt/str/models/llama-30b-4bit-128g/config.json"
# model_path = "/mnt/str/models/llama-30b-4bit-128g/llama-30b-4bit-128g.safetensors"

# tokenizer_model_path = "/mnt/str/models/llama-30b-4bit-128g-act/tokenizer.model"
# model_config_path = "/mnt/str/models/llama-30b-4bit-128g-act/config.json"
# model_path = "/mnt/str/models/llama-30b-4bit-128g-act/llama-30b-4bit-128g.safetensors"

config = ExLlamaConfig(model_config_path)
config.model_path = model_path
# config.attention_method = ExLlamaConfig.AttentionMethod.PYTORCH_SCALED_DP
# config.matmul_method = ExLlamaConfig.MatmulMethod.QUANT_ONLY
config.max_seq_len = 2048
model = ExLlama(config)
cache = ExLlamaCache(model)

tokenizer = ExLlamaTokenizer(tokenizer_model_path)
generator = ExLlamaGenerator(model, tokenizer, cache)

generator.settings.beams = 2
generator.settings.beam_length = 16

prompt = "Today is a good day to"

gen_tokens = 200

for i in range(gen_tokens):

    text = generator.generate_simple(prompt, max_new_tokens = gen_tokens)
    print(text)

