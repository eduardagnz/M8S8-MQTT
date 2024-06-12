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
O objetivo deste ataque é comprometer a confidencialidade dos dados trafegados pelo broker MQTT. Isso é feito interceptando as mensagens publicadas em um tópico, modificando-as e republicando-as em um tópico clone. Dessa forma, o atacante pode expor informações sensíveis ou repassar dados confidenciais sem autorização. Simulamos cenário com invasão de um broker e colocar um tópico para ouvir todas as mensagens, para quebrar a confidencialidade, aplicamos uma lóciga com automação onde toda mensagem que chegasse no tópico invadido ele deveria escrever a mensagem no tópico criado, afim de que tivessemos acesso as mensagens enviadas. 

## Conexão Necessária
Para realizar este ataque, foi necessário:

1. Ter acesso a um broker público MQTT, neste caso, broker.emqx.io.
2. Conectar a este broker usando o protocolo MQTT na porta padrão (1883).
3. Inscrever-se em um tópico específico e interceptar as mensagens publicadas.
4. Modificar o conteúdo dessas mensagens e republicá-las em um tópico clone.

## Sprit utilizado 
O código utilizado esta contido no arquivo python "teste-confidencialidade.py"

## Resultado 
O resultado esperado deste ataque é que qualquer mensagem original publicada no tópico teste-integridade será interceptada,e republicada no tópico clone-teste-integridade. Isso compromete a confidencialidade dos dados, pois as informações podem ser expostas ou repassadas para outros tópicos sem o conhecimento dos remetentes ou destinatários. Para esse teste, conseguimos implementar com um broker público "broker.emqx.io" 

# Ataque que impacta a integridade
## Objetivo do ataque 
O objetivo deste ataque é comprometer a integridade dos dados trafegados pelo broker MQTT. Isso é feito interceptando, modificando e republicando mensagens em um tópico específico, de forma que os dados originais sejam alterados sem o conhecimento dos remetentes ou destinatários legítimos.

## Conexão Necessária
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
Os ataques demonstrados—comprometimento de disponibilidade, integridade e confidencialidade—evidenciam vulnerabilidades críticas em sistemas baseados em MQTT. O ataque de disponibilidade, por exemplo, envolveu a publicação de mensagens em alta frequência para sobrecarregar o broker MQTT. Esse tipo de ataque pode resultar em um aumento significativo na latência das mensagens, possível queda do broker devido à sobrecarga e indisponibilidade temporária do serviço para outros clientes conectados.
Para proteger sistemas contra esses ataques, é fundamental adotar uma abordagem de segurança em camadas desde a fase de arquitetura do sistema. Isso inclui planejamento de segurança, tecnicas arquiteturais consolidadas, implementação de autenticação forte e controles de acesso rigorosos, uso de criptografia para proteger dados em trânsito e em repouso, e configuração de sistemas de monitoramento para detectar atividades anômalas. Integrando essas práticas de segurança na arquitetura do sistema, é possível mitigar significativamente os riscos associados aos ataques de disponibilidade, integridade e confidencialidade, garantindo um sistema mais seguro e confiável.
