from time import sleep
from slackclient import SlackClient

token = os.getenv('TOKEN', input('Please enter a bot token.')) # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect() == True:
  print('Connected.')
  while True:
    response = sc.rtm_read()
    for part in response:
      if part['type'] == 'message':
        if part['text'].lower().startswith('echo: '):
          sc.api_call("chat.postMessage", channel="#squad-slackbot", text=part['text'][len('echo: '):], username='echobot', icon_emoji=':robot_face:')
    sleep(1)
else:
  print('Connection Failed, invalid token?')