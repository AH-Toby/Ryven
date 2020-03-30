from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node

import imaplib
import os
import email

# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        self.initialized()


    def update_event(self, input_called=-1):
        if input_called == 0:
            email_user = self.input(1)
            email_pass = self.input(2)

            mail = imaplib.IMAP4_SSL('imap.gmail.com')

            mail.login(email_user, email_pass)
            mail.select('INBOX') #

            subject = ''
            date = ''
            message = ''
            mail.select()

            t, data = mail.search(None, 'ALL')
            mail_ids = data[0]
            id_list = mail_ids.split()

            num = data[0].split()[-1]

            t, data = mail.fetch(num, '(RFC822)' )
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('ISO-8859-1')
            email_message = email.message_from_string(raw_email_string)

            date = email_message['date']
            subject = email_message['Subject']
            message = self.get_body(email_message)


            mail.close()
            self.set_output_val(1, subject)
            self.set_output_val(2, date)
            self.set_output_val(3, message)
            self.exec_output(0)

    def get_body(self, msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
