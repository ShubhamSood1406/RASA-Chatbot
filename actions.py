# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import numpy as np
import sqlite3  # to connect to db
import smtplib  # to send mail
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class DisplayEventDetails(Action):

    def name(self) -> Text:
        return "display_event_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('events_list.db')
        user_message = str((tracker.latest_message)['text'])

        print("User message : ", user_message)
        if "Delhi" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Delhi')
        elif "Ahmedabad" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Ahmedabad')
        elif "Mumbai" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Mumbai')
        elif "Bangalore" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Bangalore')
        elif "Goa" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities  is '{0}'".format('Goa')
        elif "Kolkata" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities  is '{0}'".format('Kolkata')
        elif "Chandigarh" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities  is '{0}'".format('Chandigarh')
        elif "Online" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities  is '{0}'".format('Online')

        content = conn.execute(exe_str)
        content_text = ''
        for index, value in enumerate(content):
            content_text += str(index + 1) + ". " + str(value[0]) + "  |  " + str(value[1]) + "  |  ₹ " + str(value[2]) + "/-\n"

        content_text += "Type the Event Number to book the Tickets"
        dispatcher.utter_message(text=content_text)

        return []

class EventChoseByUser(Action):

    def name(self) -> Text:
        return "event_chose_by_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('events_list.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []
        exe_str = ''
        # getting the user message from tracker
        for event in (list(tracker.events))[:]:
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[-2]
        print("messages : ",messages)
        print("user_message : ",user_message)

        city_name = ''

        if "Delhi" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Delhi')
            city_name = "Delhi"

        elif 'Ahmedabad' in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Ahmedabad')
            city_name = "Ahmedabad"

        elif 'Mumbai' in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Mumbai')
            city_name = "Mumbai"

        elif 'Bangalore' in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Bangalore')
            city_name = "Bangalore"

        elif 'Goa' in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Goa')
            city_name = "Goa"

        elif 'Kolkata' in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Kolkata')
            city_name = "Kolkata"

        elif "Chandigarh" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Chandigarh')
            city_name = "Chandigarh"

        elif "Online" in user_message:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Online')
            city_name = "Online"

        content = conn.execute(exe_str)
        user_input = str((tracker.latest_message)['text'])
        user_input = int(user_input)
        print("user_input : ", user_input)

        total = 0
        content_text = ''
        event_chosen = ''
        date_time = ''
        for index, value in enumerate(content):
            if index + 1 == user_input:
                total += value[2]
                event_chosen += value[0]
                date_time += value[1]


        content_text = "You are booking ticket for " + str(event_chosen) + " that is on " + str(date_time) + "." \
                                + " Price for one ticket is ₹ " + str(total)
        dispatcher.utter_message(text=content_text)

        return []

class TicketChoseByUser(Action):

    def name(self) -> Text:
        return "ticket_chose_by_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('events_list.db')
        user_message1 = str((tracker.latest_message)['text'])

        messages1 = []
        exe_str = ''
        # getting the user message from tracker
        for event in (list(tracker.events))[:]:
            if event.get("event") == "user":
                messages1.append(event.get("text"))

        user_message1 = messages1[-4]
        eventchose = messages1[-3]
        ec = int(eventchose)

        print("messages1 : ",messages1)
        print("user_message1 : ",user_message1)
        print("event chose : ", eventchose)

        city_name = ''

        if "Delhi" in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Delhi')
            city_name = "Delhi"

        elif 'Ahmedabad' in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Ahmedabad')
            city_name = "Ahmedabad"

        elif 'Mumbai' in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Mumbai')
            city_name = "Mumbai"

        elif 'Bangalore' in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Bangalore')
            city_name = "Bangalore"

        elif 'Goa' in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Goa')
            city_name = "Goa"

        elif 'Kolkata' in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Kolkata')
            city_name = "Kolkata"

        elif "Chandigarh" in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Chandigarh')
            city_name = "Chandigarh"

        elif "Online" in user_message1:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Online')
            city_name = "Online"

        try:
            content = conn.execute(exe_str)
            user_input1 = str((tracker.latest_message)['text'])

            num = ''
            for i in range(len(user_input1)):
                if (user_input1[i].isdigit()):
                    num = num+ user_input1[i]

            num = int(num)

            print("user_input1 : ", user_input1)
            print("num : ", num)

            total = 0
            content_text = ''
            event_chosen = ''
            date_time = ''
            for index, value in enumerate(content):
                if index + 1 == ec:
                    total += value[2]
                    event_chosen += value[0]
                    date_time += value[1]

            import numpy as np

            bill_no = []
            id = ''
            sep = ", "
            for i in range(num):
                bill_no.append(str(np.random.randint(1000000,9999999,1)[0]))

            id = sep.join(bill_no)


            total_amt = total*num

            print("num: ", num)
            print("total:", total)
            print("total amt: ", total_amt)

            content_text = "Your ticket is booked for " + str(event_chosen) + " that is on " + str(date_time) + "." \
                                + " Your total price for tickets is ₹ " + str(total_amt) + " and your Ticket Id is " + str(id)
            dispatcher.utter_message(text=content_text)


        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []


class UserGetTicketOnMail(Action):

    def name(self) -> Text:
        return "user_get_ticket_on_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('events_list.db')
        user_message2 = str((tracker.latest_message)['text'])

        messages2 = []
        exe_str = ''
        # getting the user message from tracker
        for event in (list(tracker.events))[:]:
            if event.get("event") == "user":
                messages2.append(event.get("text"))

        user_message2 = messages2[-5]
        eventchose1 = messages2[-4]
        num1 = messages2[-2]
        ec1 = int(eventchose1)

        print("messages2 : ",messages2)
        print("user_message2 : ",user_message2)
        print("event chose 1 : ", eventchose1)

        print("num 1 : ", num1)

        city_name = ''

        if "Delhi" in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Delhi')
            city_name = "Delhi"

        elif 'Ahmedabad' in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Ahmedabad')
            city_name = "Ahmedabad"

        elif 'Mumbai' in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Mumbai')
            city_name = "Mumbai"

        elif 'Bangalore' in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Bangalore')
            city_name = "Bangalore"

        elif 'Goa' in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Goa')
            city_name = "Goa"

        elif 'Kolkata' in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Kolkata')
            city_name = "Kolkata"

        elif "Chandigarh" in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Chandigarh')
            city_name = "Chandigarh"

        elif "Online" in user_message2:
            exe_str = "Select Events, Date_Time, Price from event_items where Cities is '{0}'".format('Online')
            city_name = "Online"

        try:
            content = conn.execute(exe_str)
            user_input2 = str((tracker.latest_message)['text'])

            print("user_input2 : ", user_input2)
            print("num 1: ", num1)

            total = 0
            content_text = ''
            event_chosen = ''
            date_time = ''
            for index, value in enumerate(content):
                if index + 1 == ec1:
                    total += value[2]
                    event_chosen += value[0]
                    date_time += value[1]


            num2 = ''
            for i in range(len(num1)):
                if (num1[i].isdigit()):
                    num2 = num2 + num1[i]

            num2 = int(num2)
            print("num 2 :", num2)
            import numpy as np

            bill_no = []
            id = ''
            sep = ", "
            for i in range(num2):
                bill_no.append(str(np.random.randint(1000000,9999999,1)[0]))

            id = sep.join(bill_no)


                #content = "Your tickets has been booked. And don't forget to mark the dates on the calender to be a part of this Amazing Event."
            total_amt = total*num2

            print("num 2: ", num2)
            print("total:", total)
            print("total amt: ", total_amt)

                # content_text = "Your ticket is booked for " + str(event_chosen) + " that is on " + str(date_time) + "." \
                #                     + " Your total price for tickets is ₹ " + str(total_amt) + " and your Ticket Id is " + str(id)
                # dispatcher.utter_message(text=content_text)
                # dispatcher.utter_message(text=content)

            toaddrs = user_input2
            print("toaddrs : ", toaddrs)

            fromaddr = 'shubham14600.ss@gmail.com'
            #toaddrs = 'gottaname.m3@gmail.com'

            #msg = "\n Your ticket is booked for " + str(event_chosen) + " that is on " + str(date_time) + "." + "\n Your total price for tickets is Rs. " + str(total_amt) + " and your Ticket Id is " + str(id) + "\n \nHappy Eventing with Us. :)"
            TEXT = "\n Your ticket is booked for " + str(event_chosen) + " that is on " + str(date_time) + "." + "\n Your total price for tickets is Rs. " + str(total_amt) + " and your Ticket Id is " + str(id) + "\n \nHappy Eventing with Us. :)"
            SUBJECT = "Your booked tickets from Eve"
            msg = 'Subject: {}\n\n{}'.format(SUBJECT,TEXT)

            username = 'shubham14600.ss@gmail.com'
            obj = open('pass.txt')
            password = obj.read()
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
                #content = "The order has been taken and the respective restaurent will be notified"

                #content_text = "Your order has been received and your total order is " + str(total) + \
                #               " and your bill number is " + str(bill_no)
                #dispatcher.utter_message(text=content_text)
                #dispatcher.utter_message(text=content)

            content = "Your tickets has been booked and send on your Mail. \nDon't forget to mark the dates on the calender to be a part of this Amazing Event. \nThank You"

            dispatcher.utter_message(text=content)

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []
