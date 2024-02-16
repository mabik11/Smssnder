# Smssnder
This simple Python program allows you to send SMS messages using the Twilio API
# SMS Sending Application

This simple Python program allows you to send SMS messages using the Twilio API. The program reads Twilio API keys and the target phone number from a text file, and then prompts the user to enter a message, which is sent as an SMS using the provided information.

## Usage

1. First, install the `twilio-python` library:

pip install twilio

2. Next, clone this repo or download and extract the ZIP file:

git clone https://github.com/mabik11/smssnder.git

3. Once you've cloned the repo or extracted the ZIP file, navigate to the directory where the program is located:

cd smssnder

4. To run the program, create a text file named `credentials.txt` and add your Twilio API keys and target phone number in the following format:

YOUR_ACCOUNT_SID
YOUR_AUTH_TOKEN
YOUR_TWILIO_PHONE_NUMBER
RECIPIENT_PHONE_NUMBER

5. Finally, run the Python script to initiate the SMS sending process:

python snder.py

6. The program will prompt you to enter the message you want to send. Once you've entered the message and pressed ENTER, the SMS will be sent.
