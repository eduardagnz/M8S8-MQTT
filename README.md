# M8S8-MQTT
Atividade ponderada M8 - Semana 8
## Objetivo da atividade 
Fazer a conexão com o broker público MQTT utilizando algum identificador aleatório; Escolhendo algum nome único para seu tópico; Um dos integrantes da dupla deve se subscrever no tópico; O outro integrante irá publicar mensagens neste tópico; Agora, utilizem o MQTT para simular os ataques que impactam confidencialidade, integridade e disponibilidade; Faça um relatório técnico descrevendo os resultados obtidos.


*Descrição dos ataques*  
# Ataque que impacta a disponibilidade 
## Objetivo do ataque 
Buscamos atacar a disponibilidade com um ataque em massa no broker público, para isso, utilizamos um DOS ( ), assim colocando várias requisições, escrevendo várias mensagens para que houvesse um comportamento anomal. O objetivo deste ataque é comprometer a disponibilidade do serviço MQTT ao sobrecarregar o broker com uma alta frequência de mensagens publicadas. Isso pode causar lentidão, aumentar a latência das mensagens ou até mesmo fazer com que o broker fique indisponível para outros usuários.

## Conexão Necessária
Para realizar este ataque, foi necessário:
1. Ter acesso a um broker público MQTT, neste caso, broker.emqx.io.
2. Conectar a este broker usando o protocolo MQTT na porta padrão (1883).
3. Publicar mensagens de maneira contínua e rápida em um tópico específico.

## Sprit utilizado 
O código utilizado esta contido no arquivo python "teste-disponibilidade.py"

## Resultado 
Nosso objetivo de sobrecarregar, percebemos que ao jogar um número alto de requisições, todas estavam sendo recebidas e sendo processadas. Como alternativa, tivemos um segundo *client* para receber essa sobrecarga mas para ele as mensagens iam chegando em blocos, ou seja, a cada 1 segunda eram recebidas 5 mensasgens. Com a falha do nosso testes, percebemos a importância de uma arquitetura consolidada para diversos cenários, incluindo a sobrecarga, com o comportamento dos resultados entendemos que há uma fila para consumir, já que foi colocado mais de 15 mil requisições em curto período de tempo e o broker conseguir consumi-las.
![Image](https://github.com/Inteli-College/2024-1B-T06-ES08-G01/assets/99493861/297779f6-ef4b-43a1-a3c8-c1d328d21b1e)



# Ataque que impacta a confidencialidade
## Objetivo do ataque 
Buscamos atacar a disponibilidade com um ataque em massa no broker público, para isso, utilizamos um DOS ( ), assim colocando várias requisições, escrevendo várias mensagens para que houvesse um comportamento anomalo 

## Sprit utilizado 

## Resultado 


# Ataque que impacta a integridade
## Objetivo do ataque 
O objetivo deste ataque é comprometer a integridade dos dados trafegados pelo broker MQTT. Isso é feito interceptando, modificando e republicando mensagens em um tópico específico, de forma que os dados originais sejam alterados sem o conhecimento dos remetentes ou destinatários legítimos.

Conexão Necessária
Para realizar este ataque, foi necessário:

1. Ter acesso a um broker público MQTT, neste caso, broker.emqx.io.
2. Conectar a este broker usando o protocolo MQTT na porta padrão (1883).
3. Inscrever-se em um tópico específico e interceptar as mensagens publicadas.
4. Modificar o conteúdo dessas mensagens e republicá-las no mesmo tópico ou em um tópico clone.

## Sprit utilizado 
O código utilizado esta contido no arquivo python "teste-integridade.py"

## Resultado 
Como resultado, não foi possível por utilização do debug viamos que a mensagem havia sido alterada, mas para o client, ele recebia as mensagens sem alteração. Por uma análise, acreditamos que exista um mecanismo de validação que força a mensagem correta ser enviada. 


# Conclusão 

