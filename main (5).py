pontuacao = 0

print("🟢 Bem-vindo(a) ao Quiz do Shrek! Responda com A, B, C ou D.\n")

# Pergunta 1
resposta = input("1) Qual o melhor filme do Shrek?\nA) Shrek 1\nB) Shrek 2\nC) Shrek 3\nD) Shrek 5\nResposta: ").strip().upper()
if resposta == "B":
    print("✅ Você sabe das coisas, meu querido!")
    pontuacao += 1
else:
    print("❌ Resposta errada. O correto é B) Shrek 2.")

# Pergunta 2
resposta = input("\n2) Qual o nome do burro no filme?\nA) Burro\nB) Asno\nC) Cavalo\nD) Bobinho\nResposta: ").strip().upper()
if resposta == "A":
    print("✅ Exatamente! Simples e direto: Burro.")
    pontuacao += 1
else:
    print("❌ Errado! O nome é Burro mesmo.")

# Pergunta 3
resposta = input("\n3) Quem Shrek se casa?\nA) Rapunzel\nB) Fiona\nC) Cinderela\nD) Branca de Neve\nResposta: ").strip().upper()
if resposta == "B":
    print("✅ Boa! A princesa ogra mais linda.")
    pontuacao += 1
else:
    print("❌ Nããão... é a Fiona!")

#Pergunta 4
resposta = input("\n4) Qual o nome do filho da fada Madrinha? \nA)Miguel \nB)Geraldo\nC)Encantado\nD)Arturo\nResposta:").strip().upper()
if resposta == "C":
    print("✅ Boa! O nome do filho da fada Madrinha é Encantado.")
    pontuacao += 1
else:
    print("❌ Nããão... é o Encantado!")
#Pergunta 5
resposta = input("\n5) O gato do filme que acessorio ele usa?\nA)Oculos\nB)Chapéu\nC)Gravata\nD)Cinto\nResposta :").strip().upper()
if resposta == "B":
    print("✅ Boa! O gato usa um chapéu.")
    pontuacao += 1
else:
    print("❌ Nããão... é o chapéu!")

# Resultado final
print(f"\n🏁 Fim do quiz! Sua pontuação final foi: {pontuacao}/5")
