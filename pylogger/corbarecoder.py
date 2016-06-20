#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import types


class UnsupportedEncodingError(Exception):
    pass


class DecodeError(Exception):
    pass


class CorbaRecode(object):

    def __init__(self, coding='utf-8'):
        object.__init__(self)
        self.BasicTypes = (
                types.BooleanType,
                types.FloatType,
                types.IntType,
                types.LongType
                )
        self.IterTypes = (
                types.TupleType,
                types.ListType
                )
        try:
            codecs.lookup(coding)
            self.coding = coding
        except LookupError, msg:
            raise UnsupportedEncodingError(msg)

    def decode(self, answer):
        if isinstance(answer, types.StringTypes):
            return answer.decode(self.coding)
        if isinstance(answer, self.BasicTypes):
            return answer
        elif isinstance(answer, self.IterTypes):
            return [self.decode(x) for x in answer]
        elif isinstance(answer, types.InstanceType):
            for name in dir(answer):
                item = getattr(answer, name)
                if name.startswith('__'):
                    continue  # internal python methods / attributes
                if isinstance(item, types.StringTypes):
                    answer.__dict__[name] = item.decode(self.coding)
                if name.startswith('_'):
                    continue  # internal module defined methods / attributes
                if isinstance(item, types.MethodType):
                    continue  # methods - don't call them
                if isinstance(item, types.InstanceType):
                    answer.__dict__[name] = self.decode(item)
                if isinstance(item, self.IterTypes):
                    answer.__dict__[name] = [self.decode(x) for x in item]
            return answer

    def encode(self, answer):
        if isinstance(answer, unicode):  # types.UnicodeType
            return answer.encode(self.coding)
        if isinstance(answer, str):
            return answer
        if isinstance(answer, self.BasicTypes):
            return answer
        elif isinstance(answer, self.IterTypes):
            return [self.encode(x) for x in answer]
        elif isinstance(answer, types.InstanceType):
            for name in dir(answer):
                item = getattr(answer, name)
                if name.startswith('__'):
                    continue  # internal python methods / attributes
                if isinstance(item, types.StringTypes):
                    answer.__dict__[name] = item.encode(self.coding)
                if name.startswith('_'):
                    continue  # internal module defined methods / attributes
                if isinstance(item, types.MethodType):
                    continue  # methods - don't call them
                if isinstance(item, types.InstanceType):
                    answer.__dict__[name] = self.encode(item)
                if isinstance(item, self.IterTypes):
                    answer.__dict__[name] = [self.encode(x) for x in item]
            return answer

recoder = CorbaRecode()
c2u = recoder.decode  # recode from corba string to unicode
u2c = recoder.encode  # recode from unicode to strings
