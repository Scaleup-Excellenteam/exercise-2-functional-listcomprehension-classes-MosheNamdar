class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def read_inbox(self, username, N=None):
        msg = self.boxes[username]
        if not msg:
            return []
        if N is None:
            N = len(msg)
        messages = msg[-N:]
        for x in messages:
            x['read'] = True
        return messages

    def search_inbox(self, username, string):
        msg = self.boxes[username]
        res = []
        for x in msg:
            if string in x['body'] or string in x['title']:
                res.append(x)
        return res

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

         :param str sender: The message sender's username.
         :param str recipient: The message recipient's username.
         :param str message_body: The body of the message.
         :param urgent: The urgency of the message.
         :type urgent: bool, optional
         :return: The message ID, auto incremented number.
         :rtype: int
         :raises KeyError: if the recipient does not exist.
         """
        if recipient not in self.boxes:
            raise KeyError("Recipient does not exist.")
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': f"Message from {sender}",
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id
