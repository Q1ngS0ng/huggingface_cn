#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # 设置hugging-face的国内镜像网站

from huggingface_hub import snapshot_download 

def downloader(model_name):
    while True: # 防止断联
        try:
            snapshot_download(
                repo_id=model_name,
                local_dir_use_symlinks=True,  # 在local-dir指定的目录中都是一些“链接文件”
                ignore_patterns=[],  # 忽略下载哪些文件
                local_dir=model_name,
                token="*************",   # huggingface的access token
                resume_download=True
            )
            break # 下载成功后跳出循环
        except:
            pass
    
if __name__ == "__main__":
    downloader(model_name)
