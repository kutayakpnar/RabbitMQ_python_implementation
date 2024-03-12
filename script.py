import sys
import json

def main():
    # Bayt nesnesini string olarak decode etme
    input_data = sys.stdin.read()


     # Gelen JSON verisini bir Python sözlüğüne dönüştür
    data = json.loads(input_data)
    user=data["user"]
    system=data["system"]


    # JSON verisini işleme örnekleri
    print("Received Data:")
    print("User:",user)
    print("System:",system)


    #str(json.dumps(user))


if __name__ == "__main__":
    main()



