#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import email
import imaplib
import smtplib

from .pattern import memoized
from .str_ import Printable
from .testing import Matcher

OK = 'OK'


def all_ok(results):
    return all(x == OK for x in results)


class Account(Printable):
    def __init__(self, host, port, username, password, ssl=False):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssl = ssl


class GmailImapAccount(Account):
    host = 'imap.gmail.com'
    port = 993

    def __init__(self, username, password):
        Account.__init__(self, self.host, self.port, username, password)


class GmailSmtpAccount(Account):
    host = 'smtp.gmail.com'
    port = 587

    def __init__(self, username, password):
        Account.__init__(self, self.host, self.port, username, password)


class IMAP(Printable):
    """
    IMAP4 mailbox.
    See search operators at http://tools.ietf.org/html/rfc2060.html#section-6.4.4

    >>> account = GmailImapAccount(username='<user>', password='<pass>')
    >>> mailbox = IMAP(account)
    >>> mailbox.connect()
    >>> mailbox.messages()
    [...]
    >>> mailbox.messages('(SUBJECT {hi})')
    [...]
    >>> mailbox.messages('(ON 17-Feb-2013)')
    [...]
    """

    def __init__(self, account):
        self.account = account
        self.connection = None
        self.connected = self.connect()

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.account.host, self.account.port)
        assert self.connection is not None

        results = (
            self.connection.login(self.account.username,
                                  self.account.password)[0],
            self.connection.select()[0])

        return all_ok(results)

    @memoized
    def messages(self, query='ALL'):
        assert self.connection, 'not connected to server'

        result, msg_ids = self.connection.search(None, query)
        assert all_ok([result])

        results = []
        retval = []
        for num in msg_ids[0].split():
            result, msg = self.connection.fetch(num, '(RFC822)')
            retval.append(email.message_from_string(msg[0][1]))
            results.append(result)

        assert all_ok(results)
        return retval

    def __unicode__(self):
        return unicode(self.account['username'])


class SMTP(Printable):
    def __init__(self, account, fromaddr, ssl=False):
        self.account = account
        self.fromaddr = fromaddr
        self.ssl = ssl

    def sendmail(self, *args, **kargs):
        try:
            self._sendmail(*args, **kargs)
        except (KeyboardInterrupt, SystemExit):
            raise

    def _sendmail(self, toaddrs, subject, body):
        smtp = smtplib.SMTP(self.account.host, self.account.port)
        msg = u"From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
            self.fromaddr,
            str.join(",", toaddrs),
            subject,
            email.utils.formatdate(),
            unicode(body, 'utf-8'))

        if self.ssl:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

        smtp.login(self.account.username, self.account.password)
        smtp.sendmail(self.fromaddr, toaddrs, msg.encode('utf-8'))
        smtp.close()


class MeetsImapQuery(Matcher):
    def __init__(self, criteria):
        self.criteria = criteria

    def _matches(self, mailbox):
        messages = mailbox.messages(self.criteria)
        if not messages:
            return False

#        for m in messages:
#            print m['Subject']

        return True

    def describe_to(self, description):
        description.append_text("some mail meet '%s'" % self.criteria)


def meets_imap_query(criteria):
    return MeetsImapQuery(criteria)
