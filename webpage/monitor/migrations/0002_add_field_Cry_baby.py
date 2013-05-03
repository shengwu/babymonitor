# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cry.baby'
        db.add_column(u'monitor_cry', 'baby',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['monitor.Baby']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cry.baby'
        db.delete_column(u'monitor_cry', 'baby_id')


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