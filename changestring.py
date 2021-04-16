import argparse
import os
import re

# changestring -d DIRETORIO -s PALAVRASOURCE -c NEWPALAVRA
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", help="Diretorio", default=".")
parser.add_argument("-s", "--word-source", help="Palavra origem")
parser.add_argument("-c", "--word-dest", help="Palavra destino")
args = parser.parse_args()


if args.dir is None or args.word_source is None or args.word_dest is None:
    print(f"Parametros passados incorretamente")
    print(f"{os.sys.argv[0]} -d <diretorio> -s <palavra_origem> -c <palavra_destino>")
    exit(1)
    
directory = os.listdir(args.dir)
os.chdir(args.dir)

for file in directory:
    try:
        if os.path.isdir(file):
            print(f"É um diretório, o mesmo não sera tratado: {file}")
            continue
        open_file = open(file,'r')
        read_file = open_file.read()
        regex = re.compile(args.word_source)
        read_file = regex.sub(args.word_dest, read_file)
        write_file = open(file,'w')
        write_file.write(read_file)
        print(f"Arquivo alterado com sucesso: {file}")
    except Exception as e:
        print(f"Excessão não mapeada. Arquivo: {file} - Erro: {e}")
        exit(1)
