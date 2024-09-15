$env:HF_ENDPOINT = "https://hf-mirror.com"
huggingface-cli download --resume-download  moka-ai/m3e-base  --local-dir moka-ai/m3e-base
huggingface-cli download --resume-download  tiiuae/falcon-mamba-7b-BF16-GGUF  --local-dir tiiuae/falcon-mamba-7b-BF16-GGUF
huggingface-cli download --resume-download  tiiuae/falcon-7b-instruct  --local-dir tiiuae/falcon-7b-instruct
huggingface-cli download --resume-download  Qwen/CodeQwen1.5-7B-Chat  --local-dir Qwen/CodeQwen1.5-7B-Chat
huggingface-cli download --resume-download  tiiuae/falcon-mamba-7b-instruct  --local-dir tiiuae/falcon-mamba-7b-instruct
