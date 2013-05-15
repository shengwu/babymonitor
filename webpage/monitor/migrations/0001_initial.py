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
            ('max_vol', self.gf('django.db.models.fields.FloatField')(default=10)),
            ('min_temp', self.gf('django.db.models.fields.FloatField')(default=5)),
            ('max_temp', self.gf('django.db.models.fields.FloatField')(default=20)),
        ))
        db.send_create_signal(u'monitor', ['Baby'])

        # Adding model 'Sleep'
        db.create_table(u'monitor_sleep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Baby'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('interruptions', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'monitor', ['Sleep'])

        # Adding model 'Cry'
        db.create_table(u'monitor_cry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sleep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Sleep'])),
            ('baby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Baby'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('volume', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'monitor', ['Cry'])

        # Adding model 'DataPoint'
        db.create_table(u'monitor_datapoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sleep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Sleep'])),
            ('baby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Baby'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('temp', self.gf('django.db.models.fields.FloatField')()),
            ('humidity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'monitor', ['DataPoint'])


    def backwards(self, orm):
        # Deleting model 'Baby'
        db.delete_table(u'monitor_baby')

        # Deleting model 'Sleep'
        db.delete_table(u'monitor_sleep')

        # Deleting model 'Cry'
        db.delete_table(u'monitor_cry')

        # Deleting model 'DataPoint'
        db.delete_table(u'monitor_datapoint')


    models = {
        u'monitor.baby': {
            'Meta': {'object_name': 'Baby'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_temp': ('django.db.models.fields.FloatField', [], {'default': '20'}),
            'max_vol': ('django.db.models.fields.FloatField', [], {'default': '10'}),
            'min_temp': ('django.db.models.fields.FloatField', [], {'default': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Baby'", 'max_length': '30'})
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