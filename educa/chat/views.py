from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render


@login_required
def course_chat_room(request, course_id):
    try:
        # Retrieve course with given id joined by the current user
        course = request.user.courses_joined.get(id=course_id)
    except:  # NOQA: E722
        # User is not a student of the course or course does not exist
        return HttpResponseForbidden()
    return render(request, "chat/room.html", {"course": course})
