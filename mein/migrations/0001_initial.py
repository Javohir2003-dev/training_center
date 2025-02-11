
from django.db import migrations, models


class Migration(migrations.Migration):

     
         
   

            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
    

