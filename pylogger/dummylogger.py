#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ["DummyLogger"]

class DummyLogger(object):
    """
        Dummy Logger. Never logs anything and never
        fails.
        Used to imitate normal logger, when you don't want to log anything (e.g.
        because you don't want to connect via Corba).
    """

    def start_session(self, *args, **kwargs):
        return True

    def create_request(self, *args, **kwargs):
        return DummyLogRequest()

    def create_dummy_request(self, *args, **kwargs):
        return DummyLogRequest()

    def create_request_login(self, *args, **kwargs):
        return DummyLogRequest()
        
    def close_session(self, *args, **kwargs): 
        return True


class DummyLogRequest(object):
    def __init__(self, *args, **kwargs):
        self.request_id = 1
    
    def close(self, *args, **kwargs):
        return True

