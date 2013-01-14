# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('main_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('partner_status', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Institution'], null=True, blank=True)),
        ))
        db.send_create_signal('main', ['UserProfile'])

        # Adding M2M table for field course on 'UserProfile'
        db.create_table('main_userprofile_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('course', models.ForeignKey(orm['main.course'], null=False))
        ))
        db.create_unique('main_userprofile_course', ['userprofile_id', 'course_id'])

        # Adding M2M table for field buy_book on 'UserProfile'
        db.create_table('main_userprofile_buy_book', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('bookbuying', models.ForeignKey(orm['main.bookbuying'], null=False))
        ))
        db.create_unique('main_userprofile_buy_book', ['userprofile_id', 'bookbuying_id'])

        # Adding M2M table for field available_book_author on 'UserProfile'
        db.create_table('main_userprofile_available_book_author', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('bookavailableauthor', models.ForeignKey(orm['main.bookavailableauthor'], null=False))
        ))
        db.create_unique('main_userprofile_available_book_author', ['userprofile_id', 'bookavailableauthor_id'])

        # Adding M2M table for field partners on 'UserProfile'
        db.create_table('main_userprofile_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('main_userprofile_partners', ['userprofile_id', 'user_id'])

        # Adding model 'Institution'
        db.create_table('main_institution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('main', ['Institution'])

        # Adding M2M table for field student on 'Institution'
        db.create_table('main_institution_student', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('institution', models.ForeignKey(orm['main.institution'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('main_institution_student', ['institution_id', 'user_id'])

        # Adding model 'Message'
        db.create_table('main_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['auth.User'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='receiver', to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('elapse_time', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['Message'])

        # Adding model 'Book'
        db.create_table('main_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('isbn10', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('isbn13', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('edition', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Book'])

        # Adding model 'Course'
        db.create_table('main_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Institution'])),
            ('course_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('main', ['Course'])

        # Adding M2M table for field course_book on 'Course'
        db.create_table('main_course_course_book', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['main.course'], null=False)),
            ('book', models.ForeignKey(orm['main.book'], null=False))
        ))
        db.create_unique('main_course_course_book', ['course_id', 'book_id'])

        # Adding model 'Offer'
        db.create_table('main_offer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_offer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_offer', to=orm['auth.User'])),
            ('user_receive', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_receive', to=orm['auth.User'])),
            ('last_message', self.gf('django.db.models.fields.related.ForeignKey')(related_name='last_message', null=True, to=orm['main.Message'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('transaction_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_status', self.gf('django.db.models.fields.CharField')(default='new', max_length=3)),
            ('offer_type', self.gf('django.db.models.fields.CharField')(default='1', max_length=1)),
            ('offer_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
        ))
        db.send_create_signal('main', ['Offer'])

        # Adding M2M table for field messages on 'Offer'
        db.create_table('main_offer_messages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('offer', models.ForeignKey(orm['main.offer'], null=False)),
            ('message', models.ForeignKey(orm['main.message'], null=False))
        ))
        db.create_unique('main_offer_messages', ['offer_id', 'message_id'])

        # Adding model 'BookTransaction'
        db.create_table('main_booktransaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seller', to=orm['auth.User'])),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='buyer', null=True, to=orm['auth.User'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Book'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Course'], null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('status', self.gf('django.db.models.fields.CharField')(default='none', max_length=10)),
            ('transaction_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('transaction_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('post_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('alert_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['BookTransaction'])

        # Adding M2M table for field offer on 'BookTransaction'
        db.create_table('main_booktransaction_offer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booktransaction', models.ForeignKey(orm['main.booktransaction'], null=False)),
            ('offer', models.ForeignKey(orm['main.offer'], null=False))
        ))
        db.create_unique('main_booktransaction_offer', ['booktransaction_id', 'offer_id'])

        # Adding model 'Notify'
        db.create_table('main_notify', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('offer_content', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='new', max_length=3)),
            ('notify_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('notify_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notify_to', to=orm['auth.User'])),
            ('notify_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notify_from', to=orm['auth.User'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('elapse_time', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Notify'])

        # Adding model 'BookAvailableAuthor'
        db.create_table('main_bookavailableauthor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('alert_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('main', ['BookAvailableAuthor'])

        # Adding model 'BookBuying'
        db.create_table('main_bookbuying', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Book'])),
            ('alert_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('post_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
        ))
        db.send_create_signal('main', ['BookBuying'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('main_userprofile')

        # Removing M2M table for field course on 'UserProfile'
        db.delete_table('main_userprofile_course')

        # Removing M2M table for field buy_book on 'UserProfile'
        db.delete_table('main_userprofile_buy_book')

        # Removing M2M table for field available_book_author on 'UserProfile'
        db.delete_table('main_userprofile_available_book_author')

        # Removing M2M table for field partners on 'UserProfile'
        db.delete_table('main_userprofile_partners')

        # Deleting model 'Institution'
        db.delete_table('main_institution')

        # Removing M2M table for field student on 'Institution'
        db.delete_table('main_institution_student')

        # Deleting model 'Message'
        db.delete_table('main_message')

        # Deleting model 'Book'
        db.delete_table('main_book')

        # Deleting model 'Course'
        db.delete_table('main_course')

        # Removing M2M table for field course_book on 'Course'
        db.delete_table('main_course_course_book')

        # Deleting model 'Offer'
        db.delete_table('main_offer')

        # Removing M2M table for field messages on 'Offer'
        db.delete_table('main_offer_messages')

        # Deleting model 'BookTransaction'
        db.delete_table('main_booktransaction')

        # Removing M2M table for field offer on 'BookTransaction'
        db.delete_table('main_booktransaction_offer')

        # Deleting model 'Notify'
        db.delete_table('main_notify')

        # Deleting model 'BookAvailableAuthor'
        db.delete_table('main_bookavailableauthor')

        # Deleting model 'BookBuying'
        db.delete_table('main_bookbuying')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'edition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn10': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'main.bookavailableauthor': {
            'Meta': {'object_name': 'BookAvailableAuthor'},
            'alert_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.bookbuying': {
            'Meta': {'object_name': 'BookBuying'},
            'alert_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'})
        },
        'main.booktransaction': {
            'Meta': {'object_name': 'BookTransaction'},
            'alert_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Book']"}),
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'buyer'", 'null': 'True', 'to': "orm['auth.User']"}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Course']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'offer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Offer']", 'null': 'True', 'symmetrical': 'False'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seller'", 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '10'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'transaction_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'main.course': {
            'Meta': {'object_name': 'Course'},
            'course_book': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'course_book'", 'null': 'True', 'to': "orm['main.Book']"}),
            'course_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Institution']"})
        },
        'main.institution': {
            'Meta': {'object_name': 'Institution'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'main.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'elapse_time': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiver'", 'to': "orm['auth.User']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['auth.User']"})
        },
        'main.notify': {
            'Meta': {'ordering': "['date']", 'object_name': 'Notify'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'elapse_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notify_from'", 'to': "orm['auth.User']"}),
            'notify_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notify_to'", 'to': "orm['auth.User']"}),
            'notify_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'offer_content': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '3'})
        },
        'main.offer': {
            'Meta': {'object_name': 'Offer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'last_message'", 'null': 'True', 'to': "orm['main.Message']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'messages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'message'", 'null': 'True', 'to': "orm['main.Message']"}),
            'offer_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'offer_type': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'transaction_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_offer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_offer'", 'to': "orm['auth.User']"}),
            'user_receive': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_receive'", 'to': "orm['auth.User']"}),
            'view_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '3'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'available_book_author': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.BookAvailableAuthor']", 'null': 'True', 'blank': 'True'}),
            'buy_book': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.BookBuying']", 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Course']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner_status': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'partners'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Institution']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']