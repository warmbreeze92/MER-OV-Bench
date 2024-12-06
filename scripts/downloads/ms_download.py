import os
import argparse
from modelscope.hub.snapshot_download import snapshot_download

def download(model_id, revision, allow_patterns, ignore_patterns):
    
    print(f"正在下载模型: {model_id} (分支: {revision} )")
    
    # 下载模型文件   
    try:
        snapshot_download(
        model_id=model_id,
        revision=revision,
        allow_patterns=allow_patterns,
        ignore_patterns=ignore_patterns
        )
        print(f"模型文件下载完成")
    except Exception as e:
        print(f"下载失败: {e}")


def main():
    parser = argparse.ArgumentParser(description="下载 Hugging Face 模型或数据集")
    
    # 相关参数
    parser.add_argument("--model_id", type=str, help="要下载的模型的ID")
    parser.add_argument("--revision", type=str, default=None, help="模型/数据集的分支或版本（默认: None）")
    parser.add_argument("--allow_patterns", type=str, nargs='*', default=None, help="要包含的文件或列列表（空格分隔）")
    parser.add_argument("--ignore_patterns", type=str, nargs='*', default=None, help="要排除的文件或列列表（空格分隔）")

    args = parser.parse_args()
    
    download(args.model_id, args.revision, args.allow_patterns, args.ignore_patterns)

if __name__ == "__main__":
    main()

# example
# python ms_download.py --model_id LLM-Research/Llama-3.2-1B-Instruct
