### huggingface

```shell
## 指定镜像源网站
export HF_ENDPOINT=https://hf-mirror.com
## hf_transfer,并行下载，速度更快但只能同时下载一个文件，不稳定且无法resume,不推荐使用
export HF_HUB_ENABLE_HF_TRANSFER=1
## example
huggingface-cli download --token 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 --model meta-llama/Meta-Llama-3-8B-Instruct --exclude 'original/*' --local-dir /data1/models/Llama/Meta-Llama-3-8B-Instruct
```

### modelscope

```shell
## example
modelscope download --model LLM-Research/Meta-Llama-3-8B-Instruct --exclude 'original/*' --local_dir /data1/models/Llama/Meta-Llama-3-8B-Instruct
```
