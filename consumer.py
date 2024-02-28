import pika
import subprocess   #farklı bir py uzantılı dosyayı çağırmak için kullanabilirim
def messageCallBack(ch,method,properties,body):
    print(f"received new message: {body}")
    #print("Script yazsam?")
    #subprocess.run(["python","script.py"])



#conenction parametreleri producer'ın aynısı

connectionParameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connectionParameters)
channel=connection.channel()


channel.queue_declare(queue='deneme')
#ilk başta producerda oluşturduğumuz için rabbitmq kendisi otomatik
#olarak queuyu tanıyacak ikinci bir queue oluşturmayacak aslında burada ayrıca queue oluşturmama gerek yok
#basic consume methodunda zaten o queue name belirledim.

channel.basic_consume(queue='deneme',auto_ack=True,on_message_callback=messageCallBack)
#rabbitmq'nun queue ya bağlanıp mesajı alması

print("Starting consuming")

channel.start_consuming()
