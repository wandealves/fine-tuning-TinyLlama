# fine-tuning-TinyLlama

Ajuste fino usando o modelo TinyLlama

Comando:

python convert_to_gguf.py --input_dir caminho_para_salvar_o_modelo --output_dir caminho_para_o_modelo_gguf --quantization_method f16

Exemplo:

python convert_to_gguf.py --input_dir model-tiny --output_dir model-tiny.gguf --quantization_method f16
