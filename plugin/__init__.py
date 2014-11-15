# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext

def localeInit():
<<<<<<< HEAD
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os_environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("AnalogClock", resolveFilename(SCOPE_PLUGINS, "Extensions/AnalogClock/locale"))

def _(txt):
	t = gettext.dgettext("AnalogClock", txt)
	if t == txt:
		#print "[AnalogClock] fallback to default translation for", txt
=======
	gettext.bindtextdomain("SetPicon", resolveFilename(SCOPE_PLUGINS, "Extensions/SetPicon/locale"))

def _(txt):
	t = gettext.dgettext("SetPicon", txt)
	if t == txt:
		print "[SetPicon] fallback to default translation for", txt
>>>>>>> 4de93d21503aeac6b4512dc517af824ff73e5db1
		t = gettext.gettext(txt)
	return t

localeInit()
<<<<<<< HEAD
language.addCallback(localeInit)
=======
language.addCallback(localeInit)
>>>>>>> 4de93d21503aeac6b4512dc517af824ff73e5db1
