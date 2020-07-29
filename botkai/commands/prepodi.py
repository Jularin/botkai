from .. import classes as command_class
import random
import datetime
import json
import requests
from ..keyboards import getMainKeyboard
from ..classes import vk as vk
from ..classes import MessageSettings
from ..classes import UserParams
import traceback


chetn = UserParams.getChetn()
BASE_URL = 'https://kai.ru/raspisanie' 
prepodList = []

def info():


    group = UserParams.getGroup()
    id = MessageSettings.getId()
    #vk.method("messages.send",
    #        {"peer_id": id, "message": GetPrepodList() , "keyboard": getMainKeyboard(UserParams.role), "random_id": random.randint(1, 2147483647)})

    prepodList = GetPrepodList()
    try:
        raise Exception
        vk.method("messages.send",
            {"peer_id": id, "message": prepodList, "keyboard": getMainKeyboard(UserParams.role), "random_id": random.randint(1, 2147483647)})
    except:
        st = "&#128104;&#8205;&#127979;"
        b = 0
        i = 0
        for c in prepodList[1400:]:
            if i == len(st):
                print(i)
                b = 0
            if c == st[b]:
                
                print(c, " == ", st[b])
                b+=1
            else:
                b = 0
            i+=1
            

            


    #if len(prepodList) > 2400:
    #    vk.method("messages.send",
    #        {"peer_id": id, "message": prepodList[:3000] , "keyboard": getMainKeyboard(UserParams.role), "random_id": random.randint(1, 2147483647)})
    #    vk.method("messages.send",
    #        {"peer_id": id, "message": prepodList[3000:] , "keyboard": getMainKeyboard(UserParams.role), "random_id": random.randint(1, 2147483647)})
    #else:
    #    vk.method("messages.send",
    #        {"peer_id": id, "message": prepodList, "keyboard": getMainKeyboard(UserParams.role), "random_id": random.randint(1, 2147483647)})

    return "ok"


class Prepodi:
    def __init__(self):
       self.disciplType = ""
       self.disciplName = ""
       self.prepodName = ""







def GetPrepodList():
    prepodList.clear()
    groupId = UserParams.getGroup()
    try:
        response = requests.post( BASE_URL, data = "groupId=" + str(groupId), headers = {'Content-Type': "application/x-www-form-urlencoded"}, params = {"p_p_id":"pubStudentSchedule_WAR_publicStudentSchedule10","p_p_lifecycle":"2","p_p_resource_id":"schedule"}, timeout = 3 )
    except:
        return "&#9888; Возникла ошибка при подключении к серверам."
    #print("TEST")
    #print("Response: ", response.status_code)
    if str(response.status_code) != '200':
        return "&#9888; Возникла ошибка при подключении к серверам. \nКод ошибки: " + str(response.status_code) + " &#9888;"
    response = response.json()
    if len(response) == 0:
        return "\n&#10060;\tРасписание еще не доступно.&#10060;"
    result = ''
    for key in response:
        for elem in response[key]:
            Prepod = Prepodi()
            Prepod.disciplName = elem["disciplName"]
            Prepod.disciplType = elem["disciplType"]
            Prepod.prepodName = elem["prepodName"]
            if elem["prepodName"].rstrip() == "":
                Prepod.prepodName = ":не задан:"
            prepodList.append(Prepod)
    prepodList.sort(key=lambda Prepodi: Prepodi.disciplName)

    resultList = []
    for elem in prepodList:
        
        res = "&#128104;&#8205;&#127979;[" + (str(elem.disciplType)).rstrip() + "] " + (str(elem.disciplName)).rstrip() + " \n" + ((str(elem.prepodName)).rstrip()).title()
        if res not in resultList:
            resultList.append(res)
    for row in resultList:
        result += "\n---------------------------------------------------\n" + row
    del Prepod
    return result[len("----------------------------------------------------"):]
            



command = command_class.Command()

command.keys = ['преподы', 'преподаватели', '!преподы', 'учителя']
command.desciption = 'список преподавателей и дисциплин'
command.process = info
command.payload = "prepod"