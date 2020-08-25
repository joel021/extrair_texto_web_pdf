from text_to_json import TextToJson
#estrator de textos da web de páginas web ou pdfs mesmo.
#Para usar, basta escrever uma lista de links,autor em um arquivo txt separados com enter
#Um exemplo de entrada está na página inputs

text_to_json = TextToJson()
#portugues
text_to_json.from_pdf("inputs/pt/pdfs.txt",'pt') #extrair textos em português dos links contigos em pdfs.txt
text_to_json.from_web("inputs/pt/web.txt",'pt')   #extrair texto em português dos links contidos em web.txt

#ingles
text_to_json.from_pdf("inputs/en/pdfs.txt",'en') #extrair textos em ingles dos links contigos em pdfs.txt
text_to_json.from_web("inputs/en/web.txt",'en') #extrair texto em ingles dos links contidos em web.txt

#os resultados ficam na pasta outputs em arquivos jsos
#a lingua de tradução pode ser muito bem escolhida apenas modificando a classe...