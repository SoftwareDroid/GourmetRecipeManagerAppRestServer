# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Convtable(models.Model):
    id = models.AutoField(primary_key=True)
    ckey = models.CharField(blank=True, null=True,max_length=150)
    value = models.CharField(blank=True, null=True,max_length=150)

    class Meta:
        managed = False
        db_table = 'convtable'


class Crossunitdict(models.Model):
    id = models.AutoField(primary_key=True)
    cukey = models.CharField(blank=True, null=True,max_length=150)
    value = models.CharField(blank=True, null=True,max_length=150)

    class Meta:
        managed = False
        db_table = 'crossunitdict'


class Density(models.Model):
    id = models.AutoField(primary_key=True)
    dkey = models.CharField(blank=True, null=True,max_length=150)
    value = models.CharField(blank=True, null=True,max_length=150)

    class Meta:
        managed = False
        db_table = 'density'


class Info(models.Model):
    rowid = models.AutoField(primary_key=True)
    version_super = models.IntegerField(blank=True, null=True)
    version_major = models.IntegerField(blank=True, null=True)
    version_minor = models.IntegerField(blank=True, null=True)
    last_access = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'info'


class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING,related_name='recipe_id', blank=True, null=False)
    refid = models.ForeignKey('Recipe', models.DO_NOTHING,related_name='refid', db_column='refid', blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)  # This field type is a guess.
    rangeamount = models.FloatField(blank=True, null=True)  # This field type is a guess.
    item = models.TextField(blank=True, null=True)
    ingkey = models.TextField(blank=True, null=True)
    optional = models.BooleanField(blank=True, null=True)
    shopoptional = models.IntegerField(blank=True, null=True)
    inggroup = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Keylookup(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.TextField(blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    ingkey = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keylookup'


class Pantry(models.Model):
    id = models.AutoField(primary_key=True)
    ingkey = models.TextField(blank=True, null=True)
    pantry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pantry'


class PluginInfo(models.Model):
    plugin = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    version_super = models.IntegerField(blank=True, null=True)
    version_major = models.IntegerField(blank=True, null=True)
    version_minor = models.IntegerField(blank=True, null=True)
    plugin_version = models.CharField(blank=True, null=True,max_length=32)

    class Meta:
        managed = False
        db_table = 'plugin_info'


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    modifications = models.TextField(blank=True, null=True)
    cuisine = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True,validators=[MinValueValidator(0), MaxValueValidator(10)])
    description = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    preptime = models.IntegerField(blank=True, null=True)
    cooktime = models.IntegerField(blank=True, null=True)
    servings = models.FloatField(blank=True, null=True)  # This field type is a guess.
    yields = models.FloatField(blank=True, null=True)  # This field type is a guess.
    yield_unit = models.CharField(blank=True, null=True,max_length=32)
    image = models.BinaryField(blank=True, null=True)
    thumb = models.BinaryField(blank=True, null=True)
    # Forbid null because it does not occur in the normal db
    deleted = models.BooleanField(blank=True, null=False)
    recipe_hash = models.CharField(blank=True, null=True,max_length=32)
    ingredient_hash = models.CharField(blank=True, null=True,max_length=32)
    link = models.TextField(blank=True, null=True)
    last_modified = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Shopcats(models.Model):
    id = models.AutoField(primary_key=True)
    ingkey = models.TextField(blank=True, null=True)
    shopcategory = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopcats'


class Shopcatsorder(models.Model):
    id = models.AutoField(primary_key=True)
    shopcategory = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopcatsorder'


class Unitdict(models.Model):
    id = models.AutoField(primary_key=True)
    ukey = models.CharField(blank=True, null=True,max_length=150)
    value = models.CharField(blank=True, null=True,max_length=150)

    class Meta:
        managed = False
        db_table = 'unitdict'