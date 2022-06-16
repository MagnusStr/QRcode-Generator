import qrcode

print("---------------------------")
print("     Qr Code Generator     ")
print("---------------------------")
entrada = input("Digite o endereço de link:")
img_qrcode = qrcode.make(entrada)
nomedoarquivo = input("Digite o nome do arquivo + extensão da imagem. Exemplo: 'arquivo.png':")
img_qrcode.save(nomedoarquivo)
