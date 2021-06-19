=====
worker2
=====

worker2 is a Django worker1 to conduct Web-based worker1. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "worker2" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'worker2',
    ]

2. Include the worker2 URLconf in your project urls.py like this::

    path('worker2/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the worker2 models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a worker2 (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the worker2.