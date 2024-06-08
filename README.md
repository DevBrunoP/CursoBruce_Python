# CursoBruce_Python
### Este protejo foi baseado em um exercício do módulo de Python do curso do Bruce Fonseca
- 📚 Contexto: No **módulo 07. Funções**, mais especificamente na aula **10. Criando funções - parte 3** o professor Bruce demonstra em código a utilização das funções, e como elas permitem que o mesmo código seja reutilizado sem repeti-lo. Ele criou um exemplo de fácil compreensão: uma empresa fictícia de serviços de manutenção no qual lia um dicionário, usava como parâmetro para uma função uma lista, e aplicava no retorno um laço de repetição(`for`), ao final imprimia o resultado junto com alguns textos. Segue abaixo um exemplo de como ficou o código final que ele produziu:

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
- 🎯 Objetivo do projeto: Utilizar essa estutura porém dando "vida" ao projeto, simulando como se fosse realmente uma loja virtual. Para isso utilizei alguns conceitos do paradigma de programação funcioinal além da biblioteca Streamlit para conseguir a interação com usuário, simulando ao máximo a proximidade com um verdadeiro site.
    > Projeto finalizado
      ![Imagem do projeto finalizado](Projeto%20Streamlit%20finalizado.png)
- 🔗 Mais informações: No meu linkedin existe uma publicação que explica um pouco da construção do meu projeto, confere lá😉: [Publicação](https://www.linkedin.com/posts/bruno-pereira-de-oliveira_streamlit-python-activity-7205251367060283394-BHD2?utm_source=share&utm_medium=member_desktop)

