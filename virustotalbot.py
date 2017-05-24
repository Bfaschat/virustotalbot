#! /usr/bin/python
'''

      _             _       _        _   ___  ___ _____ 
 __ _(_)_ _ _  _ __| |_ ___| |_ __ _| | | _ )/ _ |_   _|
 \ V | | '_| || (_-|  _/ _ |  _/ _` | | | _ | (_) || |  
  \_/|_|_|  \_,_/__/\__\___/\__\__,_|___|___/\___/ |_|  
                                     |___|              
#############################
#### MALWAREVERSE BRASIL ####
#############################
Telegram: https://t.me/MalwareReverseBR
Blog: http://malwareverse.com
developed by @w00fx
<release 0.1>
'''

import time
import telepot
from telepot.loop import MessageLoop
import virustotal


def get_info(msg):
    v = virustotal.VirusTotal(
        'API VIRUS TOTAL HERE')
    report = v.get(msg)
    print(report)
    mensagem = ''
    mensagem += "\nReport da hash " + msg
    try:
        mensagem += "\n- Permalink: " + report.permalink
        mensagem += "\n- Status: " + report.status
        mensagem += "\n- Total de antivirus: " + str(report.total)
        mensagem += "\n- Antivirus detectados: " + str(report.positives)
        for antivirus, malware in report:
            if malware is not None:
                mensagem += '\n'
                mensagem += '\nAntivirus: ' + antivirus[0]
                mensagem += '\nMalware: ' + malware
        return mensagem
    except AttributeError:
        return 'Hash nao encontrada! Tente novamente.'


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Pego comando : %s' % command
    if '/hash' in command[:6] and len(command[6:]) == 32:
        bot.sendMessage(chat_id, get_info(command[6:]))
    else:
        bot.sendMessage(chat_id, 'Insira uma hash em seguida, ou insira uma hash valida!')

bot = telepot.Bot("TELEGRAM BOT ID HERE")

MessageLoop(bot, handle).run_as_thread()
print 'Estou escutando ...'

while 1:
    time.sleep(10)
