## Generic Class Based Views
This views Classes live in `django.views.generic`\
If specifying **template_name** in a view class, for templates in the app folder, use the format: **app_name/template_name.html**\

### ListView
Used to display a list of objects. It requires a **model** attribute to be set.

### CreateView
Import from `django.views.generic.edit`. Create a form to create a new object.\
