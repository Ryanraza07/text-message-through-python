#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install twilio


# In[12]:


from twilio.rest import Client
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client('your_account_sid','your_auth_token')

to_phone_number = '+1234567890'  
message_body = 'Hello, this is a test message from Python!'


message = client.messages.create(
    body=message_body,
    from_='+12564459689',  
    to=to_phone_number
)


print(f"Message sent with SID: {message.sid}")


# In[ ]:





# In[ ]:




