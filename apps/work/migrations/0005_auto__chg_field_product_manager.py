# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.manager'
        db.alter_column('work_product', 'manager_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Manager'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Product.manager'
        raise RuntimeError("Cannot reverse this migration. 'Product.manager' and its values cannot be restored.")

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
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['work']