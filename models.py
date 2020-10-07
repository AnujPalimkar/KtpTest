# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointmentsdetail(models.Model):
    idappointmentsdetail = models.AutoField(db_column='idAppointmentsdetail', primary_key=True)  # Field name made lowercase.
    date = models.DateField()
    time = models.TimeField()
    appointmentstatus = models.CharField(max_length=45)
    idclients = models.ForeignKey('Clients', models.DO_NOTHING, db_column='idclients')
    idpractioner = models.ForeignKey('Practioner', models.DO_NOTHING, db_column='idpractioner')

    class Meta:
        managed = False
        db_table = 'appointmentsdetail'


class Clients(models.Model):
    idclients = models.AutoField(db_column='idClients', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    contact_number = models.CharField(db_column='contact number', max_length=45)  # Field renamed to remove unsuitable characters.
    city = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    height = models.CharField(max_length=45)
    weight = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'clients'


class Practioner(models.Model):
    idpractioner = models.AutoField(db_column='idPractioner', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'practioner'


class Recommendation(models.Model):
    idrecommendation = models.AutoField(db_column='idRecommendation', primary_key=True)  # Field name made lowercase.
    stresslevel = models.CharField(db_column='stressLevel', max_length=45)  # Field name made lowercase.
    cholestrol = models.CharField(db_column='Cholestrol', max_length=45)  # Field name made lowercase.
    bloodpressure = models.CharField(max_length=45)
    idclients = models.ForeignKey(Clients, models.DO_NOTHING, db_column='idclients')
    idpractioner = models.ForeignKey(Practioner, models.DO_NOTHING, db_column='idpractioner')
    idappointmentdetails = models.ForeignKey(Appointmentsdetail, models.DO_NOTHING, db_column='idappointmentdetails')

    class Meta:
        managed = False
        db_table = 'recommendation'
