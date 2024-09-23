# Projeto do Curso de Python do Bruce Fonseca
### Este protejo foi baseado em um exercício do módulo de Python do curso do Bruce Fonseca
- 📚 Contexto: No **módulo 07. Funções**, mais especificamente na aula **10. Criando funções - parte 3**, o professor Bruce demonstra, por meio de código, como as funções permitem reutilizar o mesmo código sem necessidade de repeti-lo. Ele apresenta um exemplo simples e didático: uma empresa fictícia de serviços de manutenção. Nesse exemplo, ele lê um dicionário e utiliza uma lista como parâmetro para uma função. A função, por sua vez, aplica um laço de repetição (`for`) para calcular o custo e o tempo do pedido, e ao final, imprime o resultado com algumas informações adicionais.

    Abaixo está o código final produzido por ele:

    > Código final
    ```python
    pedido_servico = ["Troca de óleo", "Bateria"]
    
    custo_total = calcular_preco_pedido_manutencao(pedido_servico)
    tempo_total = calcular_tempo_pedido_manutencao(pedido_servico)
    
    print("BRUCE_CAR AUTO CENTER")
    print("-------------------------------------")
    print("Itens de manutenção:")
    for item in pedido_servico:
        print(f"{item} = R$ {precos_manutencao[item]} +- {tempo_manutencao[item]} min.")
    print("-------------------------------------")
    print(f"Valor total = R$ {custo_total}")
    print(f"Tempo total = {tempo_total} min")
    ```
    > Resultado
    ```
    BRUCE_CAR AUTO CENTER
    -------------------------------------
    Itens de manutenção:
    Troca de óleo = R$ 50 +- 30 min.
    Bateria = R$ 100 +- 60 min.
    -------------------------------------
    Valor total = R$ 150
    Tempo total = 90 min
    ```
- 🎯 Objetivo do projeto: O objetivo deste projeto é utilizar essa estrutura, dando "vida" ao código e simulando uma loja virtual real. Para isso, apliquei conceitos do paradigma de programação funcional, além de utilizar a biblioteca Streamlit para possibilitar a interação com o usuário, simulando ao máximo a experiência de um site verdadeiro.
    > Projeto finalizado
      ![Imagem do projeto finalizado](Projeto%20Streamlit%20finalizado.png)
- 🔗 Mais informações: No meu linkedin criei uma publicação onde explico toda a construção desse projeto, desde o processo de planejamento da solução até o desenvolvimento, confere lá😉: <br>
      [1ª Publicação](https://www.linkedin.com/posts/bruno-pereira-de-oliveira_ol%C3%A1-rede-depois-de-pouco-mais-de-2-meses-activity-7202726667612524544-kAHE?utm_source=share&utm_medium=member_desktop) <br>
      [2ª Publicação](https://www.linkedin.com/posts/bruno-pereira-de-oliveira_streamlit-python-activity-7205251367060283394-BHD2?utm_source=share&utm_medium=member_desktop) <br>

