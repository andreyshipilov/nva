# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table('banners_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('big_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('medium_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('small_text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bg_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work.Product'], null=True, blank=True)),
        ))
        db.send_create_signal('banners', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table('banners_banner')


    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'bg_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'big_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medium_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work.Product']", 'null': 'True', 'blank': 'True'}),
            'small_text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Manager']", 'null': 'True', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['work.ProductType']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'work.producttype': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ProductType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['banners']