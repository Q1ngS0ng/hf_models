export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --repo-type dataset --resume-download gretelai/synthetic_text_to_sql --local-dir gretelai/synthetic_text_to_sql
huggingface-cli download --repo-type dataset --resume-download yiting/UnsafeBench --local-dir yiting/UnsafeBench
huggingface-cli download --repo-type dataset --resume-download alexjercan/bugnet --local-dir alexjercan/bugnet

huggingface-cli download --repo-type dataset --resume-download ILSVRC/imagenet-1k --local-dir ILSVRC/imagenet-1k
