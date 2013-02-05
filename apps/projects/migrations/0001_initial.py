# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table('projects_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('projects', ['Client'])

        # Adding model 'Field'
        db.create_table('projects_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('projects', ['Field'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Client'], null=True, blank=True)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field field on 'Project'
        db.create_table('projects_project_field', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('field', models.ForeignKey(orm['projects.field'], null=False))
        ))
        db.create_unique('projects_project_field', ['project_id', 'field_id'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table('projects_client')

        # Deleting model 'Field'
        db.delete_table('projects_field')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field field on 'Project'
        db.delete_table('projects_project_field')


    models = {
        'projects.client': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'projects.field': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Field'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'projects.project': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Client']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'field': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'fields'", 'blank': 'True', 'to': "orm['projects.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']