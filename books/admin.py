from django.contrib import admin
from .models import *

admin.site.register(ReadenBook)
admin.site.register(Book)
admin.site.register(BookInVote)
admin.site.register(CurrentBook)
admin.site.register(VotedBook)