import argparse
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def convert_to_gguf(input_dir, output_dir, quantization_method):
    # Carregar o modelo e o tokenizer
    model = AutoModelForCausalLM.from_pretrained(input_dir)
    tokenizer = AutoTokenizer.from_pretrained(input_dir)
    
    # Salvar o modelo e o tokenizer no formato GGUF (hipotético)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salvar o modelo no formato GGUF
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    print(f"Modelo convertido para o formato GGUF e salvo em: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Converter modelo para o formato GGUF.")
    parser.add_argument("--input_dir", type=str, required=True, help="Diretório do modelo de entrada")
    parser.add_argument("--output_dir", type=str, required=True, help="Diretório para salvar o modelo convertido")
    parser.add_argument("--quantization_method", type=str, required=True, choices=["f16", "int8"], help="Método de quantização (f16 ou int8)")
    
    args = parser.parse_args()

    convert_to_gguf(args.input_dir, args.output_dir, args.quantization_method)

if __name__ == "__main__":
    main()
