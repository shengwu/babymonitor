# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Baby.is_active'
        db.add_column(u'monitor_baby', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Baby.is_active'
        db.delete_column(u'monitor_baby', 'is_active')


    models = {
        u'monitor.baby': {
            'Meta': {'object_name': 'Baby'},
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_temp': ('django.db.models.fields.FloatField', [], {'default': '20'}),
            'max_vol': ('django.db.models.fields.FloatField', [], {'default': '10'}),
            'min_temp': ('django.db.models.fields.FloatField', [], {'default': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        },
        u'monitor.cry': {
            'Meta': {'object_name': 'Cry'},
            'baby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Baby']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'sleep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Sleep']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        },
        u'monitor.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'baby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Baby']"}),
            'humidity': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sleep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Sleep']"}),
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