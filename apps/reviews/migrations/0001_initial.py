# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table('reviews_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('short_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal('reviews', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table('reviews_review')


    models = {
        'projects.project': {
            'Meta': {'ordering': "('project_title',)", 'object_name': 'Project'},
            'client_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'project_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reviews.review': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Review'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'short_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reviews']