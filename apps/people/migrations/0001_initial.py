# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Human'
        db.create_table('people_human', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('people', ['Human'])

        # Adding model 'Manager'
        db.create_table('people_manager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('people', ['Manager'])


    def backwards(self, orm):
        # Deleting model 'Human'
        db.delete_table('people_human')

        # Deleting model 'Manager'
        db.delete_table('people_manager')


    models = {
        'people.human': {
            'Meta': {'ordering': "('full_name',)", 'object_name': 'Human'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'people.manager': {
            'Meta': {'ordering': "('full_name',)", 'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['people']