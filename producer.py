import pika

connectionParameters=pika.ConnectionParameters('localhost')
#Pika kütüphanesini kullanarak localde çalışan rabbitmq sunucusuna bağlandım
#burası direkt bağlantı sağlamıyor sadece sunucu konumu vb olarak düşünebilirim


connection=pika.BlockingConnection(connectionParameters)
#Burada bağlantıyı direkt olarak kurdum.
#BlockingConnection bağlantı kurulana kadar bir sonraki adıma geçmez
#Burada  bağlantı başarılı olursa connection değişkenine otomatik olarak
#bir bağlantı nesnesi atanır ve bu nesneyi kullanarak mesaj alma ve verme gerçekleşir

channel=connection.channel()
#şimdi bir kanal oluşturdum.Kanallar sayesinde mesaj iletimi gerçekleşir
#Bir bağlantı üzerinde birden fazla kanal oluşturulabilir ve
#her kanal ayrı bir iletişim yolu sağlar
#Kanallar mesajlar arasında bağımsızlık sağlar ve
#aynı bağlantı üzerinde farklı işlemlerin paralel olarak gerçekleştirilmesine olanak tanır

channel.queue_declare(queue='deneme')
#burada artık bir tane queue oluşturdum

message="Deneme 1" #örnek mesaj

channel.basic_publish(exchange="",routing_key="deneme",body=message)
#mesajı queueya pushlamak için.
# exchange parametresi, mesajın iletilme mekanizmasını belirler
#ve mesajın nasıl işleneceğini kontrol ede
#burada defaul exchange kullandım o yüzden exchange kısmı boş
print(f"sent message: {message}")

connection.close()




