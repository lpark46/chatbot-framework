# myapp/db_routers.py

class MyAppRouter:
    """
    A router to control all database operations on models in the
    external application.
    """
    route_app_labels = {'kakao_app'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read external_app models go to external.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'external'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write external_app models go to external.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'external'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the external_app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the external_app's models get created on the right database.
        """
        if app_label in self.route_app_labels:
            return db == 'external'
        return db == 'default'
