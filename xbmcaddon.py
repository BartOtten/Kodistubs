# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
Kodi's addon class
"""
#vl.maksime
from __future__ import unicode_literals
import xbmc as _xbmc
import os
from future.utils import PY26, PY27, PY2, PY3
import xml.etree.cElementTree as etree
try:
    etree.fromstring('<?xml version="1.0"?><foo><bar/></foo>')
except TypeError:
    import xml.etree.ElementTree as etree

if not PY26:
#
    from typing import Union

__kodistubs__ = True

#vl.maksime
if PY3:
    str_type = str
elif PY27:
#
    str_type = Union[str, unicode]

#vl.maksime
_addons = {}
_default_addon = ''


def py2_decode(s, encoding='utf-8'):
    """
    Decode Python 2 ``str`` to ``unicode``

    In Python 3 the string is not changed.
    """
    if PY2 and isinstance(s, bytes):
        s = s.decode(encoding)
    return s

def init_addon(path, profile, set_default=False):
    global _default_addon

    addon_info = {'path': path,
                  'profile': profile,
                  }

    addon_xml = os.path.join(path, 'addon.xml')
    addon_root = etree.parse(addon_xml).getroot()

    addon_info['id'] = py2_decode(addon_root.attrib['id'])
    addon_info['version'] = py2_decode(addon_root.attrib['version'])
    addon_info['name'] = py2_decode(addon_root.attrib['name'])
    addon_info['author'] = py2_decode(addon_root.attrib['provider-name'])

    addon_settings = {}
    settings_xml = os.path.join(path, 'resources', 'settings.xml')
    if os.path.exists(settings_xml):
        settings_root = etree.parse(settings_xml).getroot()
        for item in settings_root:
            if item.tag == 'category':
                for setting in item:
                    _add_addon_settings(addon_settings, setting)
            elif item.tag == 'setting':
                _add_addon_settings(addon_settings, item)

    _addons[addon_info['id']] = {'info': addon_info,
                                 'settings': addon_settings}
    
    if set_default:
        _default_addon = addon_info['id']

def _add_addon_settings(addon_settings, setting):
    setting_id = py2_decode(setting.attrib.get('id'))
    if setting_id is not None \
      and addon_settings.get(setting_id) is None:
        addon_settings[setting_id] = py2_decode(setting.attrib.get('default', ''))
#

class Addon(object):
    """
    Kodi's addon class

    Offers classes and functions that manipulate the add-on settings, information
    and localization.

    Creates a new AddOn class.

    :param id: [opt] string - id of the addon as specified in addon.xml

    Specifying the addon id is not needed. Important however is that the addon
    folder has the same name as the AddOn id provided in addon.xml.
    You can optionally specify the addon id from another installed addon
    to retrieve settings from it.**id** is optional as it will be auto detected
    for this add-on instance.

    Example::

        self.Addon = xbmcaddon.Addon()
        self.Addon = xbmcaddon.Addon('script.foo.bar')
    """
    
    def __init__(self, id=None):
        # type: (str) -> None

        #vl.maksime
        self._id = id or _default_addon
        
        addon_info = _addons.get(self._id, {})
        self._info = addon_info.get('info', {})
        self._settings = addon_info.get('settings', {})
        
        path = self._info.get('path', '')
        strings_po = os.path.join(path, 'resources', 'language',
                                  'resource.language.en_gb', 'strings.po')
        if not os.path.exists(strings_po):
            strings_po = os.path.join(path, 'resources', 'language',
                                      'English', 'strings.po')
        self._ui_strings = _xbmc._parse_po(strings_po)
        
        _xbmc.log('Created {0}'.format(self))
        #
        pass
    
    def getLocalizedString(self, id):
        # type: (int) -> unicode
        """
        Returns an addon's localized 'unicode string'. 

        :param id: integer - id# for string you want to localize. 
        :return: Localized 'unicode string'

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            locstr = self.Addon.getLocalizedString(32000)
        """
        #vl.maksime
        return self._ui_strings.get(id, u'')
        #
        return u""
    
    def getSetting(self, id):
        # type: (str) -> str
        """
        Returns the value of a setting as a unicode string. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a unicode string

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            apikey = self.Addon.getSetting('apikey')
        """

       #vl.maksime
        result = self._settings.get(id, '')
        _xbmc.log('{0}: getSetting(id={1}) -> {2}'.format(self, id, result))
        return result
        #
        return ""
    
    def getSettingBool(self, id):
        # type: (str) -> bool
        """
        Returns the value of a setting as a boolean. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a boolean

        New function added.

        Example::

            enabled = self.Addon.getSettingBool('enabled')
        """
        return True
    
    def getSettingInt(self, id):
        # type: (str) -> int
        """
        Returns the value of a setting as an integer. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as an integer

        New function added.

        Example::

            max = self.Addon.getSettingInt('max')
        """
        return 0
    
    def getSettingNumber(self, id):
        # type: (str) -> float
        """
        Returns the value of a setting as a floating point number. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a floating point number

        New function added.

        Example::

            max = self.Addon.getSettingNumber('max')
        """
        return 0.0
    
    def getSettingString(self, id):
        # type: (str) -> str
        """
        Returns the value of a setting as a unicode string. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a unicode string

        New function added.

        Example::

            apikey = self.Addon.getSettingString('apikey')
        """

        #vl.maksime
        result = self._settings.get(id, '')
        _xbmc.log('{0}: getSetting(id={1}) -> {2}'.format(self, id, result))
        return result
        #
        return ""
    
    def setSetting(self, id, value):
        # type: (str, str_type) -> None
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: string or unicode - value of the setting.

        You can use the above as keywords for arguments.**id** is optional
        as it will be auto detected for this add-on instance.

        Example::

            self.Addon.setSetting(id='username', value='teamkodi')
        """

        #vl.maksime
        self._settings[id] = value
        _xbmc.log('{0}: setSetting(id={1}, value={2})'.format(self, id, value))
        #
        pass
    
    def setSettingBool(self, id, value):
        # type: (str, bool) -> bool
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: boolean - value of the setting. 
        :return: True if the value of the setting was set, false otherwise

        You can use the above as keywords for arguments.

        New function added.

        Example::

            self.Addon.setSettingBool(id='enabled', value=True)
        """
        return True
    
    def setSettingInt(self, id, value):
        # type: (str, int) -> bool
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: integer - value of the setting. 
        :return: True if the value of the setting was set, false otherwise

        You can use the above as keywords for arguments.

        New function added.

        Example::

            self.Addon.setSettingInt(id='max', value=5)
        """
        return True
    
    def setSettingNumber(self, id, value):
        # type: (str, float) -> bool
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: float - value of the setting. 
        :return: True if the value of the setting was set, false otherwise

        You can use the above as keywords for arguments.

        New function added.

        Example::

            self.Addon.setSettingNumber(id='max', value=5.5)
        """
        return True
    
    def setSettingString(self, id, value):
        # type: (str, str_type) -> bool
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: string or unicode - value of the setting. 
        :return: True if the value of the setting was set, false otherwise

        You can use the above as keywords for arguments.

        New function added.

        Example::

            self.Addon.setSettingString(id='username', value='teamkodi')
        """
        return True
    
    def openSettings(self):
        # type: () -> None
        """
        Opens this scripts settings dialog. 

        Example::

            self.Addon.openSettings()
        """
        pass
    
    def getAddonInfo(self, id):
        # type: (str) -> str
        """
        Returns the value of an addon property as a string. 

        :param id: string - id of the property that the module needs to access.
            Choices for the property are:

        ======= ========== ============ ===========
        author  changelog  description  disclaimer 
        fanart  icon       id           name       
        path    profile    stars        summary    
        type    version                            
        ======= ========== ============ ===========

        :return: AddOn property as a string

        Example::

            version = self.Addon.getAddonInfo('version')
        """

        #vl.maksime
        result = self._info.get(id, '')
        _xbmc.log('{0}: getAddonInfo(id={1}) -> {2}'.format(self, id, result))
        return result
        #
        return ""

    #vl.maksime
    def __str__(self):
        return 'Addon(id={0})'.format(self._id)
    
    