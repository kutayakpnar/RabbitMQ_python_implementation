import sys
import json
import csv
import os

def main():
    # Bayt nesnesini string olarak decode etme
    input_data = sys.stdin.read()



    data = json.loads(input_data)
    user=data.get("user")
    system=data.get("system")
    user=json.dumps(user)
    system=json.dumps(system)




    print("Received Data:")
    print(data);
    print("User:",user)
    print("System:",system)


    #str(json.dumps(user))
    with open('output.csv', 'a', newline='') as csvfile:
        #
        csv_writer = csv.writer(csvfile)

        # Verileri CSV dosyasına yazma

        csv_writer.writerow([user, system])  # Veri satırı

    # Kaydedilen dosyanın tam yolunu almak için
    file_path = os.path.abspath('output.csv')
    print(f"Data written to: {file_path}")


if __name__ == "__main__":
    main()



