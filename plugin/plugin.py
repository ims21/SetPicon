<<<<<<< HEAD
# for localized messages
from . import _
#################################################################################
#
#    Plugin for Enigma2
#    version:
VERSION = "1.08"
#    Coded by ims (c)2014
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#################################################################################

from Plugins.Plugin import PluginDescriptor
from Components.config import ConfigSubsection, config, ConfigSelection

config.plugins.AnalogClock = ConfigSubsection()
config.plugins.AnalogClock.where = ConfigSelection(default = "0", choices = [("0",_("plugins")),("1",_("menu-system"))])

def startsetup(menuid, **kwargs):
	if menuid != "system":
		return [ ]
	return [(_("Setup AnalogClock"), main, "analog_clock", None)]

def sessionstart(reason, **kwargs):
	if reason == 0:
		import ui
		ui.AnalogClock.startAnalogClock(kwargs["session"])

def main(session,**kwargs):
	import ui
	session.open(ui.AnalogClockSetup)

def Plugins(path, **kwargs):
	name = "Permanent Analog Clock"
	descr = _("Displays analog clock permanently on the screen")
	list = [PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart),]
	if config.plugins.AnalogClock.where.value == "0":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_PLUGINMENU, needsRestart = True, icon = 'aclock.png', fnc=main))
	elif config.plugins.AnalogClock.where.value == "1":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_MENU, needsRestart = True, fnc=startsetup))
	return list
=======
# for localized messages  	 
from . import _
#
#  Set Picon - Plugin E2
#
#  by ims (c) 2012 ims21@users.sourceforge.net
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#

from Plugins.Plugin import PluginDescriptor
from Components.config import ConfigSubsection, config, ConfigYesNo

config.plugins.setpicon = ConfigSubsection()
config.plugins.setpicon.extmenu = ConfigYesNo(default=True)

def main(session, servicelist=None, **kwargs):
	global Servicelist
	Servicelist = servicelist
	global epg_bouquet
	epg_bouquet = Servicelist and Servicelist.getRoot()
	if epg_bouquet is not None:
		import ui
		from ServiceReference import ServiceReference
		services = ui.getBouquetServices(epg_bouquet)
		session.openWithCallback(ui.closed, ui.setPicon, plugin_path, services, ServiceReference(epg_bouquet).getServiceName())

def Plugins(path,**kwargs):
	global plugin_path
    	plugin_path = path
	name="SetPicon"
	descr=_("set picon to service")
	list = [ PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart = False, fnc=main),]
	if config.plugins.setpicon.extmenu.value:
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart = False, fnc=main))
	return list
>>>>>>> 4de93d21503aeac6b4512dc517af824ff73e5db1
