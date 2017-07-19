import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
message = messages.GetLast()
body_content = message.body
with open('C:\\Users\\tushar.bhatt\\PycharmProjects\\pyStart\\journals\\plain_text.txt' , 'w+') as fin:
    fin.write(body_content)
    fin.close()

print("successful")


