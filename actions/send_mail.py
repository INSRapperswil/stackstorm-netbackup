import smtplib
from email.message import EmailMessage
from lib.actions import BaseAction


class SendMail(BaseAction):
    def run(self, recipient_address, mail_server, mail_sender_address, mail_message):

        msg = EmailMessage()
        msg['From'] = mail_sender_address
        msg['To'] = recipient_address
        msg['Subject'] = "Network device backup failed!"
        msg.set_content(mail_message)

        try:
            with smtplib.SMTP(mail_server) as server_instance:
                server_instance.send_message(msg)
        except Exception as e:
            self.logger.error(e)
            return False, ""

        return True, "Mail transmitted successfully!"