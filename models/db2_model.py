# -*- coding: utf-8 -*-


db.define_table(
    'sport',

    Field('title', length=25, requires=[IS_NOT_EMPTY(), Titleize()]),

    auth.signature,
    singular='Sport', plural='Sports',
    format='%(title)s',
)

db.define_table(
    'tournament',
    Field('title', length=25, requires=[IS_NOT_EMPTY(), Titleize()]),
    Field('sport', db.sport),    
    Field('owner', db.auth_user),
    Field('start_date', 'date'),
    Field('finish_date', 'date'),  
    auth.signature,
    singular=T('Tournament'), plural=T('Tournaments'),
    format='%(title)s',
)
