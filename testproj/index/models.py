from django.db import models

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types   ....   for field-types


# The META Sub-Class

# db_table = "dreamreal"               # override the default name of table creted in DB , must be in lowercase

# ordering = ['-order_date']           # a string which is a field name with an optional “-” prefix, which indicates descending order.
                                       # Fields without a leading “-” will be ordered ascending.
                                       # Use the string [“?”] to order randomly.
# ordering = ['-pub_date', 'author']   # order by "pub_date" descending, then by "author" ascending



class testdb(models.Model):
	name = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	roll = models.IntegerField(primary_key = True)

	class Meta:
		db_table = "stud"              # default would have been 'index_testdb'
		ordering = ["roll"]            # order by roll asc

