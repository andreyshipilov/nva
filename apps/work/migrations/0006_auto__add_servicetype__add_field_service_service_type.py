# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceType'
        db.create_table('work_servicetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('work', ['ServiceType'])

        # Adding field 'Service.service_type'
        db.add_column('work_service', 'service_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['work.ServiceType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ServiceType'
        db.delete_table('work_servicetype')

        # Deleting field 'Service.service_type'
        db.delete_column('work_service', 'service_type_id')


    models = {
        'people.manager': {
            'Meta': {'ordering': "('full_name',)", 'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'work.product': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Product'},
            'demo_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Manager']", 'null': 'True', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work.ProductType']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'work.producttype': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ProductType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'work.service': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Manager']", 'null': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work.ServiceType']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'work.servicetype': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ServiceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['work']