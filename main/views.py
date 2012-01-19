# Sample Python webservice for SMSsync
# Developed by Caine Wanjau
# For inquiries contact caine@faidika.co.ke
#
# Comment snippets adapted from sample php webservice at http://smssync.ushahidi.com/doc

from django.http import HttpResponse
from django.utils import simplejson
from django.conf import settings

import os

def smssync(request):
    
    if request.method == 'POST':
        
        #get the phone number that sent the SMS.
        
        if "from" in request.POST and request.POST["from"]:
            
            num_from = request.POST["from"]
        
        
        # get the SMS aka message sent
        
        if "message" in request.POST and request.POST["message"]:
            
            message = request.POST["message"]
            
        
        # set success to true
        
        success = "true"
        
        # in case a secret has been set at SMSSync side, 
        # get it for match making
        
        if "secret" in request.POST and request.POST["secret"]:
            
            secret = request.POST["secret"]
        
            
        # get the timestamp of the SMS
        
        if "sent_timestamp" in request.POST and request.POST["sent_timestamp"]:
            
            sent_timestamp = request.POST["sent_timestamp"]
        
        
        if "sent_to" in request.POST and request.POST["sent_to"]:
            
            sent_to = request.POST["sent_to"]
            
        
        if "message_id" in request.POST and request.POST["message_id"]:
            
            message_id = request.POST["message_id"]
        else:
            message_id = 0
        
        
        # We have have retrieved the data sent over by SMSSync 
        # via HTTP. next thing to do is to do something with 
        # the data. Either echo it or write to a file or even 
        # store it in a database. This is entirely up to you. 
        # After, return a JSON string back to SMSSync to know 
        # if the web service received the message successfully. 
        
        # In this demo, we are just going to send a success or false reply to SMSsync.
        
        
        if len(num_from) > 0 and len(message) > 0 and len(sent_timestamp) > 0 and len(sent_to) > 0:
            if secret != "123456":
                
                success = "false"
                
            string = "From : %s\n" %(num_from)
            string += "Message: %s\n" %(message)
            string += "Timestamp: %s\n" %(sent_timestamp)
            string += "Message Id: %s\n" %(message_id)
            string += "Sent to: %s\n\n\n" %(sent_to)
            
            
            writefile = "log.txt"
            
            fh = open(os.path.join(settings.MEDIA_ROOT, writefile), 'a')
            
            fh.write(string)
            
            fh.close()
            
        else:
            success = "false"
            
        reply = {"payload":{"success": success}}
        
        return HttpResponse(simplejson.dumps(reply),mimetype="application/json")

