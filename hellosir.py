#!/usr/bin/env python3

import time
from twilio.rest import Client

accountSid = "CHANGEME"
authtoken = "CHANGEME"
voiceml="http://demo.twilio.com/docs/voice.xml"

# source phone number used to spam
# can use more than one source
# sourceNumbers = [ "+420111222333", "+44123654789", "+21563215654" ]

sourceNumbers = [ "+CHANGEME" ]

def callThem(toNumber, fromNumber):
    try:
       call = client.calls.create(
             to = toNumber,
             from_ = fromNumber,
             record = True,
             url = voiceml,
             method = "GET",
       )
       print("Spamming number {0} from number {1}".format(toNumber, fromNumber))
    except:
       print("Error, cannot spam number {0} from number {0}: {1}".format(toNumber, fromNumber, err))


print("****************************************")
print("*            Hello sir 0.1             *")
print("* call spammer for education purposes  *")
print("****************************************")
print("")
numToCall = input("Write target phone number and press ENTER: ")

client = Client(accountSid, authtoken)

count = 0
while True:
    count += 1
    print("Callspam n.{0} [ from number {1} ]".format(count, len(sourceNumbers)))

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber)
        time.sleep(1)
    time.sleep(1)


