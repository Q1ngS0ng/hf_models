export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --repo-type dataset --resume-download gretelai/synthetic_text_to_sql --local-dir gretelai/synthetic_text_to_sql
huggingface-cli download --repo-type dataset --resume-download yiting/UnsafeBench --local-dir yiting/UnsafeBench