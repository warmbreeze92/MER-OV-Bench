import os
import argparse
from huggingface_hub import hf_hub_download, snapshot_download

def download(token, repo_type, repo_id, revision, allow_patterns, ignore_patterns): #, cache_dir, local_dir):
    # 设置 HF_ENDPOINT 环境变量
    # os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    
    print(f"正在下载模型: {repo_id} (分支: {revision} )")
    
    # 下载模型文件   
    try:
        snapshot_download(
        token=token,
        repo_type=repo_type,
        repo_id=repo_id,
        revision=revision,
        allow_patterns=allow_patterns,
        ignore_patterns=ignore_patterns
        # cache_dir=cache_dir,
        # local_dir=local_dir
        )
        print(f"模型文件下载完成")
    except Exception as e:
        print(f"下载失败: {e}")


def main():
    parser = argparse.ArgumentParser(description="下载 Hugging Face 模型或数据集")
    
    # 相关参数
    parser.add_argument("--token", default=None, help="Hugging Face access token")
    parser.add_argument("--repo_type", type=str, choices=["model", "dataset"], default="model", help="下载类型: 'model' 或 'dataset'")
    parser.add_argument("--repo_id", type=str, help="要下载的模型/数据集的 Hugging Face Hub ID")
    parser.add_argument("--revision", type=str, default="main", help="模型/数据集的分支或版本（默认: main）")
    parser.add_argument("--allow_patterns", type=str, nargs='*', default=None, help="要包含的文件或列列表（空格分隔）")
    parser.add_argument("--ignore_patterns", type=str, nargs='*', default=None, help="要排除的文件或列列表（空格分隔）")
    # parser.add_argument("--local_dir", type=str, default="./cache", help="缓存目录（默认: ./cache）")
    # parser.add_argument("--cache_dir", type=str, default="./cache", help="缓存目录（默认: ./cache）")
    

    args = parser.parse_args()
    
    download(args.token, args.repo_type, args.repo_id, args.revision, args.allow_patterns, args.ignore_patterns)#, args.cache_dir, args.local_dir)

if __name__ == "__main__":
    main()

# example
# python hf_download.py --token "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" --repo_type model --repo_id google-bert/bert-base-uncased --ignore_patterns 'original/*' 
