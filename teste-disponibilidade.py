import paho.mqtt.client as mqtt
import time
import threading
# Configurações do broker e tópico
broker = "broker.emqx.io"
port = 1883
topic = "teste-disponibilidade"
# Função de callback para conexão
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.connected_flag = True
    else:
        client.connected_flag = False
# Função de callback para quando a mensagem é publicada
def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")
# Função para publicar mensagens continuamente
def publish_messages(client):
    while client.connected_flag:
        client.publish(topic, "Teste de disponibilidade")
        time.sleep(0.01)  # Ajuste a frequência conforme necessário
# Configura o cliente MQTT
mqtt.Client.connected_flag = False
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
# Conecta ao broker
client.connect(broker, port, 60)
# Inicia o loop de mensagens
client.loop_start()
while not client.connected_flag:  # Espera a conexão ser estabelecida
    print("Aguardando conexão...")
    time.sleep(1)
# Inicia a publicação de mensagens em um thread separado
thread = threading.Thread(target=publish_messages, args=(client,))
thread.start()
# Mantém o script rodando para monitorar a disponibilidade
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Teste interrompido pelo usuário.")
finally:
    client.loop_stop()
    client.disconnect()
