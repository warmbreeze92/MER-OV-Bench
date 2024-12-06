import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from modelscope import AutoModelForCausalLM, AutoTokenizer

# def load_model(model_name):
#     # 加载 tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(model_name)

#     # 加载模型
#     model = AutoModelForCausalLM.from_pretrained(model_name)
#     print(model)

#     return tokenizer, model

# load_model("google-bert/bert-base-uncased")


model_name = "LLM-Research/Llama-3.2-1B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
print(model)