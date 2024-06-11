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
    
    # Modificar a mensagem aqui
    modified_message = msg.payload.decode() + " - mensagem modificada"
    
    # Publicar a mensagem modificada em outro tópico
    client.publish(modified_topic, modified_message)
    print(f"Mensagem modificada enviada para {modified_topic}: {modified_message}")
# Criando o cliente MQTT e configurando os callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Conectando ao broker
client.connect(broker, port, 60)
# Mantendo a conexão aberta
client.loop_forever()
