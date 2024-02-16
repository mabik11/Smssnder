from twilio.rest import Client

def send_sms(account_sid, auth_token, from_number, to_number, message_body):
    # Twilio Client'ı oluşturun
    client = Client(account_sid, auth_token)

    # SMS gönderme
    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )

    print("SMS gönderildi! SID:", message.sid)

def read_credentials(file_path):
    # Dosyadan API anahtarlarını ve telefon numarasını oku
    with open(file_path, 'r') as file:
        lines = file.readlines()
        account_sid = lines[0].strip()
        auth_token = lines[1].strip()
        from_number = lines[2].strip()
        to_number = lines[3].strip()
    return account_sid, auth_token, from_number, to_number

if __name__ == "__main__":
    # API anahtarlarını ve telefon numarasını dosyadan oku
    credentials_file = "credentials.txt"
    account_sid, auth_token, from_number, to_number = read_credentials(credentials_file)

    # Gönderilecek mesajı kullanıcıdan al
    message_body = input("Göndermek istediğiniz mesajı yazın: ")

    # SMS gönderme işlemi
    send_sms(account_sid, auth_token, from_number, to_number, message_body)
