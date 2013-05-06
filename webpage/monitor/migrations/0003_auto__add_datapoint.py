# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataPoint'
        db.create_table(u'monitor_datapoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('temp', self.gf('django.db.models.fields.FloatField')()),
            ('humidity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'monitor', ['DataPoint'])


    def backwards(self, orm):
        # Deleting model 'DataPoint'
        db.delete_table(u'monitor_datapoint')


    models = {
        u'monitor.baby': {
            'Meta': {'object_name': 'Baby'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Baby'", 'max_length': '30'})
        },
        u'monitor.cry': {
            'Meta': {'object_name': 'Cry'},
            'baby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Baby']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        },
        u'monitor.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'humidity': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'monitor.sleep': {
            'Meta': {'object_name': 'Sleep'},
            'baby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Baby']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interruptions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['monitor']