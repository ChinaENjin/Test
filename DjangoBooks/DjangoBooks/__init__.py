from __future__ import absolute_import
import pymysql
pymysql.install_as_MySQLdb()


from DjangoBooks.celery import app as celery_app


__all__ = ['celery_app']