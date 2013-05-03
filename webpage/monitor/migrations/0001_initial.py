# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Baby'
        db.create_table(u'monitor_baby', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Baby', max_length=30)),
        ))
        db.send_create_signal(u'monitor', ['Baby'])

        # Adding model 'Cry'
        db.create_table(u'monitor_cry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Baby'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('volume', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'monitor', ['Cry'])

        # Adding model 'Sleep'
        db.create_table(u'monitor_sleep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Baby'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('interruptions', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'monitor', ['Sleep'])


    def backwards(self, orm):
        # Deleting model 'Baby'
        db.delete_table(u'monitor_baby')

        # Deleting model 'Cry'
        db.delete_table(u'monitor_cry')

        # Deleting model 'Sleep'
        db.delete_table(u'monitor_sleep')


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