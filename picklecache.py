#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Sythesizing tasks"""

import os
import pickle

class PickleCache(object):
    """This class has 2 arguments and it is a constructor function.

    Attributes:
        data(dictionary)
    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """ Class Constructor.

        Args:
            file_path(string, optional): defaults to 'datastore.pkl'
            autosync(bool, optional): defaults to False

        Returns:
            
        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """This function is a key value pairs with PickleCache class"""
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """This function returns length of self.__data"""
        return len(self.__data)

    def __getitem__(self, key):
        """This function uses the key to return the value from
            self.__data dictionary"""
        try:
            return self.__data[key]
        except:
            raise KeyError('a key cannot be found')

    def __delitem__(self, key):
        """This function removes any entries from self.__data attribute
        with key."""
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """This function loads the file and saves the content in self.__data"""
        if os.path.exists(self.__file_path) is True\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """This function saves stored data to file"""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
