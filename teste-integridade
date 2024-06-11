import paho.mqtt.client as mqtt

# Configurações do broker
broker = 'broker.emqx.io'
port = 1883
topic = 'teste-integridade'
modified_topic = 'clone-teste-integridade'
# Callback quando a conexão com o broker for estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))
    client.subscribe(topic)
# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
    
    # Verificar e modificar a mensagem
    if msg.payload.decode() == "12345":
        modified_message = "6789"
        client.publish(topic, "fafa")
        print(f"Mensagem modificada enviada para {topic}: {modified_message}")
# Criando o cliente MQTT e configurando os callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Conectando ao broker
client.connect(broker, port, 60)
# Mantendo a conexão aberta
client.loop_forever()
