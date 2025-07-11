import imaplib
import email
from email.header import decode_header
from config.env import EMAIL_ADDRESS, EMAIL_PASSWORD



def connect_to_gmail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return mail


def get_last_email():
    mail = connect_to_gmail()
    mail.select("inbox")

    # Search for all unread emails
    status, messages = mail.search(None, '(UNSEEN)')
    if status != "OK":
        return None

    email_ids = messages[0].split()
    if not email_ids:
        return None

    last_email_id = email_ids[-1].decode()
    return last_email_id


def get_email_content(email_id):
    mail = connect_to_gmail()
    mail.select("inbox")

    status, data = mail.fetch(email_id, "(RFC822)")
    if status != "OK":
        return "Error fetching email."

    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Decode subject
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")

    # Extract body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                charset = part.get_content_charset()
                body = part.get_payload(decode=True).decode(charset or "utf-8", errors="ignore")
                break
    else:
        charset = msg.get_content_charset()
        body = msg.get_payload(decode=True).decode(charset or "utf-8", errors="ignore")

    return f"Subject: {subject}\n\n{body.strip()}"
