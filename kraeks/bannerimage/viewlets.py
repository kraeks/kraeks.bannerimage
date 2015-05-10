# -*- coding: utf-8 -*-
# Copyright (c) 2004-2009 novareto GmbH
# lwalther@novareto.de
from zope.interface import Interface
from uvc.api import api
import random
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContentTitle
from kraeks.bannerimage import bannerimageMessageFactory as _

api.templatedir('templates')

class HeaderBannerImageViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IPortalHeader)

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def refs(self, obj):
        """ returns a list of references """
        refs = [i.UID() for i in obj.getReferences('rel_titleimages')]
        brains = self.portal_catalog.searchResults(UID=refs)
        myrefs = []
        for i in brains:
            myrefs.append(i.getObject())
        return myrefs

    def available(self):
        if getattr(self.context, 'viewlet'):
            if getattr(self.context, 'viewlet') == 'header':
                return True
        return False

    def update(self):
        self.imagelist = []
        self.videopath = None
        self.imagepath = None
        if self.context.portal_type in ['Folder', 'Document', 'Topic', 'Collection']:
            if getattr(self.context, 'anzeige', False):
                titelbilder = self.refs(self.context)
                if titelbilder:
                    to = len(titelbilder)
                    if getattr(self.context, 'zufall', False):
                        imageindex = random.randint(0, to-1)
                        randimage = titelbilder[imageindex]
                        refurl = ''
                        #Verlinkung des Titelbildes mit einem Inhalt
                        if randimage.getReferences():
                            refurl = randimage.getReferences()[0].absolute_url()
                        #Lesen des Titelbildes
                        if randimage.getField('image'):
                            image = {'img':randimage.getField('image').tag(randimage, width="100%", height="100%"),
                                     'img-caption':randimage.title,
                                     'img-url': refurl}
                            self.imagelist.append(image)
                    else:
                        for i in range(to):
                            refurl = ''
                            #Verlinkung des Titelbildes mit einem Inhalt
                            if titelbilder[i].getReferences():
                                refurl = titelbilder[i].getReferences()[0].absolute_url()
                            if i == 0:
                                if titelbilder[i].getField('image'):
                                    image = {'data-slide':i,
                                             'class':'active',
                                             'item-class':'item active',
                                             'img':titelbilder[i].getField('image').tag(titelbilder[i], width="", height=""),
                                             'img-caption':titelbilder[i].title,
                                             'img-url': refurl}
                                    self.imagelist.append(image)
                            else:
                                if titelbilder[i].getField('image'):
                                    image = {'data-slide':i,
                                             'class':'',
                                             'item-class':'item',
                                             'img':titelbilder[i].getField('image').tag(titelbilder[i], width="", height=""),
                                             'img-caption':titelbilder[i].title,
                                             'img-url': refurl}
                                    self.imagelist.append(image)
                    if self.context.getReferences('rel_videopath'):
                        self.videopath = self.context.getReferences('rel_videopath')[0].absolute_url()
                    if self.context.getReferences('rel_imagepath'):
                        self.imagepath = self.context.getReferences('rel_imagepath')[0].absolute_url()
        return

class TitleBannerImageViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IAboveContentTitle)

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def refs(self, obj):
        """ returns a list of references """
        refs = [i.UID() for i in obj.getReferences('rel_titleimages')]
        brains = self.portal_catalog.searchResults(UID=refs)
        myrefs = []
        for i in brains:
            myrefs.append(i.getObject())
        return myrefs

    def available(self):
        if getattr(self.context, 'viewlet'):
            if getattr(self.context, 'viewlet')[0] == 'abovetitle':
                 return True
        return False

    def update(self):
        self.imagelist = []
        self.videopath = None
        self.imagepath = None
        if self.context.portal_type in ['Folder', 'Document', 'Topic', 'Collection']:
            if getattr(self.context, 'anzeige', False):
                titelbilder = self.refs(self.context)
                if titelbilder:
                    to = len(titelbilder)
                    if getattr(self.context, 'zufall', False):
                        imageindex = random.randint(0, to-1)
                        randimage = titelbilder[imageindex]
                        refurl = ''
                        #Verlinkung des Titelbildes mit einem Inhalt
                        if randimage.getReferences():
                            refurl = randimage.getReferences()[0].absolute_url()
                        #Lesen des Titelbildes
                        if randimage.getField('image'):
                            image = {'img':randimage.getField('image').tag(randimage, width="100%", height="100%"),
                                     'img-caption':randimage.title,
                                     'img-url': refurl}
                            self.imagelist.append(image)
                    else:
                        for i in range(to):
                            refurl = ''
                            #Verlinkung des Titelbildes mit einem Inhalt
                            if titelbilder[i].getReferences():
                                refurl = titelbilder[i].getReferences()[0].absolute_url()
                            if i == 0:
                                if titelbilder[i].getField('image'):
                                    image = {'data-slide':i,
                                             'class':'active',
                                             'item-class':'item active',
                                             'img':titelbilder[i].getField('image').tag(titelbilder[i], width="", height=""),
                                             'img-caption':titelbilder[i].title,
                                             'img-url': refurl}
                                    self.imagelist.append(image)
                            else:
                                if titelbilder[i].getField('image'):
                                    image = {'data-slide':i,
                                             'class':'',
                                             'item-class':'item',
                                             'img':titelbilder[i].getField('image').tag(titelbilder[i], width="", height=""),
                                             'img-caption':titelbilder[i].title,
                                             'img-url': refurl}
                                    self.imagelist.append(image)
                    if self.context.getReferences('rel_videopath'):
                        self.videopath = self.context.getReferences('rel_videopath')[0].absolute_url()
                    if self.context.getReferences('rel_imagepath'):
                        self.imagepath = self.context.getReferences('rel_imagepath')[0].absolute_url()
        return
