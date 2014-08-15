# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Filter'
        db.create_table(u'reports_filter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('options', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Filter'])

        # Adding model 'Filterset'
        db.create_table(u'reports_filterset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'reports', ['Filterset'])

        # Adding model 'FilterExtra'
        db.create_table(u'reports_filterextra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filterset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Filterset'])),
            ('filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Filter'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'reports', ['FilterExtra'])

        # Adding model 'Serie'
        db.create_table(u'reports_serie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=24, null=True, blank=True)),
            ('tick_format', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('query', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('validated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validated_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('validated_person', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('validation_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('last_execution_time', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('avg_execution_time', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Serie'])

        # Adding model 'SeriesStatistic'
        db.create_table(u'reports_seriesstatistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Serie'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('execution_time', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('params', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['SeriesStatistic'])

        # Adding model 'Report'
        db.create_table(u'reports_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='SI', max_length=2)),
            ('zoom', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pointlabels', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pointlabels_location', self.gf('django.db.models.fields.CharField')(default='n', max_length=2)),
            ('trendline', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('highlighter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('use_one_scale', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('scale_label_override', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('tracking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('legend', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('legend_location', self.gf('django.db.models.fields.CharField')(default='ne', max_length=2)),
            ('orientation', self.gf('django.db.models.fields.CharField')(default='v', max_length=1)),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding M2M table for field filtersets on 'Report'
        m2m_table_name = db.shorten_name(u'reports_report_filtersets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm[u'reports.report'], null=False)),
            ('filterset', models.ForeignKey(orm[u'reports.filterset'], null=False))
        ))
        db.create_unique(m2m_table_name, ['report_id', 'filterset_id'])

        # Adding model 'ReportStatistic'
        db.create_table(u'reports_reportstatistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('execution_time', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('params', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['ReportStatistic'])

        # Adding model 'SerieType'
        db.create_table(u'reports_serietype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Serie'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='BA', max_length=2)),
            ('zerobase', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'reports', ['SerieType'])

        # Adding model 'Menuitem'
        db.create_table(u'reports_menuitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'reports', ['Menuitem'])

        # Adding M2M table for field reports on 'Menuitem'
        m2m_table_name = db.shorten_name(u'reports_menuitem_reports')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menuitem', models.ForeignKey(orm[u'reports.menuitem'], null=False)),
            ('report', models.ForeignKey(orm[u'reports.report'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menuitem_id', 'report_id'])

        # Adding model 'UserPermission'
        db.create_table(u'reports_userpermission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('union', self.gf('django.db.models.fields.CharField')(default='I', max_length=1)),
        ))
        db.send_create_signal(u'reports', ['UserPermission'])

        # Adding M2M table for field reports on 'UserPermission'
        m2m_table_name = db.shorten_name(u'reports_userpermission_reports')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userpermission', models.ForeignKey(orm[u'reports.userpermission'], null=False)),
            ('report', models.ForeignKey(orm[u'reports.report'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userpermission_id', 'report_id'])

        # Adding model 'UserPermissionFilterValues'
        db.create_table(u'reports_userpermissionfiltervalues', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userpermission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.UserPermission'])),
            ('filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Filter'])),
            ('options', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['UserPermissionFilterValues'])

        # Adding model 'GroupPermission'
        db.create_table(u'reports_grouppermission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'], unique=True)),
        ))
        db.send_create_signal(u'reports', ['GroupPermission'])

        # Adding M2M table for field reports on 'GroupPermission'
        m2m_table_name = db.shorten_name(u'reports_grouppermission_reports')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('grouppermission', models.ForeignKey(orm[u'reports.grouppermission'], null=False)),
            ('report', models.ForeignKey(orm[u'reports.report'], null=False))
        ))
        db.create_unique(m2m_table_name, ['grouppermission_id', 'report_id'])

        # Adding model 'GroupPermissionFilterValues'
        db.create_table(u'reports_grouppermissionfiltervalues', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grouppermission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.GroupPermission'])),
            ('filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Filter'])),
            ('options', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['GroupPermissionFilterValues'])

    def backwards(self, orm):
        # Deleting model 'Filter'
        db.delete_table(u'reports_filter')

        # Deleting model 'Filterset'
        db.delete_table(u'reports_filterset')

        # Deleting model 'FilterExtra'
        db.delete_table(u'reports_filterextra')

        # Deleting model 'Serie'
        db.delete_table(u'reports_serie')

        # Deleting model 'SeriesStatistic'
        db.delete_table(u'reports_seriesstatistic')

        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Removing M2M table for field filtersets on 'Report'
        db.delete_table(db.shorten_name(u'reports_report_filtersets'))

        # Deleting model 'ReportStatistic'
        db.delete_table(u'reports_reportstatistic')

        # Deleting model 'SerieType'
        db.delete_table(u'reports_serietype')

        # Deleting model 'Menuitem'
        db.delete_table(u'reports_menuitem')

        # Removing M2M table for field reports on 'Menuitem'
        db.delete_table(db.shorten_name(u'reports_menuitem_reports'))

        # Deleting model 'UserPermission'
        db.delete_table(u'reports_userpermission')

        # Removing M2M table for field reports on 'UserPermission'
        db.delete_table(db.shorten_name(u'reports_userpermission_reports'))

        # Deleting model 'UserPermissionFilterValues'
        db.delete_table(u'reports_userpermissionfiltervalues')

        # Deleting model 'GroupPermission'
        db.delete_table(u'reports_grouppermission')

        # Removing M2M table for field reports on 'GroupPermission'
        db.delete_table(db.shorten_name(u'reports_grouppermission_reports'))

        # Deleting model 'GroupPermissionFilterValues'
        db.delete_table(u'reports_grouppermissionfiltervalues')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reports.filter': {
            'Meta': {'ordering': "['name']", 'object_name': 'Filter'},
            'default': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'reports.filterextra': {
            'Meta': {'object_name': 'FilterExtra'},
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Filter']"}),
            'filterset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Filterset']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'reports.filterset': {
            'Meta': {'ordering': "['name']", 'object_name': 'Filterset'},
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reports.Filter']", 'through': u"orm['reports.FilterExtra']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'reports.grouppermission': {
            'Meta': {'object_name': 'GroupPermission'},
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reports.Filter']", 'through': u"orm['reports.GroupPermissionFilterValues']", 'symmetrical': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reports': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reports.Report']", 'null': 'True', 'blank': 'True'})
        },
        u'reports.grouppermissionfiltervalues': {
            'Meta': {'object_name': 'GroupPermissionFilterValues'},
            'default': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Filter']"}),
            'grouppermission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.GroupPermission']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.menuitem': {
            'Meta': {'ordering': "['order', 'title']", 'object_name': 'Menuitem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reports': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reports.Report']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'reports.report': {
            'Meta': {'ordering': "['title']", 'object_name': 'Report'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'filtersets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reports.Filterset']", 'null': 'True', 'blank': 'True'}),
            'highlighter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legend_location': ('django.db.models.fields.CharField', [], {'default': "'ne'", 'max_length': '2'}),
            'orientation': ('django.db.models.fields.CharField', [], {'default': "'v'", 'max_length': '1'}),
            'pointlabels': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pointlabels_location': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '2'}),
            'scale_label_override': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reports.Serie']", 'through': u"orm['reports.SerieType']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tracking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trendline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'SI'", 'max_length': '2'}),
            'use_one_scale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zoom': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'reports.reportstatistic': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'ReportStatistic'},
            'execution_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reports.serie': {
            'Meta': {'ordering': "['name']", 'object_name': 'Serie'},
            'avg_execution_time': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'last_execution_time': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'tick_format': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'validated_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'validated_person': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'validation_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.seriesstatistic': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'SeriesStatistic'},
            'execution_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Serie']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reports.serietype': {
            'Meta': {'object_name': 'SerieType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Serie']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'BA'", 'max_length': '2'}),
            'zerobase': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'reports.userpermission': {
            'Meta': {'object_name': 'UserPermission'},
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reports.Filter']", 'through': u"orm['reports.UserPermissionFilterValues']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reports': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reports.Report']", 'null': 'True', 'blank': 'True'}),
            'union': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'reports.userpermissionfiltervalues': {
            'Meta': {'object_name': 'UserPermissionFilterValues'},
            'default': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Filter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'userpermission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.UserPermission']"})
        }
    }

    complete_apps = ['reports']
