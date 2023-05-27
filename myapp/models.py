from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Absence(models.Model):
    abno = models.CharField(db_column='abNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey('Manager', models.DO_NOTHING, db_column='Man_staffNo')  # Field name made lowercase.
    abreason = models.TextField(db_column='abReason', blank=True, null=True)  # Field name made lowercase.
    abapplydate = models.DateField(db_column='abApplyDate', blank=True, null=True)  # Field name made lowercase.
    abstartdate = models.DateField(db_column='abStartDate', blank=True, null=True)  # Field name made lowercase.
    abenddate = models.DateField(db_column='abEndDate', blank=True, null=True)  # Field name made lowercase.
    abstatu = models.CharField(db_column='abStatu', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Absence'


class Attendancerecord(models.Model):
    recordno = models.CharField(db_column='recordNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    recorddate = models.DateField(db_column='recordDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AttendanceRecord'


class Businesstrip(models.Model):
    btno = models.CharField(db_column='btNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey('Manager', models.DO_NOTHING, db_column='Man_staffNo')  # Field name made lowercase.
    btcontent = models.TextField(db_column='btContent', blank=True, null=True)  # Field name made lowercase.
    btapplydate = models.DateField(db_column='btApplyDate', blank=True, null=True)  # Field name made lowercase.
    btstartdate = models.DateField(db_column='btStartDate', blank=True, null=True)  # Field name made lowercase.
    btenddate = models.DateField(db_column='btEndDate', blank=True, null=True)  # Field name made lowercase.
    btstatu = models.CharField(db_column='btStatu', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BusinessTrip'


class Department(models.Model):
    departmentno = models.CharField(db_column='departmentNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Manager', models.DO_NOTHING, db_column='staffNo', blank=True, null=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='departmentName', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Department'


class Departmentposition(models.Model):
    positionno = models.CharField(db_column='positionNo', primary_key=True, max_length=20)  # Field name made lowercase.
    departmentno = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentNo')  # Field name made lowercase.
    positionname = models.CharField(db_column='positionName', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DepartmentPosition'


class Leave(models.Model):
    leaveno = models.CharField(db_column='leaveNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey('Manager', models.DO_NOTHING, db_column='Man_staffNo')  # Field name made lowercase.
    leavereason = models.TextField(db_column='leaveReason', blank=True, null=True)  # Field name made lowercase.
    leaveapplydate = models.DateField(db_column='leaveApplyDate', blank=True, null=True)  # Field name made lowercase.
    leavestatu = models.CharField(db_column='leaveStatu', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Leave'


class Mail(models.Model):
    mailno = models.CharField(db_column='mailNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='arrivalDate', blank=True, null=True)  # Field name made lowercase.
    arrivaltime = models.TimeField(db_column='arrivalTime', blank=True, null=True)  # Field name made lowercase.
    mailcontent = models.TextField(db_column='mailContent', blank=True, null=True)  # Field name made lowercase.
    mailtype = models.CharField(db_column='mailType', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Mail'


class Manager(models.Model):
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo', primary_key=True)  # Field name made lowercase.
    departmentno = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentNo', blank=True, null=True)  # Field name made lowercase.
    positionno = models.CharField(db_column='positionNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    staffname = models.CharField(db_column='staffName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    identitycard = models.CharField(db_column='identityCard', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    phoneno = models.CharField(db_column='phoneNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=25, blank=True, null=True)
    entrydate = models.DateField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    avatar = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Manager'


class Meeting(models.Model):
    meetingno = models.CharField(db_column='meetingNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey(Manager, models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    meetingname = models.CharField(db_column='meetingName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    meetingstarttime = models.TimeField(db_column='meetingStartTime', blank=True, null=True)  # Field name made lowercase.
    meetingendtime = models.TimeField(db_column='meetingEndTime', blank=True, null=True)  # Field name made lowercase.
    meetingdate = models.DateField(db_column='meetingDate', blank=True, null=True)  # Field name made lowercase.
    meetingcontent = models.TextField(db_column='meetingContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Meeting'


class Overtime(models.Model):
    overno = models.CharField(db_column='overNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey(Manager, models.DO_NOTHING, db_column='Man_staffNo')  # Field name made lowercase.
    overreason = models.TextField(db_column='overReason', blank=True, null=True)  # Field name made lowercase.
    overapplydate = models.DateField(db_column='overApplyDate', blank=True, null=True)  # Field name made lowercase.
    overstarttime = models.DateTimeField(db_column='overStartTime', blank=True, null=True)  # Field name made lowercase.
    overendtime = models.DateTimeField(db_column='overEndTime', blank=True, null=True)  # Field name made lowercase.
    overstatu = models.CharField(db_column='overStatu', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Overtime'


class Reimbursement(models.Model):
    reimno = models.CharField(db_column='reimNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey(Manager, models.DO_NOTHING, db_column='Man_staffNo')  # Field name made lowercase.
    reimamount = models.FloatField(db_column='reimAmount', blank=True, null=True)  # Field name made lowercase.
    reimitem = models.TextField(db_column='reimItem', blank=True, null=True)  # Field name made lowercase.
    reimapplydate = models.DateField(db_column='reimApplyDate', blank=True, null=True)  # Field name made lowercase.
    reimstatu = models.CharField(db_column='reimStatu', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Reimbursement'


class Salary(models.Model):
    payrollno = models.CharField(db_column='payrollNo', primary_key=True, max_length=20)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffNo')  # Field name made lowercase.
    basicsalary = models.FloatField(db_column='basicSalary', blank=True, null=True)  # Field name made lowercase.
    insurance = models.FloatField(blank=True, null=True)
    bonus = models.FloatField(blank=True, null=True)
    supplement = models.FloatField(blank=True, null=True)
    overtimepay = models.FloatField(db_column='overtimePay', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Salary'


class Staff(models.Model):
    staffno = models.CharField(db_column='staffNo', primary_key=True, max_length=20)  # Field name made lowercase.
    departmentno = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentNo')  # Field name made lowercase.
    positionno = models.ForeignKey(Departmentposition, models.DO_NOTHING, db_column='positionNo')  # Field name made lowercase.
    man_staffno = models.ForeignKey(Manager, models.DO_NOTHING, db_column='Man_staffNo', blank=True, null=True)  # Field name made lowercase.
    staffname = models.CharField(db_column='staffName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    identitycard = models.CharField(db_column='identityCard', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=25, blank=True, null=True)
    entrydate = models.DateField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    avatar = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)

    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    sex = models.IntegerField(blank=True, null=True,choices=gender_choices)

    class Meta:
        managed = True
        db_table = 'Staff'


class Admin(models.Model):
    adminNo = models.CharField(db_column='adminNo', primary_key=True, max_length=20)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Admin'

class Participate(models.Model):
    staffno = models.ForeignKey(Staff, models.DO_NOTHING, db_column='staffNo', primary_key=True)  # Field name made lowercase.
    meetingno = models.ForeignKey(Meeting, models.DO_NOTHING, db_column='meetingNo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'participate'
        unique_together = (('staffno', 'meetingno'),)
