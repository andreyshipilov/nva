# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.is_published'
        db.add_column('reviews_review', 'is_published',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Review.is_published'
        db.delete_column('reviews_review', 'is_published')


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
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'short_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reviews']